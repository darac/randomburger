#!python3

import argparse
import random

breads = [
    "Sesame Seed Bun",
    "Wholegrain Bun",
    "Rye Bun",
    "Flatbread",
    "Sliced White",
    "Croissant",
    "Jam Doughnut"
]

meats = [
    "100% Beef Patty",
    "50/50 Beef/Pork Patty",
    "Chicken Breast",
    "Breaded Chicken Breast",
    "Lamb Patty",
    "Salmon Fillet",
    "Lamb and Mint Patty",
    "Pulled Pork",
    "Pulled Turkey",
    "Turducken",
    "Reindeer Patty"
]

nonmeats = [
    "Tofu Burger",
    "Plant-Based 'Beef' Burger",
    "Nut Burger"
]

cheeses = [
    "American/Processed Cheese",
    "Cheddar",
    "Red Leicester",
    "Blue Stilton",
    "Mozzarella",
    "Feta",
    "Norwegian Brunost"
]

toppings = [
    "Smoked Bacon",
    "Tortilla Chips",
    "Crispy Onions",
    "Gucamole",
    "Jalapenos",
    "Black Olives"
]

sauces = [
    "Burger Sauce",
    "BBQ Sauce",
    "Mayonnaise",
    "Garlic Mayonnaise",
    "Creamy Dijon Mustard",
    "Tartare Sauce",
    "Sriracha Sauce"
]

leaves = [
    "Iceberg Lettuce",
    "Rocket",
    "Curly Kale",
    "Sliced Sprouts",
    "Cabbage"
]

vegetables = [
    "Sliced Tomato",
    "Mushroom",
    "Sliced Cucumber",
    "Sliced Bell Pepper",
    "Sliced Courgette"
]


def add(population):
    return random.choices(population, k=1, weights=list(reversed(range(1, len(population) + 1))))[0]


def random_burger(layers=None, vegetarian=False, go_wild=False):
    if vegetarian:
        patty = meats
    else:
        patty = nonmeats
    if not go_wild and (layers is None or layers < 10):
        if layers is None:
            layers = 7
        ingredients = {
            1: [patty],
            2: [patty, breads],
            3: [breads, patty, breads],
            4: [breads, cheeses, patty, breads],
            5: [breads, vegetables, cheeses, patty, breads],
            6: [breads, leaves, vegetables, cheeses, patty, breads],
            7: [breads, leaves, sauces, vegetables, cheeses, patty, breads],
            8: [breads, toppings, sauces, vegetables, patty, cheeses, patty, breads],
            9: [breads, leaves, sauces, vegetables, patty, vegetables, cheeses, patty, breads]
        }[layers]
    else:
        ingredients = []
        if layers is None:
            layers = random.randint(1, 25)
        for i in range(layers):
            if vegetarian:
                ingredients.append(add([breads, nonmeats, cheeses, toppings, sauces, leaves, vegetables]))
            else:
                ingredients.append(add([breads, meats, nonmeats, cheeses, toppings, sauces, leaves, vegetables]))

    for i in ingredients:
        print(add(i))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Make some random burgers")
    parser.add_argument('--layers', metavar='N', type=int)
    parser.add_argument('--vegetarian', action='store_true')
    parser.add_argument('--gowild', action='store_true')

    args = parser.parse_args()

    random.seed()
    random_burger(args.layers, args.vegetarian, args.gowild)
