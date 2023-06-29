"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

test_price_count1 = Item('POCO', 15000, 6)
test_price_count2 = Item('apple', 60000, 10)
test_price_count3 = Item('POCOll', 20000, 3)

test_apply1 = Item('lol', 8000, 5)
test_apply2 = Item('pec', 25000, 3)
test_apply3 = Item('rok', 40000, 2)


def test_calculate_total_price():
    assert test_price_count1.calculate_total_price() == 90000
    assert test_price_count2.calculate_total_price() == 600_000
    assert test_price_count3.calculate_total_price() == 60_000


def test_apply_discount():
    Item.pay_rate = 0.6
    test_apply1.apply_discount()
    assert test_apply1.price == float(4800)
    test_apply2.apply_discount()
    assert test_apply2.price == float(15000)
    test_apply3.apply_discount()
    assert test_apply3.price == float(24000)


def test_name():
    model = Item('Apple', 20000, 2)
    model.name = 'Samsung'
    assert model.name == 'Samsung'
    model.name = 'Samsung Full Flip'
    assert model.name == 'Samsung Fu'


def test_string_to_number():

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('7.0') == 7
    assert Item.string_to_number('53.5') == 53


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test___repr__():
    assert Item.__repr__(test_price_count1) == "Item('POCO', 15000, 6)"
    assert Item.__repr__(test_price_count2) == "Item('apple', 60000, 10)"
    assert Item.__repr__(test_price_count3) == "Item('POCOll', 20000, 3)"


def test___str__():
    assert Item.__str__(test_apply1) == "lol"
    assert Item.__str__(test_apply2) == "pec"
    assert Item.__str__(test_apply3) == "rok"
