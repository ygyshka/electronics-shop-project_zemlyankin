import pytest
from src.keyboard import Keyboard


@pytest.fixture
def test_1():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_language(test_1):
    assert test_1.language == 'EN'


def test_change_lang(test_1):
    test_1.change_lang()
    assert test_1.language == "RU"
    test_1.change_lang()
    assert test_1.language == "EN"
