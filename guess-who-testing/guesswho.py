# Tuntomerkki/pidätys -systeemin pohjaa kokeilun vuoksi
# Tästä voi rakentaa ja muokata ja lisätä pääpeliin

import random


def main():
    enemy = generate_person()
    print(f"THIEF: {describe_person(enemy)}\n")

    print("You see the following people...\nWho is the thief?\n")
    enemy_index = random.randint(0,9)
    for i in range(10):
        if i == enemy_index:
            print(f"{[i+1]} {describe_person(enemy)}")
        else:
            npc = generate_person()
            while npc == enemy:
                npc = generate_person()
            print(f"[{i+1}] {describe_person(npc)}")

    selection = int(input("\nEnter a number to arrest a person: ")) - 1
    if selection == enemy_index:
        print("You arrested the thief! You win!")
    else:
        print("You arrested an innocent person. You lose.")


def generate_person():
    person = {}
    features = {
        "height":
            ["Short",
             "Average height",
             "Tall"],
        "age":
            ["young",
             "adult",
             "middle-aged",
             "old"],
        "gender":
            ["man",
             "woman"],
        "head":
            ["blonde hair",
             "brown hair",
             "long hair",
             "no hair",
             "a baseball cap",
             "sunglasses",
             "headphones"],
        "clothes":
            ["a hawaiian shirt",
             "a suit",
             "a dress",
             "a hoodie",
             "a denim jacket",
             "sweatpants"]
    }

    for feature in features:
        person[feature] = random.choice(features[feature])

    return person


def describe_person(p):
    return f"{p['height']} {p['age']} {p['gender']} with {p['head']} and {p['clothes']}"


main()
