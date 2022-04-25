from datetime import datetime
import pathlib

import pytest

from nbu_privat_currency_sale import get_privat_currency_info, get_nbu_currency_info

HERE = pathlib.Path(__file__).resolve().parent


@pytest.fixture
def local_nbu_rates():
    """Use local JSON instead of request url."""
    return HERE / "privat_rates_22.04.2020.json"


@pytest.fixture
def date_1():
    """Return datetime object."""
    return datetime(2020, 4, 22)
start1 = datetime(2020, 4, 22)
start2= datetime(2020, 4, 23)
start3= datetime(2020, 4, 24)


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




