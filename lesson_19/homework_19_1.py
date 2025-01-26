"""Hometask 19_1."""

from pathlib import Path

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


def fetch_photos(link, specs, download_dir='Mars_photos'):
    """Fetch and download photos from API response."""
    try:
        link = link.strip('<>')
        response = requests.get(link, params=specs, timeout=10)
        response.raise_for_status()
        data = response.json()
        photos = data.get('photos', [])
        if not photos:
            print('No photos found.')
            return

        download_path = Path(download_dir)
        download_path.mkdir(exist_ok=True)
        print(f'Saving photos to: {download_path}')

        for index, photo in enumerate(photos, start=1):
            img_src = photo.get('img_src')
            if img_src:
                try:
                    with requests.get(img_src, timeout=10) as img_response:
                        img_response.raise_for_status()
                        img_name = download_path / f'mars_photo{index}.jpg'
                        img_name.write_bytes(img_response.content)
                        print(f'Photo {index} saved to {img_name}')
                except requests.exceptions.RequestException as err:
                    print(f'Failed to download photo {index}: {err}')
            else:
                print(f'Photo {index} does not have a valid "img_src".')
    except requests.RequestException as err:
        print(f'An error occurred: {err}')
    except Exception as err:
        print(f'Unexpected error: {err}')


if __name__ == '__main__':
    url = '<https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos>'
    params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}
    fetch_photos(url, params)
