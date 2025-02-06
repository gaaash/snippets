
'''
    Challenge #8
    From : https://www.w3resource.com/python-exercises/oop/index.php

'''

from os import remove


class Items:
    def __init__(self, inventory):
        self.inventory = inventory
        
class Shopingcart(Items):
    def __init__(self, inventory):
        super().__init__(inventory)
        self.cart = []
    def insert(self, value):
        if value in self.inventory:
            self.cart.append(value)
        else:
            print(f"Item {value} is not in the Inventory !!!")
    def remove(self, value):
        if value in self.cart:
            self.cart.remove(value)
        else:
            print(f"Item {value} is not in your shopping cart")
    def total(self):
        sum = 0
        for i in self.cart:
            sum += inventory[i]
        print(f'{sum}$')
    def display(self):
        for i in self.cart:
            print(i, end='\n')






inventory = { 
                'apple':120,
                'banana':32, 
                'orange':40,
                'pineapple':700,
                'sigar':400
            }

shop = Shopingcart(inventory)
shop.insert('apple')
shop.insert('sigar')
shop.insert('banana')
shop.insert('orange')

shop.remove('sigar')
shop.display()
shop.total()