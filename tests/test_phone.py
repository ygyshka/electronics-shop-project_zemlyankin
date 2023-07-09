import pytest
from src.phone import Phone


@pytest.fixture
def test_phone():
    return Phone('Apple', 50000, 6, 1)


@pytest.fixture
def test_phone1():
    return Phone('Sumsung', 30000, 10, 2)


def test___repr__(test_phone, test_phone1):
    assert test_phone.__repr__() == "Phone('Apple', 50000, 6, 1)"
    assert test_phone1.__repr__() == "Phone('Sumsung', 30000, 10, 2)"


def test___str__(test_phone, test_phone1):
    assert test_phone.__str__() == 'Apple'
    assert test_phone1.__str__() == 'Sumsung'


def test_number_of_sim(test_phone):
    assert test_phone.number_of_sim == 1


def test___add__(test_phone):
    assert test_phone + test_phone == 12
    assert test_phone + 5 == None
