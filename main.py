import requests
# Задача №1 unit-tests

## Задание 1 из ДЗ 'Коллекции данных'
def geo_log(geo_logs):
    result = []
    for logs in geo_logs:
        key, value = list(logs.keys())[0], list(logs.values())[0]
        if 'Россия' in value:
            destination = ', '.join(value)
            result.append(f'{key}: {destination}')
    return result


## Задание 2 из ДЗ 'Коллекции данных'
def uniq_id(ids):
    uniq_values = set([])
    for user in ids.values():
        for number in user:
            uniq_values.add(number)
    return uniq_values


## Задание 4 из ДЗ 'Коллекции данных'
def max_sales(stats):
    stats_r, money = {}, []
    for key, value in stats.items():
        money.append(value)
        stats_r.setdefault(value, key)
    return stats_r[max(money)]


# Задача №2 Автотест API Яндекса

def yad_api(path, yad_token):
    params = {'path': f'{path}'}
    yad_api_url = 'https://cloud-api.yandex.net/v1/disk/resources'
    yad_headers = {'Authorization': f'OAuth {yad_token}',
                   'Content-Type': 'application/json'}

    res = requests.put(url=yad_api_url,
                       headers=yad_headers,
                       params=params).status_code
    return res

# Данные для тестирования:
data = {
    'geo_log': [[{'visit1': ['Москва', 'Россия']},
                 {'visit2': ['Дели', 'Индия']},
                 {'visit3': ['Владимир', 'Россия']},
                 {'visit4': ['Лиссабон', 'Португалия']},
                 {'visit5': ['Париж', 'Франция']},
                 {'visit6': ['Лиссабон', 'Португалия']},
                 {'visit7': ['Тула', 'Россия']},
                 {'visit9': ['Курск', 'Россия']},
                 {'visit10': ['Архангельск', 'Россия']}],
                ['visit1: Москва, Россия',
                 'visit3: Владимир, Россия',
                 'visit7: Тула, Россия',
                 'visit8: Тула, Россия',
                 'visit9: Курск, Россия',
                 'visit10: Архангельск, Россия']
                ],
    'uniq_id': [{'user1': [213, 213, 213, 15, 213],
                 'user2': [54, 54, 119, 119, 119],
                 'user3': [213, 98, 98, 35]},
                {98, 35, 15, 213, 54, 119}],
    'max_sales': [{'facebook': 55, 'yandex': 120, 'vk': 115,
                   'google': 99, 'email': 42, 'ok': 98},
                  'yandex']}