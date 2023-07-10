import pytest
from src.keyboard import Keyboard


@pytest.fixture
def test_1():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_language(test_1):
    assert test_1.language == 'EN'
