'''
File : toppings.py
Description : This is the toppings python module storing the topping 
              name and price and its respective properties.
Author : Vraj Patel
Student ID : 110422159
UserName : patvn002
This is my own work as defined by the University's Academic Misconduct Policy.
'''


class Topping:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_topping_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    tname = property(get_topping_name)
    tprice = property(get_price)
