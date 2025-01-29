import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse


API_VERSION = '5.199'


def shorten_link(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    params = {'v': API_VERSION, 'url': url}

    response = requests.get(
        'https://api.vk.ru/method/utils.getShortLink',
        headers=headers,
        params=params)
    response.raise_for_status()
    response_body = response.json()
    if 'error' in response_body:
        if response_body['error']['error_code'] == 100:
            raise ValueError
        else:
            raise Exception

    short_link = response_body['response']['short_url']
    return short_link


def count_clicks(token, url):
    clicks_count = 0
    headers = {'Authorization': f'Bearer {token}'}
    key = urlparse(url).path[1:]
    params = {'v': API_VERSION, 'key': key, 'interval': 'day'}

    response = requests.get(
        'https://api.vk.ru/method/utils.getLinkStats',
        headers=headers,
        params=params)
    response.raise_for_status()
    response_body = response.json()
    if 'error' in response_body:
        if response_body['error']['error_code'] == 100:
            raise ValueError
        else:
            raise Exception

    if response_body['response']['stats']:
        clicks_count = response_body['response']['stats'][0]['views']
    return clicks_count


def is_short_link(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    key = urlparse(url).path[1:]
    params = {'v': API_VERSION, 'key': key}

    response = requests.get(
        'https://api.vk.ru/method/utils.getLinkStats',
        headers=headers,
        params=params)
    response.raise_for_status()
    return 'error' not in response.json()


def main():
    load_dotenv()
    token = os.environ['VK_TOKEN']
    user_link = input('Введите ссылку: ')

    if is_short_link(token=token, url=user_link):
        try:
            clicks_count = count_clicks(token=token,
                                        url=user_link)
            print('Количество переходов по ссылке за день:', clicks_count)
        except ValueError:
            print('Вы ввели неверную ссылку!')
    else:
        try:
            short_link = shorten_link(token=token, url=user_link)
            print('Сокращенная ссылка:', short_link)
        except ValueError:
            print('Вы ввели неверную ссылку!')


if __name__ == '__main__':
    main()
