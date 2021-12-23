import pytest

from helper import helper_data
from test_planet_by_id import helper


@pytest.mark.parametrize('planet_id', [x for x in range(1, helper_data.planet_count + 1)],
                         ids=[x for x in range(1, helper_data.planet_count + 1)])
def test_planet_statuses(planet_id):
    planet_info = helper.get_planets(planet_id)
    assert planet_info.status_code == 200, "Incorrect status code"


@pytest.mark.parametrize('planet_id', [0, helper_data.planet_count + 1],
                         ids=[0, helper_data.planet_count + 1])
def test_incorrect_ids_status(planet_id):
    planet_info = helper.get_planets(planet_id)
    assert planet_info.status_code == 404, "Out of planet range"
