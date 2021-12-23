import pandas as pd
import pytest
import requests


@pytest.fixture(scope='session')
def get_all_planets():
    table = []
    i = 1
    while True:
        response = requests.get(f'https://swapi.dev/api/planets/?page={i}')
        table.append(pd.DataFrame(response.json()['results']))
        i += 1
        if response.json()['next'] is None:
            break
    table = pd.concat(table)
    return table


@pytest.fixture(scope='session')
def get_planets_count(get_all_planets):
    return len(get_all_planets.index)
