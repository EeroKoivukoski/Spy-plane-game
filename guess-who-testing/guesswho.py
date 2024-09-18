# Tuntomerkki/pidätys -systeemin pohjaa kokeilun vuoksi
# Tästä rakennetaan ja muokataan pääpeliin


import random


def main():
    enemy = generate_person_description()
    print(f"THIEF: {enemy}\n")

    print("You see the following people...\nWho is the spy?\n")
    enemy_index = random.randint(0,9)
    for i in range(10):
        if i == enemy_index:
            print(f"{[i+1]} {enemy}")
            continue
        npc = generate_person_description()
        while npc == enemy:
            npc = generate_person_description()
        print(f"{[i+1]} {npc}")

    selection = int(input("\nEnter a number to arrest a person: "))
    if selection == enemy_index + 1:
        print("You arrested the thief! You win!")
    else:
        print("You arrested an innocent person. You lose.")


def generate_person_description():
    person = {
        "height": ["short", "average height", "tall"],
        "age": ["young", "adult", "middle-aged", "old"],
        "gender": ["man", "woman"],
        "hair": ["blonde", "brown", "dark", "gray", "no"],
        "clothes": ["a hawaiian shirt", "a suit", "a dress", "a hoodie", "a baseball cap", "sunglasses"]
    }

    for feature in person:
        person[feature] = random.choice(person[feature])

    return f"{person['height'].capitalize()} {person['age']} {person['gender']} with {person['hair']} hair and {person['clothes']}"


main()
