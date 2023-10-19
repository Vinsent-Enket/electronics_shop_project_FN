import pytest

from src.keyboard import Keyboard


@pytest.fixture
def kboard1():
    return Keyboard('Dark Project KD87A', 9600, 5)

def test___repr__(kboard1):
    assert repr(kboard1) == "Keyboard('Dark Project KD87A', 9600, 5)"

def test___str__(kboard1):
    assert str(kboard1) == 'Dark Project KD87A'

def test_apply_discount(kboard1):
    Keyboard.pay_rate = 0.8
    kboard1.apply_discount()
    assert kboard1.price == 7680

def test_calculate_total_price(kboard1):
    assert kboard1.calculate_total_price() == 48000

def test_apply_discount(kboard1):
    kboard1.pay_rate = 2
    kboard1.apply_discount()
    assert kboard1.price == 19200

def test_name(kboard1):
    assert kboard1.name == "Dark Project KD87A"
    kboard1.name = "1234567890смарт"
    assert kboard1.name == "1234567890"

def test_chanch_lang(kboard1):
    kboard1.change_lang()
    assert kboard1.language == "RU"
