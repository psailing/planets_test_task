import pytest
import requests


def get_schema():
    response = requests.get('https://swapi.dev/api/planets/schema/')
    return response


@pytest.mark.xfail(reason="Broken link")
def test_schema():
    assert get_schema().status_code == 200, "Broken link"
