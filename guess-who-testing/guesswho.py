import random


def main():
    spy = generate_person_description()
    print(f"SPY: {spy}\n")

    print("You see the following people...\nWho is the spy?\n")
    spy_index = random.randint(0,9)
    for i in range(10):
        if i == spy_index:
            print(f"{[i+1]} {spy}")
            continue
        npc = generate_person_description()
        while npc == spy:
            npc = generate_person_description()
        print(f"{[i+1]} {npc}")

    selection = int(input("\nEnter a number to arrest a person: "))
    if selection == spy_index + 1:
        print("You arrested the spy! You win!")
    else:
        print("You arrested an innocent person. You lose.")


def generate_person_description():
    person = {
        "height": ["short", "average height", "tall"],
        "age": ["young", "adult", "middle-aged", "old"],
        "gender": ["man", "woman"],
        "hair": ["blonde", "brown", "dark", "no", "red", "gray"],
        "clothes": ["a hawaiian shirt", "a suit", "a dress", "a hoodie", "a baseball cap", "sunglasses"]
    }

    for feature in person:
        person[feature] = random.choice(person[feature])

    return f"{person['height'].capitalize()} {person['age']} {person['gender']} with {person['hair']} hair and {person['clothes']}"


main()
