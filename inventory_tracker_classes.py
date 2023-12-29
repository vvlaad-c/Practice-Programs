# Inventory tracker used to maintain an inventory using classes

# Creating the product class
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def show_name(self):
        return self.name
    
    def show_price(self):
        return self.price

# Creating the inventory class
class Inventory:

    def __init__(self, inventory):
        self.inventory = inventory
    
    def add_item(self, product):
        if product in self.inventory:
            self.inventory[product] += 1
        else:
            self.inventory[product] = 1
    
    def remove_item(self, product_name):
        found = False
        for product in self.inventory:
            name = product.show_name()
            if name == product_name:
                del self.inventory[product]
                found = True
                break
        
        if not found:
            raise Exception("The product you are trying to remove does not exist in inventory")
    
    def display_items(self):
        details = {}
        for product, quantity in self.inventory.items():
            name = product.show_name()  # Retrieve the product name using show_name()
            if name in details:
                details[name] += quantity
            else:
                details[name] = quantity
        
        for product_name, total_quantity in details.items():
            print(f"Product name: {product_name}")
            print(f"Quantity: {total_quantity}")
            