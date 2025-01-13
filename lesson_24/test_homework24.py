"""Homework 24."""

import pytest
import requests

from conftest import base_url

"""
Є Flask app яке дозволяє робити аутентифiкацию
i пiсля цього шукати автомобiлi через
GET запрос. Потрiбно через Pytest органiзувати тестування даного
app використовуючи параметризацiю ( 5-7 наборiв даних ) з рiзними
параметрами GET запиту **sort_by** i **limit**. Тест повинен
використовувати модуль **request**. Первинна аутентифiкация
повинна бути органiзована у виглядi фiкстури **scope=’class’**.
Сам тест повинен вмiти робити логування не тiльки в
консоль але i в файл **test_search.log**
"""


class TestCarSearch:
    """Search with parameters."""

    @staticmethod
    def gen_test_params():
        """Generate test parameters dynamically."""
        return [
            ('brand', 4, ['Acura', 'Audi', 'BMW', 'Bugatti']),
            ('year', 3, ['Ford', 'Honda', 'Toyota']),
            ('engine_volume', 6, ['Tesla', 'Nissan', 'Honda',
                                  'Hyundai', 'Audi', 'Chevrolet']),
            ('price', 5, ['Chevrolet', 'Hyundai', 'Honda', 'Kia', 'Ford']),
            (None, 5, ['Acura', 'Audi', 'BMW', 'Bugatti', 'Chevrolet']),
            (None, None, ['Acura', 'Audi', 'BMW', 'Bugatti', 'Chevrolet',
                          'Ferrari', 'Ford', 'Honda',
                          'Hyundai', 'Infiniti', 'Jeep',
                          'Kia', 'Lamborghini',
                          'Land Rover', 'Lexus', 'Mazda',
                          'McLaren', 'Mercedes',
                          'Nissan', 'Porsche', 'Subaru',
                          'Tesla', 'Toyota',
                          'Volkswagen', 'Volvo']),
            ('brand', None, ['Acura', 'Audi', 'BMW', 'Bugatti',
                             'Chevrolet', 'Ferrari',
                             'Ford', 'Honda',
                             'Hyundai', 'Infiniti',
                             'Jeep', 'Kia', 'Lamborghini',
                             'Land Rover', 'Lexus',
                             'Mazda', 'McLaren', 'Mercedes',
                             'Nissan', 'Porsche',
                             'Subaru', 'Tesla', 'Toyota',
                             'Volkswagen', 'Volvo']),
        ]

    @pytest.mark.parametrize('sort_by, limit, expected_brands', gen_test_params())
    def test_search_cars(self, auth_process, test_logger, sort_by, limit, expected_brands):
        """The search test."""
        self.logger = test_logger
        params = {k: v for k, v in [('sort_by', sort_by), ('limit', limit)] if v is not None}

        # Send the request and get the response
        cars = self._send_request(auth_process, f'{base_url}/cars', params)

        # Validate the response
        self._validate_response(sort_by, limit, expected_brands, cars)

    def _send_request(self, auth_session, endpoint, params):
        """Send GET request and handle errors."""
        try:
            response = auth_session.get(endpoint, params=params, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            self.logger.error(f'Request failed: {err}')
            pytest.fail(f'Request failed: {err}')

    def _validate_response(self, sort_by, limit, expected_brands, actual_response):
        """Log and validate the API response."""
        actual_brands = [car['brand'] for car in actual_response]

        self.logger.info(f'Response for sort_by={sort_by}, limit={limit}: {actual_brands}')
        self.logger.info(f'Expected brands: {expected_brands}')

        for brand in expected_brands:
            if brand not in actual_brands:
                self.logger.error(f'{brand} not found in the results')
                pytest.fail(f'{brand} not found in the results')
