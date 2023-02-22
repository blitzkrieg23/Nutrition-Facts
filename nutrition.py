x = input("Item: ")
x = x.lower().rstrip('s')

fruits = {
    "apple": 130,
    "avocado": 50,
    "banana":110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries":50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

matching_key = None
for key in fruits:
    if x in key:
        matching_key = key
        break

if matching_key is not None:
    print("Calories: {}".format(fruits[matching_key]))
