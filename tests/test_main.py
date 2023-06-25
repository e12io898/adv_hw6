import pytest
from main import uniq_id, geo_log, max_sales, yad_api
from unittest import TestCase
import configparser

# Задача №1 unit-tests

@pytest.mark.parametrize(
    'ids, exepted', [
        ({'user1': [213, 213, 213, 15, 213],
          'user2': [54, 54, 119, 119, 119],
          'user3': [213, 98, 98, 35]},
         {98, 35, 15, 213, 54, 119})
    ]
)
def test_uniq_id(ids, exepted):
    res = uniq_id(ids)
    assert res == exepted


@pytest.mark.parametrize(
    'geo_logs, exepted', [
        ([{'visit1': ['Москва', 'Россия']},
          {'visit2': ['Дели', 'Индия']},
          {'visit3': ['Владимир', 'Россия']},
          {'visit4': ['Лиссабон', 'Португалия']},
          {'visit5': ['Париж', 'Франция']},
          {'visit6': ['Лиссабон', 'Португалия']},
          {'visit7': ['Тула', 'Россия']},
          {'visit8': ['Тула', 'Россия']},
          {'visit9': ['Курск', 'Россия']},
          {'visit10': ['Архангельск', 'Россия']}],
         ['visit1: Москва, Россия',
          'visit3: Владимир, Россия',
          'visit7: Тула, Россия',
          'visit8: Тула, Россия',
          'visit9: Курск, Россия',
          'visit10: Архангельск, Россия'])
    ]
)
def test_geo_log(geo_logs, exepted):
    res = geo_log(geo_logs)
    assert res == exepted


@pytest.mark.parametrize(
    'stats, exepted', [
        ({'facebook': 55, 'yandex': 120, 'vk': 115,
          'google': 99, 'email': 42, 'ok': 98}, 'yandex')
    ]
)
def test_max_sales(stats, exepted):
    res = max_sales(stats)
    assert res == exepted


# Задача №2 Автотест API Яндекса

config = configparser.ConfigParser()
config.read('token.ini')
yad_token = config['YaD']['token']

class Yad_test(TestCase):
    def test_yad_api_create_folder(self):
        self.assertEqual(yad_api('test', yad_token), 201, 'Папка создана')

    def test_yad_api_folder_already(self):
        self.assertEqual(yad_api('test', yad_token), 409, 'Папка уже создана')

    def test_yad_api_not_authorized(self):
        self.assertEqual(yad_api('test', '123456'), 401, 'Не авторизован')