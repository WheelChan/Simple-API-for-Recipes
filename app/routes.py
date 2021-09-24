#routes
from .recipe import Recipes
from . import app
from flask import request

# 'get' route that returns all recipes
@app.get("/recipes")
def get_recipes():
    recipes = [recipe.get("name") for recipe in Recipes.load()]
    return {"Recipe Names": recipes}
        


# 'get' route that takes recipe name as input and returns information for that recipe
# information for recipe includes: 1). ingredients, 2). number of steps
# provide error message if recipe not in set
@app.get("/recipes/details/<name>")
def get_recipe_by_name(recipe_name):
    result = {}
    all_recipes = Recipes.load()
    if recipe_name not in [recipe.get("name") for recipe in all_recipes]:
        return {}
    else:
        ingredients, steps = Recipes.get_recipe_name(all_recipes, recipe_name)
        return {"details": {"Ingredients": ingredients, "num_steps": len(steps)}}

    
    
# 'post' route that adds recipes to dataset
# provide error message if recipe already exists in list
@app.post("/recipes")
def post_recipe():
    #retrieve new recipe information
    new_recipe = request.get_json()
    
    all_recipes = Recipes.load()
    if new_recipe.get("name") in [recipe.get("name") for recipe in all_recipes]:
        return {"error": "recipe already exists"}, 400
    else:
        all_recipes.append(new_recipe)
        Recipes.write(all_recipes)
        return ""


# 'put' route that updates recipes in dataset
# provide error message if recipe not in dataset
@app.put("/recipes")
def update_recipe():
    #retrieve new recipe information
    new_recipe_data = request.get_json()
    
    all_recipes = Recipes.load()
    if new_recipe.get("name") not in [recipe.get("name") for recipe in all_recipes]:
        return {"error": "recipe does not exist"}, 404
    else:
        Recipe.update(all_recipes, new_recipe_data)
        Recipes.write(all_recipes)
        return "", 204