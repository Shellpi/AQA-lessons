"""Homework_19.2."""

import os

import requests

"""У venv Python встановiть Flask за допомогою команди pip install flask

Створiть у окремiй директорiї файл app.py та скопiюйте у нього
код файлу app.py який приведено нижче в початкових даних.

Запустiть http сервер за допомогою команди python app.py

Сервер стартує за базовою адресою http://127.0.0.1:8080

Враховуючи документацiю яку наведено нижче вам потрiбно написати
код який використовуючи модуль request зробить через POST upload
якогось зображення на сервер, за допомогою GET отримає посилання
на цей файл и потiм за допомогою DELETE зробить видалення файлу з сервера"""

"""
Метод: POST

Шлях: /upload

Опис: Завантажує зображення на сервер.

Параметри запиту:

image: файл зображення (тип MIME: image/*)
Відповідь:

Код стану 201 (Created) у разі успішного завантаження.
Повертає URL завантаженого зображення у форматі JSON
"""


def upload_image(host_url, image, timeout=10):
    """Upload image to the server."""
    if not os.path.exists(image):
        print(f"Error: File '{image}' not found.")
        exit(1)

    with open(image, 'rb') as image_file:
        files = {'image': image_file}
        response = requests.post(f'{host_url}/upload',
                                 files=files, timeout=timeout)
        response.raise_for_status()
        image_url = response.json().get('image_url')
        print(f'Image uploaded successfully: {image_url}')
        return image_url


"""
Метод: GET

Шлях: /image/<filename>

Опис: Повертає URL або саме зображення в залежності від заголовка
Content-Type. **<filename>** повинен бути вказаним
враховуючи правила кодування ULR

Відповідь:

Код стану 200 (OK)
Повертає URL завантаженого зображення у форматі JSON,
якщо Content-Type рівний text
Повертає саме зображення, якщо Content-Type рівний image.
"""


def get_image_url(host_url, filename, headers, timeout=10):
    """Get image URL or the image content."""
    url = f'{host_url}/image/{filename}'
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()

    if 'image' in response.headers.get('Content-Type', ''):
        print(f'Image retrieved successfully: {filename}')
        return response.content

    image_url = response.json().get('image_url')
    print(f'Image URL retrieved: {image_url}')
    return response.json()


"""
Метод: DELETE

Шлях: /delete/<filename>

Опис: Видаляє завантажене зображення з серверу. **<filename>**
повинен бути вказаним враховуючи правила кодування ULR

Відповідь:

Код стану 200 (OK) у разі успішного видалення.
Повертає повідомлення про успішне видалення у форматі JSON
"""


def delete_image(host_url, filename, timeout=10):
    """Delete the image from the server."""
    url = f'{host_url}/delete/{filename}'
    response = requests.delete(url, timeout=timeout)
    response.raise_for_status()
    message = response.json().get('message')
    print(f'Image deleted successfully: {message}')
    return response.json()


if __name__ == '__main__':
    base_url = 'http://127.0.0.1:8080'
    image_path = 'uploads/123.jpg'
    filename = '123.jpg'
    content_types = [{'Content-Type': 'text'}, {'Content-Type': 'image'}]
    timeout = 10

    try:
        print('Starting upload process...')
        uploaded_image_url = upload_image(base_url, image_path, timeout)
        print(f'\nUploaded image URL: {uploaded_image_url}')

        print('\nRetrieving image using GET method...')
        for headers in content_types:
            result = get_image_url(base_url, filename, headers, timeout)
            print(result)

        print('\nDeleting image...')
        delete_image(base_url, filename, timeout)

    except requests.exceptions.RequestException as err:
        print(f'Error : {err}')
