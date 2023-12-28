import math
import pyinputplus as pyip

# Making a calculator app using classes and modular programming

# Creating the calculator class which will perform the calculations
class Calculator:

    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num1 == 0 or num2 == 0:
            raise Exception("Cannot divide by 0")
        else:
            return num1 / num2
    
    def square_root(self, num1):
        return math.sqrt(num1)
    
    def power_of(self, num1, num2):
        return num1 ** num2

# Interacting with the user
print("--------------------")
print("Welcome to the calculator app!")
print()

# Performing the calculations
calc = Calculator()
choices = ["addition", "subtraction", "multiplication", "division", "square root", "power of"]
while True:
    print("These are the operations choices, please choose one:")
    for choice in choices:
        print(choice)
    
    user_choice = pyip.inputChoice(
        choices,
        prompt="Please enter a choice: "
    )

    if user_choice == "square root":
        num1 = pyip.inputNum(
        prompt="Please enter the number you wish to find the square root of: "
    )
        result = calc.square_root(num1)
        print(result)
        continue

    num1 = pyip.inputNum(
        prompt="Please enter the first number: "
    )
    num2 = pyip.inputNum(
        prompt="Please enter the second number: "
    )

    if user_choice.lower() == "addition":
        result = calc.add(num1, num2)
        print(result)
    
    elif user_choice.lower() == "subtraction":
        result = calc.subtract(num1, num2)
        print(result)
    
    elif user_choice.lower() == "multiplication":
        result = calc.multiply(num1, num2)
        print(result)
    
    elif user_choice.lower() == "division":
        result = calc.divide(num1, num2)
        print(result)

    elif user_choice.lower() == "power of":
        result = calc.power_of(num1, num2)
        print(result)