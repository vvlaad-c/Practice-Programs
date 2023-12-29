import pyinputplus as pyip
from inventory_tracker_classes import Product
from inventory_tracker_classes import Inventory

# Product class init --> name, price
# Inventory class init --> inventory dictionary

inventory_data = {}
inventory = Inventory(inventory_data)

# Interacting with the user, manipulating the inventory
user_options = [
    "add product", "remove product", "display items"
    ]

def add_a_product():
    # Getting the values
    product_name = pyip.inputStr(prompt="Please enter the name of the product: ")

    # Creating a Product instance
    new_product = Product(product_name, 0)

    # Adding the product to the inventory
    inventory.add_item(new_product)
    print("Item successfully added to inventory!")
    print()

    # Using the product methods
    new_product.show_name()


while True:
    print("Please enter a valid option:")
    for index, option in enumerate(user_options, start=1):
        print(f"{index}. {option}")
    
    user_decision = pyip.inputNum(min=1, max=4)

    if user_decision == 1:
        add_a_product()

    elif user_decision == 2:
        name = pyip.inputStr("Please enter the name of the product you wish to remove: ")
        inventory.remove_item(name)
        
        print("Item successfully removed from inventory!")
        print()

    elif user_decision == 3:
        inventory.display_items()
    
    elif user_decision == 4:
        break
    