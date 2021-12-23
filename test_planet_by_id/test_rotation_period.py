import pytest

from helper import helper_data
from test_planet_by_id import helper


@pytest.mark.parametrize('planet_id', [x for x in range(1, helper_data.planet_count + 1)],
                         ids=[x for x in range(1, helper_data.planet_count + 1)])
def test_first_ten_planet_names(get_all_planets, planet_id):
    planet_info = helper.get_planets(planet_id)
    assert helper.get_rotation_period(planet_info) == get_all_planets['rotation_period'].values[planet_id - 1], \
        "Incorrect rotation period"
