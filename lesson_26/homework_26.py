"""Hometask 26."""

from importlib import import_module

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

"""
Написати на python selenium код який пройде по двох фреймах
на початковiй сторiнцi, ввійде в кожний фрейм, введе правильний
секретний текст, натисне кнопку “Перевiрити”, порівняє текст
дiалогового вiкна для підтвердження успішності верифікації
та закриє діалогове вікно.
"""


class SecretVerification:
    """Class for verifying secrets inside frames of a webpage."""

    def __init__(self, url, browser, success_message):
        """Initialize params."""
        self.url = url
        self.driver = self.driver_initialize(browser)
        self.success_message = success_message

    def driver_initialize(self, browser):
        """Initialize the webdriver based on the chosen browser."""
        try:
            # Dynamic browser module import
            webdriver_module = import_module(
                f'selenium.webdriver.{browser.lower()}.webdriver')
            driver_class = getattr(webdriver_module, 'WebDriver')
            return driver_class()
        except ModuleNotFoundError:
            raise ValueError(f'Unsupported browser: {browser}')
        except Exception as e:
            raise RuntimeError(
                f'Failed to initialize driver for {browser}: {e}')

    def frame_checker(self, frame_id, input_id, secret_text):
        """Perform operations in a specific frame."""
        self.driver.get(self.url)

        frame = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, frame_id))
        )
        self.driver.switch_to.frame(frame)

        # Text input
        input_field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, input_id))
        )
        input_field.send_keys(secret_text)

        # Button click
        button = self.driver.find_element(By.TAG_NAME, 'button')
        button.click()

        # Alert dialogue window check
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == self.success_message, f'Unexpected alert text: {alert.text}'
        alert.accept()

    def run(self):
        """Execute frame verification for all frames."""
        try:
            self.frame_checker('frame1', 'input1', 'Frame1_Secret')
            self.frame_checker('frame2', 'input2', 'Frame2_Secret')
        finally:
            self.driver.quit()


if __name__ == '__main__':
    url = 'http://localhost:8000/dz.html'
    browser = 'chrome'
    success_message = 'Верифікація пройшла успішно!'
    verifier = SecretVerification(url, browser, success_message)
    verifier.run()
