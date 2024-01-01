import pyinputplus as pyip


# Creating the Recipe class
class Recipe:
    def __init__(self, recipes):
        self.recipes = recipes
    
    def add_recipe(self, name, preparation_time, recipe_data):
        self.recipes[name] = {
            "preparation_time": preparation_time,
            "recipe_data": recipe_data
        }
    
    def remove_recipe(self, recipe_name):
        if recipe_name in self.recipes:
            del self.recipes[recipe_name]
            print(f"Recipe '{recipe_name}' removed successfully.")
        else:
            print(f"No recipe named '{recipe_name}' found.")
    
    def create_recipe_category(self, category):
        if category not in self.recipes:
            self.recipes[category] = {}
        
        while True:
            print(f"Current recipes in category '{category}': {list(self.recipes[category].keys())}")
            choice = input("Do you want to add an existing recipe or a new recipe? (existing/new/exit): ")
            
            if choice == "existing":
                existing_recipe = input("Enter the name of the existing recipe: ")
                if existing_recipe in self.recipes:
                    self.recipes[category][existing_recipe] = self.recipes[existing_recipe]
                    print(f"Added existing recipe '{existing_recipe}' to category '{category}'")
                else:
                    print(f"No recipe named '{existing_recipe}' found.")
            
            elif choice == "new":
                new_recipe_name = input("Enter the name of the new recipe: ")
                preparation_time = int(input("Enter the preparation time: "))
                recipe_data = str(input("Enter the recipe data (instructions): "))
                
                self.recipes[category][new_recipe_name] = {
                    "preparation_time": preparation_time,
                    "recipe_data": recipe_data
                }
                print(f"Added new recipe '{new_recipe_name}' to category '{category}'")

            elif choice == "exit":
                break
            else:
                print("Invalid choice. Please enter 'existing', 'new', or 'exit'.")

    def display_recipes(self):
        for recipe_name, recipe_details in self.recipes.items():
            print(f"\tRecipe name: {recipe_name}")
            print(f"\tPreparation time: {recipe_details['preparation_time']} minutes")
            print("\tRecipe data:")
            for key, value in recipe_details['recipe_data'].items():
                print(f"\t\t{key.capitalize()}: {value}")
            print("\t-----------------------")
    
    def display_category(self, category):
        if category not in self.recipes:
            print(f"No category named '{category}' found.")
        else:
            print(f"Recipes in category '{category}':")
            recipes = self.recipes[category]
            if not recipes:
                print("No recipes in this category yet.")
            else:
                for recipe_name, recipe_details in recipes.items():
                    print(f"\tRecipe name: {recipe_name}")
                    print(f"\tPreparation time: {recipe_details['preparation_time']} minutes")
                    print("\tRecipe data:")
                    for key, value in recipe_details['recipe_data'].items():
                        print(f"\t\t{key.capitalize()}: {value}")
                    print("\t-----------------------")
