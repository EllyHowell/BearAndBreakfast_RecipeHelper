from recipe import Recipe
import json

def find_recipes_with_ingredients(recipes:[Recipe], available_ingredients, level):
    """Searches the given recipes and returns recipes which are viable with the given ingredients and level

    Args:
        recipes ([Recipe]): List of the class 'Recipe' (contains 'name', 'ingredients' and 'level')
        available_ingredients ({}): List of ingredients which the user currently has (read from 'user_data.json')
        level (int): Users current level, this will be checked against the recipes

    Returns:
        [Recipe]: List of recipes which the user can create with the given ingredients
    """
    matching_recipes = []
    for recipe in recipes:
        ingredients = recipe.ingredients
        if all(ingredient in available_ingredients and
               available_ingredients[ingredient] >= amount and
               recipe.level <= level for ingredient, amount in ingredients.items()):
            # Remove ingredients from list to ensure all that is returned is able to create 
            
            matching_recipes.append(recipe.name)
    return matching_recipes


def get_recipes_from_json():
    """Reads the recipes from the 'recipes.json' file 

    Returns:
        [Recipe]: List of Recipe instances
    """
    recipes = []
    try:
        with open('recipes.json', 'r') as f:
            recipes_json = json.load(f)

        for recipe in recipes_json:
            recipes.append(Recipe(recipe['name'], recipe['ingredients'], recipe['level']))
            
    except Exception:
        print("> Error when reading the 'recipes.json' file, please ensure this file is populated (recipes in repository should be up-to-date)")
        
    return recipes  

def get_user_data():
    """Reads the users current level and available ingredients from the 'user_data.json'

    Returns:
        {}, int: Dictionary of ingredients (name and amount) and current level of the user
    """
    ingredients, level = None, None
    
    try:
        with open('user_data.json', 'r') as f:
            user_data = json.load(f)
            
        if ('ingredients' in user_data and 'level' in user_data):
            ingredients, level = user_data['ingredients'], user_data['level'] 
        else:    
            print(f"> User data found in 'user_data.json' did not contain the attributes 'ingredients' and/or 'level'")
            
    except Exception:
        print(f"> Error when reading the 'user_data.json' file, please ensure this file is populated and formatted correctly")    
        
    return ingredients, level   
    
def main():
    recipes = get_recipes_from_json()
    current_ingredients, user_level = get_user_data()
    
    if len(recipes) > 0 and current_ingredients is not None and user_level is not None:
        matching_recipes = find_recipes_with_ingredients(recipes, current_ingredients, user_level)

        if matching_recipes:
            print("You can make the following recipes:")
            for recipe in matching_recipes:
                print("- " + recipe)
        else:
            print("> You don't have enough ingredients to make any recipe.") 

if __name__ == "__main__":
    main()
