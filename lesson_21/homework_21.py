"""Homework 21."""

import logging
from datetime import datetime

"""
Моніторингова система клєнта надсилає сигнал,
що вона працездатна кожні 30-31 сек
- наприкладTimestamp 05:45:40, а в наступному повідомлені — Timestamp 05:45:09
(тут різниця heartbeat в 31 секунду)

Є декілька дублючих потоків, що шлють дані одночасно,
тож ми можемо проаналізувати лише один потік - Key TSTFEED0300|7E3E|0400

Засобами автоматизації проаналізуйте наданий нам лог: hblog.txt

відберіть лише строки з вказаним ключем Key TSTFEED0300|7E3E|0400
Створіть функцію, що поверне лог-файл, де буде аналіз правильності вимог:
для кожного випадку де heartbeat більше 31 сек але
менше 33 логувало WARNING в файл hb_test.log
для кожного випадку де heartbeat більше рівно 33
логувало ERROR в файл hb_test.log
3.Зверніть увагу, що нам для аналізу помилок було
б добре знати час, в який помилка відбулася.

Обов’язково включіть результат роботи — файл hb_test.log в PR.
"""


class HBAnalyzer:
    """Class to analyze heartbeat logs."""

    def __init__(self, log_file, key, timestamp_prefix,
                 warn_limit, err_limit, time_format='%H:%M:%S'):
        """Initialize parameters."""
        self.log_file = log_file
        self.key = key
        self.timestamp_prefix = timestamp_prefix
        self.warn_limit = warn_limit
        self.err_limit = err_limit
        self.time_format = time_format
        self.logger = self._configure_logger()

    def _configure_logger(self):
        """Configure logger."""
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler('hb_test.log', mode='a')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s - '
                                      '%(message)s', '%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def _read_lines(self):
        """Read lines from the log file."""
        try:
            with open(self.log_file, 'rt') as file:
                lines = file.readlines()
                if not lines:
                    self.logger.warning(f'The log file {self.log_file}'
                                        f' is empty.')
                return lines
        except FileNotFoundError:
            self.logger.error(f'File not found: {self.log_file}')
            return []

    def _extract_timestamp(self, line):
        """Extract timestamp from a log line."""
        start_idx = line.find(self.
                              timestamp_prefix) + len(self.timestamp_prefix)
        timestamp_str = line[start_idx:start_idx + 8]
        try:
            return datetime.strptime(timestamp_str, self.time_format)
        except (ValueError, IndexError):
            self.logger.error(f'Invalid timestamp '
                              f'format in line: {line.strip()}')
            return None

    def log_analyzer(self):
        """Analyze the log file for heartbeat issues."""
        lines = self._read_lines()
        filtered_lines = [line for line in lines if self.key in
                          line and self.timestamp_prefix in line]

        if not filtered_lines:
            self.logger.warning(f'No lines found with the key {self.key}')
            return

        timestamps = [self._extract_timestamp(line) for line in
                      filtered_lines if self._extract_timestamp(line)]
        for i in range(len(timestamps) - 1):
            self._log_difference(timestamps[i], timestamps[i + 1])

    def _log_difference(self, time_a, time_b):
        """Log the difference between two timestamps."""
        time_diff = abs((time_b - time_a).total_seconds())
        if time_diff >= self.err_limit:
            self.logger.error(f'Heartbeat delay {time_diff}'
                              f' sec exceeds error.')
        elif self.warn_limit < time_diff < self.err_limit:
            self.logger.warning(f'Heartbeat delay {time_diff}'
                                f' sec exceeds warning.')


if __name__ == '__main__':
    analyzer = HBAnalyzer(
        log_file='hblog.txt',
        key='Key TSTFEED0300|7E3E|0400',
        timestamp_prefix='Timestamp ',
        warn_limit=31,
        err_limit=33,
    )
    analyzer.log_analyzer()
