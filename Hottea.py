'''
File : Hottea.py
Description : This is the Hottea module having the HotTea class 
              i.e. inheriting the BubbleTea class and overriding its abstract 
              methods and magic methods to calculate and view the HotTea price.
Author : Vraj Patel
Student ID : 110422159
UserName : patvn002
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from bubbletea import BubbleTea

# same logic for the calculate price expalined in FruitTea module
# HotTea does not have the add fruit method as it is not a Fruit Tea


class HotTea(BubbleTea):
    def __init__(self, name, size, level_of_ice, level_of_sugar, type_of_tea):
        super().__init__(name, size, level_of_ice, level_of_sugar, type_of_tea)

    def calculate_price(self, top_pricing):
        price_of_flavour = 0
        price_of_toppings = 0
        bprice = 4.5
        if self.size == "S":
            price = 0
        elif self.size == "M":
            price = 0.85
        else:
            price = 1.2

        for flavour in self.flavours:
            one_price = top_pricing["flavours"][flavour]
            price_of_flavour += one_price

        for t_name in self.toppings:
            t_quant = self.toppings[t_name]
            one_price = top_pricing["toppings"][t_name]
            total_price = t_quant * one_price
            price_of_toppings = price_of_toppings + total_price

        return bprice + 0.24 + price + price_of_flavour + price_of_toppings

    def __str__(self):
        return f"Name = {self.name}\n Size = {self.size}\n Ice = {self.level_of_ice}\n Sugar = {self.level_of_sugar}\n Flavour = {self.flavours}\n Topping = {self.toppings}\n Tea Type = {self.type_of_tea}\n"
