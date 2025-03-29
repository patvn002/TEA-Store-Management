'''
File : test_bubbletea.py
Description : This is the test file containing all the tests for the methods made and used 
              previously in all the files, it contains all the necessary imports and has 
              five fixtures for all the five teas and also contains tests on five different methods.
Author : Vraj Patel
Student ID : 110422159
UserName : patvn002
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import pytest
from bubbletea import BubbleTea
from FruitTea import FruitTea
from toppings import Topping
from Hottea import HotTea
from Milktea import MilkTea
from Frozentea import FrozenTea
from Sparklingtea import SparklingTea
from store import Store

# made a TestTeas class for all the teas and testing them
# made five fixtures , for all the respective teas


class TestTeas:
    @pytest.fixture
    def fruittea_1(self):
        fruittea_1 = FruitTea("Guava Fruit Tea", "L",
                              "none", "normal", "Green")
        return fruittea_1

    @pytest.fixture
    def hottea1(self):
        hottea1 = HotTea("Premium Milk Chocolate",
                         "M", "no", "1spoon", "Matcha")
        return hottea1

    @pytest.fixture
    def milktea1(self):
        milktea = MilkTea("Taro Milk Tea", "S", "extra", "no", "Green")
        return milktea

    @pytest.fixture
    def sparktea1(self):
        sparktea1 = SparklingTea(
            "Roasted Sparkling Tea", "M", "normal", "normal", "Black")
        return sparktea1

    @pytest.fixture
    def frozentea1(self):
        frozentea1 = FrozenTea(
            "Roasted Sparkling Tea", "M", "normal", "normal", "Black", True, False)
        return frozentea1

# testing the add topping method
    def test_add_toppings(self, fruittea_1):
        fruittea_1.add_toppings("custard", 2)
        assert fruittea_1.toppings["custard"] == 2
        fruittea_1.add_toppings("custard", 1)
        assert fruittea_1.toppings["custard"] == 3

# testing the add flavour method
    def test_add_flavour(self, hottea1):
        hottea1.add_flavour("vanilla")
        assert "vanilla" in hottea1.flavours

# testing the add fruit method
    def test_add_fruit(self, sparktea1):
        sparktea1.add_fruit("mango")
        assert "mango" in sparktea1.fruits

# testing the remove topping method
    def test_remove_toppings(self, milktea1):
        milktea1.add_toppings("custard", 9)
        milktea1.remove_toppings("custard", 1)
        assert milktea1.toppings["custard"] == 8

# testing the remove flavour method
    def test_remove_flavour(self, frozentea1):
        frozentea1.add_flavour("mint_choc")
        frozentea1.remove_flavour("mint_choc")
        assert "mint_choc" not in frozentea1.flavours

# testing the remove fruit method
    def test_remove_fruit(self, sparktea1):
        sparktea1.add_fruit("strawberry")
        sparktea1.remove_fruit("strawberry")
        assert "strawberry" not in sparktea1.fruits

# testing the calculate price method
    def test_calculate_price(self, milktea1):
        store = Store()
        top_pricing = store._Store__all_prices
        assert milktea1.calculate_price(top_pricing) == 4.79

    def test_calculate_price(self, frozentea1):
        store = Store()
        top_pricing = store._Store__all_prices
        assert frozentea1.calculate_price(top_pricing) == 8.35

# testing the tea ordering method
    def test_tea_ordering(self, hottea1):
        store = Store()
        hottea1 = HotTea("Hot Chocolate tea", "S", "no", "no", "Green")
        hottea1.add_toppings("coconut_jelly", 2)
        hottea1.add_toppings("pearls", 1)
        store.tea_ordering(hottea1)
        top_pricing = store._Store__all_prices
        assert hottea1.calculate_price(top_pricing) == 6.94

# testing the calculate type price method
    def test_calculate_type_price(self, frozentea1):
        store = Store()
        top_pricing = store._Store__all_prices
        assert frozentea1.calculate_type_price(top_pricing) == 3.29

# testing the str method from sparkling tea
    def test__str(self, sparktea1):
        sparktea1.add_fruit("lemon")
        sparktea1.add_flavour("thai")
        sparktea1.add_toppings("jelly", 1)
        str_output = (
            f"Name = Roasted Sparkling Tea\n Size = M\n Ice = normal\n Sugar = normal\n Flavour = {{'thai': 1}}\n Fruit = {{'lemon': 1}}\n Topping = {{'jelly': 1}}\n Tea Type = Black\n"
        )
        assert str(sparktea1) == str_output
