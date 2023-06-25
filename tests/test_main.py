import pytest
import configparser
from unittest import TestCase
from main import uniq_id, geo_log, max_sales, yad_api, data


# Задача №1:

test_data = (data['uniq_id'][0], data['uniq_id'][1])
@pytest.mark.parametrize('ids, exepted', [test_data])
def test_uniq_id(ids, exepted):
    res = uniq_id(ids)
    assert res == exepted

test_data = (data['geo_log'][0], data['geo_log'][1])
@pytest.mark.parametrize('geo_logs, exepted', [test_data])
def test_geo_log(geo_logs, exepted):
    res = geo_log(geo_logs)
    assert res == exepted

test_data = (data['max_sales'][0], data['max_sales'][1])
@pytest.mark.parametrize('stats, exepted', [test_data])
def test_max_sales(stats, exepted):
    res = max_sales(stats)
    assert res == exepted


# Задача №2:

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