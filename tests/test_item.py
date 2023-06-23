"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


test_price_count1 = Item('POCO', 15000, 6)
test_price_count2 = Item('apple', 60000, 10)
test_price_count3 = Item('POCO', 20000, 3)

test_apply1 = Item('lol', 8000, 5)
test_apply2 = Item('pec', 25000, 3)
test_apply3 = Item('rok', 40000, 2)


def test_calculate_total_price():
    assert test_price_count1.calculate_total_price() == 90000
    assert test_price_count2.calculate_total_price() == 600_000
    assert test_price_count3.calculate_total_price() == 60_000
    pass


def test_apply_discount():
    Item.pay_rate = 0.6
    test_apply1.apply_discount()
    assert test_apply1.price == float(4800)
    test_apply2.apply_discount()
    assert test_apply2.price == float(15000)
    test_apply3.apply_discount()
    assert test_apply3.price == float(24000)
    pass
