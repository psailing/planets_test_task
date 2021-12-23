import pytest
import requests

from helper import helper_data


@pytest.fixture(scope='module')
def get_all_planets_default():
    response = requests.get(helper_data.default_link)
    return response


@pytest.fixture()
def get_all_pages_status():
    status_code = {}
    i = 1
    while True:
        response = requests.get(helper_data.page_link + f'{i}')
        status_code[i] = response.status_code
        i += 1
        if response.json()['next'] is None:
            break
    return status_code


@pytest.fixture()
def get_invalid_pages_status(get_all_pages_status):
    status_code = {}
    min_page = min(get_all_pages_status.keys()) - 1
    max_page = max(get_all_pages_status.keys()) + 1
    for i in [min_page, max_page]:
        response = requests.get(helper_data.page_link + f'{i}')
        status_code[i] = response.status_code
    return status_code


@pytest.fixture()
def get_next_prev_pages(get_all_pages_status):
    next_prev = {}
    first_page = min(get_all_pages_status.keys())
    last_page = max(get_all_pages_status.keys())
    for i in [first_page, last_page]:
        response = requests.get(helper_data.page_link + f'{i}')
        next_prev[i] = [response.json()['next'], response.json()['previous']]
    return next_prev
