# Write your solution here

def search_by_name(filename: str, word: str):
    recipes = create_recipe_list(filename)
    return_list = []
    for recipe in recipes:
        if word.lower() in recipe[0].lower():
            return_list.append(recipe[0])
    return return_list

def search_by_time(filename: str, prep_time: int):
    recipes = create_recipe_list(filename)
    return_list = []
    for recipe in recipes:
        if int(recipe[1]) <= prep_time:
            return_list.append(recipe[0] + ', preparation time ' + recipe[1] + ' min')
    return return_list

def search_by_ingredient(filename: str, ingredient: str):
    recipes = create_recipe_list(filename)
    return_list = []
    for recipe in recipes:
        if ingredient in recipe[2:]:
            return_list.append(recipe[0] + ', preparation time ' + recipe[1] + ' min')
    return return_list

def create_recipe_list(recipe_file:str):
    recipes = []

    with open(recipe_file) as new_file:
        recipe = []
        for line in new_file:
            clean_line = line.strip()
            if clean_line != '':
                recipe.append(clean_line)
            else:
                recipes.append(recipe)
                recipe = []
        recipes.append(recipe)
        
    return recipes


#if __name__ == "__main__":
#print(search_by_name('recipes1.txt','cake'))
#print(search_by_time('recipes1.txt',20))
#print(search_by_ingredient('recipes1.txt','eggs'))