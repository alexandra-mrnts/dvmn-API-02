import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()
TOKEN = os.environ['TOKEN']
API_VERSION = '5.199'


def shorten_link(token, url):
    headers = {'Authorization': f'Bearer {token}'}
    params = {'v': API_VERSION, 'url': url}

    response = requests.get(
        'https://api.vk.ru/method/utils.getShortLink',
        headers=headers,
        params=params)
    response.raise_for_status()
    if 'error' in response.json():
        if response.json()['error']['error_code'] == 100:
            raise ValueError
        else:
            raise Exception

    short_link = response.json()['response']['short_url']
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
    if 'error' in response.json():
        if response.json()['error']['error_code'] == 100:
            raise ValueError
        else:
            raise Exception

    if len(response.json()['response']['stats']) > 0:
        clicks_count = response.json()['response']['stats'][0]['views']
    return clicks_count


def is_short_link(url):
    if urlparse(url).netloc == 'vk.cc':
        return True
    return False


def main():
    user_link = input('Введите ссылку: ')

    # If the user link is shortened show number of clicks
    if is_short_link(user_link):
        try:
            clicks_count = count_clicks(token=TOKEN,
                                        url=user_link)
            print('Количество переходов по ссылке за день:', clicks_count)
        except ValueError:
            print('Вы ввели неверную ссылку!')
        except Exception:
            print('Не удалось получить количество переходов по ссылке')
        finally:
            return

    # If the user link is not shortened return short link
    try:
        short_link = shorten_link(token=TOKEN, url=user_link)
        print('Сокращенная ссылка:', short_link)
    except ValueError:
        print('Вы ввели неверную ссылку!')
    except Exception:
        print('Не удалось получить короткую ссылку')
    finally:
        return


if __name__ == '__main__':
    main()
