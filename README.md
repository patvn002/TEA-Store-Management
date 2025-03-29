# TEA-Store-Management

# Overview

This repository contains a Python-based Bubble Tea ordering system. It is structured using object-oriented principles, featuring an abstract base class and multiple subclasses for different tea types, alongside supporting modules for store management and topping details.

# File Descriptions

# Main Modules

bubbletea.py: An abstract base class defining common attributes and abstract methods for various types of bubble teas.

FruitTea.py: Subclass inheriting from BubbleTea for handling fruit tea orders, including specific price calculations.

Hottea.py: Subclass of BubbleTea designed for hot tea, featuring price calculation methods tailored for hot beverages.

Milktea.py: Subclass of BubbleTea focused on milk tea orders with specific price adjustments.

Frozentea.py: Handles frozen tea types, allowing options for milky or fruity variations, and adjusts pricing accordingly.

Sparklingtea.py: Manages sparkling tea orders, including fruits, flavors, and toppings, with a custom price calculation.

# Store and Utility Modules

store.py: Manages store operations, including tea ordering, maintaining order history, and calculating total earnings. Contains dictionaries for pricing of sizes, flavors, fruits, and toppings.

toppings.py: Simple module defining the Topping class to store details such as topping names and prices.

# Main Execution Module

main.py: Demonstrates instantiation of various tea objects, performing operations such as adding toppings and flavors, calculating prices, and managing orders through the Store class. Also prints store order history and earnings.

# Testing Module

test_bubbletea.py: Contains pytest-based test cases and fixtures for validating methods across tea classes, including adding and removing toppings, fruits, flavors, and testing price calculations and order processes.

# Features

Object-oriented design with clear abstraction and inheritance.

Comprehensive pricing system including base prices and additional costs for sizes, flavors, toppings, and special tea types.

Detailed order history management and earnings calculation in the Store class.

Extensive testing suite ensuring robustness and correctness of functionality.

# Usage

Run the main.py file to see a sample execution and interaction of the Bubble Tea ordering system.

Use pytest to run tests defined in test_bubbletea.py to ensure reliability and correctness of the implementations.

# Author

Vraj Patel (Username: patvn002)

This work complies with the University's Academic Misconduct Policy.

