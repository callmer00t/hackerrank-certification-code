#!/bin/python3

import math
import os
import random
import re
import sys

class VendingMachine:
    def __init__(self, num_items, item_price):
        """Initialize the vending machine with the given number of items and item price."""
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        """Process a buy request and return change if successful, or raise an exception."""
        total_cost = req_items * self.item_price
        
        if req_items > self.num_items:
            raise ValueError("Not enough items in the machine")
        if money < total_cost:
            raise ValueError("Not enough coins")
        
        # Deduct items and return the change
        self.num_items -= req_items
        return money - total_cost

if __name__ == '__main__':
    # Sample usage
    vending_machine = VendingMachine(10, 2)  # 10 items, each costs 2 coins
    print(vending_machine.buy(3, 10))  # Buying 3 items with 10 coins, should return 4
