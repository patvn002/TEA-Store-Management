'''
File : store.py
Description : This is the store module containing the Store class which 
              contains the earning , the order history and the dictionary for all the prices 
              for size, flavour , fruits and also toppins. Moreover it contains methods for 
              ordering tea and displaying the store order history.
Author : Vraj Patel
Student ID : 110422159
UserName : patvn002
This is my own work as defined by the University's Academic Misconduct Policy.
'''


from bubbletea import BubbleTea
from FruitTea import FruitTea
from Hottea import HotTea
from Milktea import MilkTea
from Sparklingtea import SparklingTea
from Frozentea import FrozenTea
from toppings import Topping


class Store:
    def __init__(self):
        self.__store_earnings = 0
        self.__store_order_history = []
        self.__all_prices = {
            "tea_types": {"Fruity": 0.15, "Milky": 0.29, "Sparkling": 0.19, "Hot": 0.24, "Frozen": 3.0},
            "quantity_price": {"small": 0, "medium": 0.85, "large": 1.2},
            "fruits": {'mango': 0.3, 'lychee': 0.1, 'apple': 0.2, 'grape': 0.4, 'melon': 0.5, 'grapefruit': 0.1,
                       'lemon': 0.3, 'guava': 0.2, 'passionfruit': 0.25, 'strawberry': 0.2, 'pomegranate': 0.45,
                       'peach': 0.1, 'tropical': 0.65, 'watermelon': 0.35},
            "flavours": {'mint_choc': 0.3, 'thai': 0.35, 'salted_caramel': 0.2, 'roasted': 0.4, 'earl_grey': 0.5,
                         'vanilla': 0.1, 'assam': 0.3, 'hazelnut': 0.2, 'oolong': 0.25, 'jasmine': 0.2, 'matcha': 0.45,
                         'premium': 0.1, 'taro': 0.65, 'chocolate': 0.4},
            "toppings": {'custard': 1.0, 'mousse': 2.4, 'pearls': 1.2, 'cookie_crumb': 0.75, 'mixed_jellies': 0.35,
                         'herbal_jelly': 0.45, 'coconut_jelly': 0.5, 'aloe_vera': 0.7, 'mango_popping_pearls': 0.4,
                         'strawberry_popping_pearls': 0.4, 'apple_popping_pearls': 0.4}}

    def get_store_earnings(self):
        self.__store_earnings

    def get_store_order_history(self):
        self.__store_order_history

    # this method is used to order the teas
    def tea_ordering(self, tea):
        # the below code store the calculated tea price into a varibale
        tea_p = tea.calculate_price(self.__all_prices)
        # adding the calcullated tea price to the store earnings
        self.__store_earnings = self.__store_earnings + tea_p
        # also appending the tea price to the store order history
        self.__store_order_history.append((tea, tea_p))
        return tea_p

    def display_store_order_history(self):
        # looping over the store order history and displaying all the orders one by one
        for tea, price in self.__store_order_history:
            print("-----------------------")
            print("-----------------------")
            print(tea)
            print(f"Price: $, {price}")
        print(f"Total Earnings: $, {self.__store_earnings}")
        print("---------------------------")
        print("---------------------------")

    earnings = property(get_store_earnings)
    history = property(get_store_order_history)
