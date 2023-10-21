"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.my_exeption import InstantiateCSVError


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)

def test___repr__(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test___str__(item1):
    assert str(item1) == 'Смартфон'

def test_apply_discount(item1):
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0

def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000

def test_apply_discount(item1):
    item1.pay_rate = 2
    item1.apply_discount()
    assert item1.price == 20000

def test_name(item1):
    assert item1.name == "Смартфон"
    item1.name = "1234567890смарт"
    assert item1.name == "1234567890"

def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')  # создание объектов из данных файла
    print(Item.all)
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../src/items2.csv')
    assert Item.instantiate_from_csv('../src/items3.csv') == None

def test_string_to_number():
    assert Item.string_to_number('228') == 228

