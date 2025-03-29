'''
File : Frozentea.py
Description : This is the inherited Frozentea module containing the FrozenTea 
              class having all the required methods and magic 
              method for calculating and viewing the frozentea price. 
Author : Vraj Patel
Student ID : 110422159
UserName : patvn002
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from bubbletea import BubbleTea


class FrozenTea(BubbleTea):
    def __init__(self, name, size, level_of_ice, level_of_sugar, type_of_tea, milky, fruity):
        super().__init__(name, size, level_of_ice, level_of_sugar, type_of_tea)
        self.__milky = milky
        self.__fruity = fruity

    def get_milky(self):
        return self.__milky

    def get_fruity(self):
        return self.__fruity

    milky = property(get_milky)
    fruity = property(get_fruity)

    # FrozenTea has a special method that is used increase the price based on, if the customer wants to have it milky , or fruity or both
    def calculate_type_price(self, top_pricing):
        main_price = 3
        # if the customer wants to make a frozen tea that is both milky and fruity
        if self.__milky and self.__fruity:
            main_price += top_pricing["tea_types"]["Milky"] + \
                top_pricing["tea_types"]["Fruity"]
        # if the customer only wants to have milky frozen tea
        elif self.__milky:
            main_price += top_pricing["tea_types"]["Milky"]
        # if the customer wants a fruity frozen tea
        elif self.__fruity:
            main_price += top_pricing["tea_types"]["Fruity"]

        return main_price

# the below methods stay same as before
    def calculate_price(self, top_pricing):
        price_of_flavour = 0
        price_of_fruit = 0
        price_of_toppings = 0
        bprice = 4.5
        if self.size == "S":
            price = 0
        elif self.size == "M":
            price = 0.85
        else:
            price = 1.2

        for fruit in self.fruits:
            one_price = top_pricing["fruits"][fruit]
            price_of_fruit += one_price

        for flavour in self.flavours:
            one_price = top_pricing["flavours"][flavour]
            price_of_flavour += one_price

        for t_name in self.toppings:
            t_quant = self.toppings[t_name]
            one_price = top_pricing["toppings"][t_name]
            total_price = t_quant * one_price
            price_of_toppings = price_of_toppings + total_price

        return bprice + 3 + price + price_of_flavour + price_of_fruit + price_of_toppings

    def __str__(self):
        return f"Name = {self.name}\n Size = {self.size}\n Ice = {self.level_of_ice}\n Sugar = {self.level_of_sugar}\n Flavour = {self.flavours}\n Fruit = {self.fruits}\n Topping = {self.toppings}\n Tea Type = {self.type_of_tea}\n"
