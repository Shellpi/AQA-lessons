"""Hometask 19_1."""

import json
import os

import requests

"""
Є вiдкритий API NASA який дозволяє за певними параметрами
отримати данi у виглядi JSON про фото зробленi ровером
“Curiosity” на Марсi. Серед цих даних є посилання на фото якi
потрiбно розпарсити i потiм за допомогою додаткових запитiв
скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg ,
mars_photo2.jpg . Завдання потрiбно зробити використовуючи
модуль requests
"""

TASK_START_TEMPLATE = '\n---Task {0}---\n'
print(TASK_START_TEMPLATE.format('01'))


def download_json(link, specs, output_file='Mars.json'):
    """Download photos from URL with params."""
    try:
        # Link preparations
        url_enh = link.strip('<>')

        # Response code
        response = requests.get(url_enh, params=specs, timeout=10)
        response.raise_for_status()

        # Saving JSON
        with open(output_file, 'wb') as file:
            file.write(response.content)
        print(f'Json is saved to {output_file}')

    except requests.exceptions.Timeout:
        print('Request timed out.')
    except requests.exceptions.RequestException as err:
        print(f'An error occurred: {err}')
    except Exception as err:
        print(f'An error occurred: {err}')


def parse_and_download_photos(json_path, download_dir='Mars_photos'):
    """Parse JSON and download photos from 'img_scr'."""
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)

        photos = data.get('photos', [])
        if not photos:
            print('No photos found')
            return

        os.makedirs(download_dir, exist_ok=True)
        print(f'Saving photos to: {download_dir}')

        for index, photo in enumerate(photos, start=1):
            img_src = photo.get('img_src')
            if img_src:
                try:
                    print(f'Downloading photo {index}: {img_src}')
                    img_response = requests.get(img_src, timeout=10)
                    img_response.raise_for_status()

                    img_name = os.path.join(download_dir,
                                            f'mars_photo{index}.jpg')
                    with open(img_name, 'wb') as img_file:
                        img_file.write(img_response.content)
                    print(f'Photo {index} saved to {img_name}')
                except requests.exceptions.RequestException as err:
                    print(f'Failed to download photo {index}: {err}')
            else:
                print(f'Photo {index} does not have a valid "img_src".')
    except FileNotFoundError:
        print(f'JSON file {json_path} not found.')
    except json.JSONDecodeError as err:
        print(f'Error decoding JSON: {err}')
    except Exception as err:
        print(f'Unexpected error during photo processing: {err}')


def json_remover(file_path):
    """Delete JSON file if it exists."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f'JSON file {file_path} successfully removed.')
        else:
            print(f'JSON file {file_path} not found. Skipping removal.')
    except Exception as err:
        print(f'Error during JSON removal: {err}')


def process_mars_photos(url, params, json_file='mars_photos.json',
                        download_dir='Mars_photos'):
    """Coordinate the downloading of JSON data and photos."""
    try:
        print('The photo saving process has been started...')
        # JSON download
        download_json(url, params, json_file)

        # JSON parse and photo download
        parse_and_download_photos(json_file, download_dir)

        # JSON remover
        json_remover(json_file)

        print('Mars photos saved successfully!')

    except Exception as err:
        print(f'An error occurred during processing: {err}')


if __name__ == '__main__':
    url = '<https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos>'
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

    process_mars_photos(url, params)
