'''
File : bubbletea.py
Description : This is the main bubbletea module for the BubbleTea class(an abstract based class) 
              containing all the necessary imports andmethods that are going to be used throughout 
              the code in different files.
Author : Vraj Patel
Student ID : 110422159
UserName : patvn002
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractmethod
from toppings import Topping


class BubbleTea(ABC):
    def __init__(self, name, size, level_of_ice, level_of_sugar, type_of_tea):
        self.__name = name
        self.__size = size
        self.__level_of_ice = level_of_ice
        self.__level_of_sugar = level_of_sugar
        self.__fruits = {}
        self.__flavours = {}
        self.__toppings = {}
        self.__type_of_tea = type_of_tea

# these are the two defined abstract methods
    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_level_of_ice(self):
        return self.__level_of_ice

    def get_level_of_sugar(self):
        return self.__level_of_sugar

    def get_toppings(self):
        return self.__toppings

    def get_type_of_tea(self):
        return self.__type_of_tea

    def get_flavours(self):
        return self.__flavours

    def get_fruits(self):
        return self.__fruits

# the methods below to add and remove flavour, fruit and toppings to the teas
    def add_toppings(self, topping, topping_quantity):
        # checks if the topping exist in the topping dictionary
        if topping in self.toppings:
            # adds the quantity to the topping
            self.toppings[topping] = self.toppings[topping] + \
                topping_quantity
        else:
            self.toppings[topping] = topping_quantity

    def remove_toppings(self, topping, topping_quantity):
        # checks if the topping exist in the topping dictionary
        if topping in self.toppings:
            # if it exists then pops one quantity from the topping dictionary
            self.toppings[topping] = self.toppings[topping] - \
                topping_quantity
            if self.toppings[topping] <= 0:
                self.toppings.pop(topping)

    def add_flavour(self, flavour):
        self.flavours[flavour] = 1

    def remove_flavour(self, flavour):
        if flavour in self.flavours:
            self.flavours.pop(flavour)

    def add_fruit(self, fruit):
        self.fruits[fruit] = 1

    def remove_fruit(self, fruit):
        if fruit in self.fruits:
            self.fruits.pop(fruit)

    name = property(get_name)
    size = property(get_size)
    level_of_ice = property(get_level_of_ice)
    level_of_sugar = property(get_level_of_sugar)
    toppings = property(get_toppings)
    type_of_tea = property(get_type_of_tea)
    flavours = property(get_flavours)
    fruits = property(get_fruits)
