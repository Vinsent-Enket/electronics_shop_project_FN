"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item





def test_calculate_total_price():

    item1 = Item("Смартфон", 10000, 20)
    # устанавливаем новый уровень цен
    # применяем скидку
    item1.apply_discount()
    assert item1.calculate_total_price() == 200000
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0