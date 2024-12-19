#!python3

from __future__ import annotations

import argparse
import random

# region Food Selection

breads = [
    "Sesame Seed Bun",
    "Wholegrain Bun",
    "Rye Bun",
    "Flatbread",
    "Sliced White",
    "Croissant",
    "Jam Doughnut",
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
    "Reindeer Patty",
]

nonmeats = ["Tofu Burger", "Plant-Based 'Beef' Burger", "Nut Burger"]

cheeses = [
    "American/Processed Cheese",
    "Cheddar",
    "Red Leicester",
    "Blue Stilton",
    "Mozzarella",
    "Crumbled Feta",
    "Norwegian Brunost",
]

toppings = [
    "Smoked Bacon",
    "Tortilla Chips",
    "Crispy Onions",
    "Guacamole",
    "Jalapenos",
    "Black Olives",
]

sauces = [
    "Burger Sauce",
    '"Special" Sauce',
    "BBQ Sauce",
    "Mayonnaise",
    "Garlic Mayonnaise",
    "Creamy Dijon Mustard",
    "Tartare Sauce",
    "Sriracha Sauce",
]

leaves = ["Iceberg Lettuce", "Rocket", "Curly Kale", "Sliced Sprouts", "Cabbage"]

vegetables = [
    "Sliced Tomato",
    "Field Mushroom",
    "Sliced Cucumber",
    "Sliced Bell Pepper",
    "Sliced Courgette",
    "Sliced Onion",
    "Sliced Red Onion",
]

pickles = [
    "Pickled Gherkins",
    "Pickled Beetroots",
    "Pickled Celeriac",
    "Sweet-pickled Red Onion",
]

# endregion


def add[T](population: list[T]) -> T:
    """Return an increasingly unlikely option from the list."""
    return random.choices(
        population,
        k=1,
        weights=list(reversed(range(1, len(population) + 1))),
    )[0]


def test_add():
    str_list = ["one", "two", "three"]

    assert add(str_list) in str_list

    list_list = [str_list, str_list, str_list]

    assert add(list_list) in list_list


def random_burger(
    layers: int | None = None,
    vegetarian: bool = False,
    go_wild: bool = False,
) -> list[str]:
    patty = nonmeats if vegetarian else nonmeats + meats
    if not go_wild:
        ingredients = {
            1: [patty],
            2: [patty, breads],
            3: [breads, patty, breads],
            4: [breads, cheeses, patty, breads],
            5: [breads, vegetables, cheeses, patty, breads],
            6: [breads, leaves, vegetables, cheeses, patty, breads],
            7: [breads, leaves, sauces, vegetables, cheeses, patty, breads],
            8: [breads, toppings, sauces, vegetables, patty, cheeses, patty, breads],
            9: [
                breads,
                leaves,
                sauces,
                vegetables,
                patty,
                vegetables,
                cheeses,
                patty,
                breads,
            ],
            # Attempt a Big Mac
            13: [
                breads,
                meats,
                pickles,
                leaves,
                vegetables,
                sauces,
                breads,
                meats,
                cheeses,
                leaves,
                vegetables,
                sauces,
                breads,
            ],
        }[layers or 7]
    else:
        ingredients = []
        if layers is None:
            layers = random.randint(1, 25)
        for _ in range(layers):
            if vegetarian:
                ingredients.append(
                    add(
                        [
                            breads,
                            nonmeats,
                            cheeses,
                            toppings,
                            sauces,
                            leaves,
                            vegetables,
                        ],
                    ),
                )
            else:
                ingredients.append(
                    add(
                        [
                            breads,
                            meats,
                            nonmeats,
                            cheeses,
                            toppings,
                            sauces,
                            leaves,
                            vegetables,
                        ],
                    ),
                )

    return [add(_) for _ in ingredients]


def test_random_burger():
    assert random_burger(1)[0] in meats + nonmeats
    assert random_burger(1, vegetarian=True)[0] in nonmeats
    assert len(random_burger(go_wild=True)) in range(1, 26)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make some random burgers")
    parser.add_argument(
        "--layers",
        metavar="N",
        type=int,
        help="How many Layers should the burger consist of?",
    )
    parser.add_argument(
        "--vegetarian", action="store_true", help="Only use non-meat patties"
    )
    parser.add_argument("--gowild", action="store_true", help="Random number of Layers")

    args = parser.parse_args()

    random.seed()
    print("\n".join(random_burger(args.layers, args.vegetarian, args.gowild)))
