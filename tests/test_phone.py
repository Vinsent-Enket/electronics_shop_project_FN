import pytest

from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)

def test___repr__(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test___str__(phone1):
    assert str(phone1) == 'iPhone 14'

def test_apply_discount(phone1):
    phone1.pay_rate = 0.8
    phone1.apply_discount()
    assert phone1.price == 96000

def test_calculate_total_price(phone1):
    assert phone1.calculate_total_price() == 600_000

def test_apply_discount(phone1):
    phone1.pay_rate = 2
    phone1.apply_discount()
    assert phone1.price == 240000

def test_name(phone1):
    assert phone1.name == 'iPhone 14'
    phone1.name = "1234567890смарт"
    assert phone1.name == "1234567890"
