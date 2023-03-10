import pytest

from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


# test method init
def test_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


# test method calculate_total_price
def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


# test method apply_discount
def test_apply_discount(item1):
    assert item1.apply_discount() == None
