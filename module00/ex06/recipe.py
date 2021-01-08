cookbook = {
  "sandwich": {
    "ingredients": ["ham", "bread", "cheese", "tomatoes"],
    "meal": "lunch",
    "prep_time": 10
  },
  "cake": {
    "ingredients": ["flour", "sugar", "sugar"],
    "meal": "dessert",
    "prep_time": 60
  },
  "salad": {
    "ingredients": ["avocado", "avocado", "tomatoes", "spinach"],
    "meal": "lunch",
    "prep_time": 15
  }
}

def add_recipe():
  name = input("name:")
  meal_type = input("meal type:")
  prep_time = input("preparation time:")
  ingredients = input("Ingredient separate by ',': ")
  new_recipe = {
    name: {
      "ingredients": ingredients.split(","),
      "meal": meal_type,
      "prep_time": prep_time
    }
  }
  cookbook.update(new_recipe)

def print_cookbook():
  print(cookbook)

def delete_recipe(receipe_name):
  try: 
    del cookbook[receipe_name]
    return True
  except ValueError:
    return False

def search_recipe(receipe_name):
  try: 
    print(cookbook[receipe_name])
    return True
  except ValueError:
    return False

quitting = False
while not quitting:
  number = input("Please select an option by typing the corresponding number:\n1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")
  if number == "1":
    add_recipe()
  elif number == "2":
    receipe_name = input("Please enter the recipe's name to delete it:\n")
    has_deleted = delete_recipe(receipe_name)
    if has_deleted == False:
      print("Err")
  elif number == "3":
    receipe_name = input("Please enter the recipe's name to get its details:\n")
    element_find = search_recipe(receipe_name)
    if element_find == False:
      print("err")
  elif number == "4":
    print_cookbook()
  elif number == "5":
    print("Cookbook closed.")
    quitting = True
  else:
    print("This option does not exist, please type the corresponding number.\nTo exit, enter 5.")