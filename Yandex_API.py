import unittest
import requests

# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой

# Токен ЯНДЕКС-диска
TOKEN = ''


# ___________________

# Создание папки
def create_folder(folder_name, token=TOKEN):
    url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
    headers = {
        'Authorization': TOKEN,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # Создание папки
    request = requests.put(url, headers=headers, params={'path': f'{folder_name}'})
    return request.status_code


# Проверка наличия папки
def check_folder(folder_name, token=TOKEN):
    url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
    headers = {
        'Authorization': TOKEN,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # Проверка наличия папки
    request = requests.get(url, headers=headers, params={'path': f'{folder_name}'})
    return request.status_code

# ___________________

class TestYandexAPI(unittest.TestCase):

    folder_name = '123'

    def test_create_new_folder(self):
        expected = create_folder(self.folder_name)
        result = 201
        self.assertEqual(expected, result)
        print(f'Папка {self.folder_name} создана.')

    def test_folder_exists(self):
        expected = check_folder(self.folder_name)
        result = 200
        self.assertEqual(expected, result)
        print(f'Папка {self.folder_name} уже есть.')

    def test_folder_does_not_exist(self):
        expected = check_folder(self.folder_name[:len(self.folder_name) - 1])
        result = 404
        self.assertEqual(expected, result)
        print(f'Папка {self.folder_name[:len(self.folder_name)-1]} отсутствует.')


if __name__ == '__main__':
    unittest.main()
