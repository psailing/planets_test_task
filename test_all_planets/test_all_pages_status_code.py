def test_status_default_page(get_all_planets_default):
    assert get_all_planets_default.status_code == 200, 'Incorrect status code for default page'


def test_page_status(get_all_pages_status):
    for i in get_all_pages_status:
        assert get_all_pages_status[i] == 200, f'Incorrect code for page{i}'


def test_incorrect_page_status(get_invalid_pages_status):
    for i in get_invalid_pages_status:
        assert get_invalid_pages_status[i] == 404, f'Incorrect code for page{i}'
