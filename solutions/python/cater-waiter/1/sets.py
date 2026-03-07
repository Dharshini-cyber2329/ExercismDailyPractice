"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    ingredients = set(dish_ingredients)
    return (dish_name, ingredients)


def check_drinks(drink_name, drink_ingredients):
    if set(drink_ingredients) & ALCOHOLS:
        return drink_name + " Cocktail"
    else:
        return drink_name + " Mocktail"


def categorize_dish(dish_name, dish_ingredients):

    if dish_ingredients <= VEGAN:
        category = "VEGAN"
    elif dish_ingredients <= VEGETARIAN:
        category = "VEGETARIAN"
    elif dish_ingredients <= PALEO:
        category = "PALEO"
    elif dish_ingredients <= KETO:
        category = "KETO"
    else:
        category = "OMNIVORE"

    return f"{dish_name}: {category}"


def tag_special_ingredients(dish):
    name, ingredients = dish
    special = set(ingredients) & SPECIAL_INGREDIENTS
    return (name, special)


def compile_ingredients(dishes):
    master = set()
    for dish in dishes:
        master |= dish
    return master


def separate_appetizers(dishes, appetizers):
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    all_ing = set()

    for dish in dishes:
        all_ing |= dish

    return all_ing - intersection