from datetime import datetime

import pytest

from nbu_privat_currency_sale import get_privat_currency_info, get_nbu_currency_info


@pytest.fixture
def date_1():
    """Return datetime object."""
    return datetime(2020, 4, 22)


def test_get_privat_currency_info(date_1):
    get_something = get_privat_currency_info(date_1)
    assert isinstance(get_something, list)
    assert type(get_something[0]) == dict
    assert list(get_something[0]) == ['bank', 'date', 'currency', 'rate']
    assert datetime.strptime(get_something[0]['date'], '%d.%m.%Y') == date_1
    assert get_something[0]['bank'] == 'PrivatBank'


def test_get_nbu_currency_info(date_1):
    get_something = get_nbu_currency_info(date_1)
    assert isinstance(get_something, list)
    assert type(get_something[0]) == dict
    assert list(get_something[0]) == ['bank', 'date', 'currency', 'rate']
    assert datetime.strptime(get_something[0]['date'], '%d.%m.%Y') == date_1
    assert get_something[0]['bank'] == 'National Bank of Ukraine'




