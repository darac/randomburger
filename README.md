# RandomBurger

Based on a stupid idea, prints out a list of "layers" to make a random burger.

Ingredients are printed top down, so a [Big Mac](https://en.wikipedia.org/wiki/Big_Mac)
would appear as:

```text
Sesame Seed Bun
100% Beef Patty
Pickled Gherkins
Iceberg Lettuce
Sliced Onions
"Special" Sauce
Sesame Seed Bun
100% Beef Patty
American/Processed Cheese
Iceberg Lettuce
Sliced Onions
"Special" Sauce
Sesame Seed Bun
```

Some thought has been put into ensuring that the burger has some structure (unless
`--gowild` is specified); for example, a 1-layer burger will just be a plain patty,
while a 2-layer burger will be a patty on some sort of bread, and a 3-layer burger is
basically a sandwich (bread / burger / bread).

There is no guarantee that the resulting burger actually _tastes_ any good.

Arguments about whether the lettuce goes on top or beneath may be raised as pull requests. ☺

## Usage

```text
usage: randomburger.py [-h] [--layers N] [--vegetarian] [--gowild]

Make some random burgers

options:
  -h, --help    show this help message and exit
  --layers N    How many Layers should the burger consist of?
  --vegetarian  Only use non-meat patties
  --gowild      Random number of Layers
```
