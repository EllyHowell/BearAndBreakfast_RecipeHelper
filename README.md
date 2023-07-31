# Welcome to the Bear and Breakfast Recipe Helper!

Are you tired of knowing what recipes to make in Bear and breakfast? What food to cook to make the most of your inventory? Then look no further!

# HOW

Run the program from the `main.py` file found in the repository

- `recipes.json` - This file is up-to-date with all of the bear and breakfast recipes, including: name, level, score and needed ingredients (_including fuel_)
- `user_data.json` - This is the **ONLY** file you will need to update, currently it contains example data. You will need to insert all of the raw ingredients into this file as well as your current food cooking level\*\*\*

\*\*\* Future work includes extracting current inventory rather than manually inputting data manually

## WHAT IS YOUR COOKING LEVEL?

| Level # | Unlock Information                                                |
| ------- | ----------------------------------------------------------------- |
| Level 1 | Available after completing `Farm to Fork (3)` in Highlake         |
| Level 2 | Gain Main Quest `Rat Tat To It` in Whitestone Bay                 |
| Level 3 | Available after completing Main Quest `Bear Fruit` in Winterberry |
| Level 4 | Available after completing `The First Cabin` in Pinefall          |

## OUTPUT

Below shows an example of what the output will look like, please keep in mind that recipes are sorted by food score (highest to lowest):

    You can make the following recipes:
    - Hash Browns x 6
    - Tomato Soup x 2
    - Grilled Cheese x 5
    - Mushroom Soup x 2
    - Corn Flakes x 33
    - Peach Iced Tea x 8
    - Chamomile Tea x 10
    - Apple Bowl x 1

### FOOD SCORE?

> Keep in mind, that the higher the quality of food, the higher Food
> score you will receive. Some Guests will have the "Foodie" request,
> meaning they want a room with a high food score. You will need to
> accommodate them.

For more information, see: [IGN COOKING RECIPES](https://www.ign.com/wikis/bear-and-breakfast/Cooking_Recipes)
