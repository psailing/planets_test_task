import requests

from helper import helper_data


def get_planets(planet_id):
    response = requests.get(helper_data.default_link + f'{planet_id}')
    return response


def get_name(response_obj):
    return response_obj.json()['name']


def get_rotation_period(response_obj):
    return response_obj.json()['rotation_period']
