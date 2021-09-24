import json
#API should be done with a data class so we created Recipe as data class

class Recipes:
    filename = "data.json"
    
    @classmethod
    def load(cls):
        #read data and loads data into list
        with open(cls.filename, "r") as recipe_files:
            return json.load(recipe_files).get("recipes", [])
        
    @classmethod
    def get_recipe_name(cls, all_recipes, recipe_name):
        #return recipe information
        recipe = list(filter(lambda rec: rec.get("name") == recipe_name, all_recipes))
        return recipe[0].get("ingredients"), recipe[0].get("instructions")
    
    @classmethod
    def write(cls, all_recipes):
        #rewrite recipe data in JSON file
        with open(cls.filename, "w") as recipe_files:
            json.dump({"recipes": all_recipes}, recipe_files)
    
    @classmethod
    def update(cls, all_recipes, new_recipe_data):
        recipe = list(filter(lambda rec: rec.get("name") == new_recipe_data.get("name"), all_recipes))
        for key, value in new_recipe_data:
            recipe[key] = value
        