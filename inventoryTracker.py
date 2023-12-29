import pyinputplus as pyip
from inventory_tracker_classes import Product
from inventory_tracker_classes import Inventory

# Product class init --> name, price
# Inventory class init --> inventory dictionary

inventory_data = {}
inventory = Inventory(inventory_data)

# Interacting with the user, manipulating the inventory
user_options = [
    "add product", "remove product", "show name", "show price", "display_items"
    ]

def add_a_product():
    # Getting the values
    product_name = pyip.inputStr(prompt="Please enter the name of the product: ")
    price = pyip.inputNum(prompt="Please enter the price of the product: ")

    # Creating a Product instance
    new_product = Product(product_name, price)

    # Adding the product to the inventory
    inventory.add_item(new_product)
    print("Item successfully added to inventory!")
    print()

    # Using the product methods
    new_product.show_name()
    new_product.show_price()

def remove_a_product():
    product_name = pyip.inputStr(
        prompt="Please enter the name of the product you wish to remove"
    )

    inventory.remove_item(product_name)
    print("Item successfully removed from inventory!")
    print()
    

while True:
    print("Please enter a valid option:")
    for index, option in enumerate(user_options, start=1):
        print(f"{index}. {option}")
    
    user_decision = pyip.inputNum(min=1, max=5)
