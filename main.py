'''
File : main.py
Description : This is the main module for instantiating and checking 
              all the methods and classes, it has all the teas ,store and toppings imported 
              to it, this module has all the methods checked and instantiated to it 
              (eg: adding toppings, calculting price and also diplaying the store order history etc..).
Author : Vraj Patel
Student ID : 110422159
UserName : patvn002
This is my own work as defined by the University's Academic Misconduct Policy.
'''


from bubbletea import BubbleTea
from toppings import Topping
from FruitTea import FruitTea
from Hottea import HotTea
from Milktea import MilkTea
from Frozentea import FrozenTea
from Sparklingtea import SparklingTea
from store import Store


store = Store()

top_pricing = store._Store__all_prices

fruittea1 = FruitTea("Pearl Fruit Tea", "M",
                     "No Ice", "No Sugar", "Green")
fruittea1.add_toppings("pearls", 2)
fruittea1.add_flavour("thai")
fruittea1.add_fruit("peach")
store.tea_ordering(fruittea1)
print()

fruittea2 = FruitTea("Mousse Fruit Tea", "L",
                     "No Ice", "No Sugar", "Black")
fruittea2.add_flavour("hazelnut")
fruittea2.add_toppings("mousse", 5)
store.tea_ordering(fruittea2)
print()

milktea = MilkTea("Cookie Crumb Milk Tea", "S",
                  "normal", "2spoons", "Black")
milktea.add_flavour("oolong")
milktea.add_toppings("cookie_crumb", 10)
milktea.add_toppings("custard", 1)
milktea.remove_toppings("custard", 1)
store.tea_ordering(milktea)
print()

fruittea3 = FruitTea("Mango Fruit Tea", "L",
                     "normal", "2spoons", "Black")
fruittea3.add_toppings("pearls", 2)
fruittea3.add_fruit("passionfruit")
store.tea_ordering(fruittea3)
print()


hottea = HotTea("Hot Chocolate tea", "S", "no", "no", "Green")
hottea.add_toppings("coconut_jelly", 2)
hottea.add_toppings("pearls", 1)
store.tea_ordering(hottea)
print()

frozen_tea = FrozenTea("Frozen Tea", "L", "Normal",
                       "2 spoon sugar", "Green", True, True)
frozen_tea.add_toppings("mango_popping_pearls", 1)
frozen_tea.add_toppings("strawberry_popping_pearls", 3)
frozen_tea.add_fruit("peach")
store.tea_ordering(frozen_tea)
print()

sparktea = SparklingTea("Jasmine Sparkling Tea", "S", "No", "no", "Black")
sparktea.add_toppings("apple_popping_pearls", 3)
sparktea.add_flavour("thai")
store.tea_ordering(sparktea)
print()

hottea2 = HotTea("Assam Hot Tea", "M", "No", "2spoons", "Black")
hottea2.add_toppings("aloe_vera", 3)
hottea2.add_flavour("assam")
store.tea_ordering(hottea2)
print()

frozen_tea2 = FrozenTea("Assam Hot Tea", "M", "No",
                        "5spoons", "Green", True, True)
frozen_tea2.add_toppings("pearls", 3)
frozen_tea2.add_toppings("mixed_jellies", 4)
frozen_tea2.add_flavour("assam")
frozen_tea2.add_fruit("grape")
frozen_tea2.add_fruit("tropical")
store.tea_ordering(frozen_tea2)
print()

sparktea2 = SparklingTea("Jasmine Sparkling Tea", "M",
                         "No", "1spoons", "Black")
sparktea2.add_flavour("thai")
sparktea2.add_fruit("lemon")
sparktea2.add_fruit("guava")
store.tea_ordering(sparktea2)
print()

store.display_store_order_history()
