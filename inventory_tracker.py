# Inventory tracker used to maintain an inventory using classes

# Creating the product class
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def show_name(self):
        print(f"Product name: {self.name}")
    
    def show_price(self):
        print(f"Product price: {self.price}")

# Creating the inventory class
class Inventory:

    def __init__(self, inventory):
        self.inventory = inventory
    
    def add_item(self, product):
        if product in self.inventory:
            self.inventory[product] += 1
        else:
            self.inventory[product] = 1
    
    def remove_item(self, product):
        if product in self.inventory:
            del self.inventory[product]
        else:
            raise Exception("The product you are trying to remove does not exist in inventory")
    
    def display_items(self):
        for key, value in self.inventory.items():
            print(f"Product: {key}")
            print(f"Quantity: {value}")