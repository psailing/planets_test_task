import pytest

from helper import helper_data


def test_all_planets_count(get_planets_count, get_all_planets_default):
    assert get_planets_count == helper_data.planet_count, "Incorrect planets count"


def test_all_planets_count_field(get_all_planets_default):
    assert get_all_planets_default.json()['count'] == helper_data.planet_count, "Incorrect planets count"


@pytest.mark.parametrize('first_last, next_page, prev_page', [
    (1, helper_data.page_link + str(helper_data.first_page + 1), None),
    (6, None, helper_data.page_link + str(helper_data.last_page - 1))], ids=['First page', "Last page"])
def test_next_prev_pages(get_next_prev_pages, first_last, next_page, prev_page):
    assert get_next_prev_pages[first_last] == [next_page, prev_page], "Incorrect planets count"
