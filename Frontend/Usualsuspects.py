import random
def numerochecker(y,z):
   z+=1
   while True:
        try:
            int(y)
        except ValueError:
            print("That's not a number!")
        else:
            y = int(y)
            for i in range(1, z):
                if y == i:
                    return y
        y=input("Enter the input: ")

def minipeli(country):
    x = random.randint(1, 8)
    # Esimerkki
    if x == 1:
        print("""
Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki...

You dont know why you're thinking example in finnish.
The thought passes and you continue about your day.
""")
        return 1
    # HQ saa selville ulkonäön osan
    elif x == 2:
        print("""
You get a call from HQ 
The Call is from your boss who tells you that they found new data on the suspect.
""")
        return 2
    # Ruokaika
    elif x == 3:
        print("""
You felt quite hungry and chose to go for a bite.
You ate at the airport like normal.
""")
        return 1
    # Hukkunut lippu
    elif x == 4:
        print("""
While walking through the airport like normal, you noctice that your ticket is missing.
You probably accidentally dropped your ticket.
""")
        y = input("Do you stay a day to find your ticket? (Yes=1/No=2): ")
        y = numerochecker(y,2)
        if y == 1:
            print("You stay to search for it")
            return 3
        else:
            print("You leave the airport thinking about your dear lost ticket :(.")
            return 1
    # Tappelu konnien kanssa
    elif x == 5:
        print('''
You are moving through the airport until you come accross three intimidating fellows.
One of the goons whispers to the other "hey, isn't that the guy we're supposed to whack".
''')
        y = input('Do you want to fight the goons(50% reward, 50% penalty) or run (100% success)? (Yes=1/No=2): ')
        y = numerochecker(y,2)
        if y == 1:
            z = random.randint(1, 2)
            if z == 1:
                print("You win the fight and interrogate the goons!")
                return 2
            else:
                print("You lose to the goons and have to waste a day resting.")
                return 3
        else:
            print("You successfully run away!")
            return 1
#Mainos "ständi"
    elif x == 6:
        print('''
While moving through the airport, you spot a advertisement stand.
You have to walk past them to get to the seats.
''')
        y=input('Do you want to ignore the advertisers Yes=1/No=2')
        y = numerochecker(y, 2)
        if y == 1:
            print("You ignored the workers despite the advertisers best attempts.")
            return 1
        if y == 2:
            z=random.randint(1,4)
            if z == 1:
                print('''
You for some reason decide to talk with the advertisers.
They apparently are advetising a rocket travel company and are
offering a free test ride to the first customer.
''')
                return 4
            if z == 2:
                print('''
You for some reason decide to talk with the advertisers.
They apparently are advetising a investment company and
are asking you for a deposit into their company. It sounds
reasonable so you agree.

After that you sit down and check your bank account and noctice that your balance is 0€.
You look around and noctice that the advertisement stand has disappeared.

You spend the rest of day negotiating with HQ about getting your salary in advance
''')
                return 3
            if z == 3:
                print('''
You for some reason decide to talk with the advertisers.
They apparently are advetising a worldwide detective agency.
You laugh into their faces when they tell you they can locate any man in the world.
They get aggrevated by your laughter so they ask you if you are looking for anyone.
You decide to ask them about the spy you're tracking and
To your suprise they actually find a picture of him.
''')
                return 2
            if z == 4:
                print('''
You for some reason decide to talk with the advertisers.
They apparently are advetising a worldwide detective agency.
You laugh into their faces when they tell you they can locate any man in the world.
They get aggrevated by your laughter so they ask you if you are looking for anyone.
You decide to ask them about the spy you're tracking and
they do not find him and you leave the stand with a grin on your face.
''')
                return 1
    elif x == 7:
        print('''
You are walking at the airport and you feel that the world is against you
        ''')
        y = input('Do you want to fight the airport Yes=1/No=2')
        y = numerochecker(y,2)
        if y == 1:
            print('You fight the airport')
            return 3
        if y == 2:
            print('you do not fight the airport')
            return 1
    #trivia
    elif x == 8:
        if country == "Finland":
            y=input("What is the capital of Finland?: ")
            if y == "Helsinki":
                print("Correct!")
                return 4
            else:
                print("WRONG!")
                return 3
        elif country == "France":
            y=input("What is the capital of France?: ")
            if y == "Paris":
                print("Correct!")
                return 4
            else:
                print("WRONG!")
                return 3
        elif country == "Germany":
            y=input("What is the capital of Germany?: ")
            if y == "Berlin":
                print("Correct!")
                return 4
            else:
                print("WRONG!")
                return 3
        elif country == "Italy":
            y=input("What is the capital of Italy?: ")
            if y == "Rome":
                print("Correct!")
                return 4
            else:
                print("WRONG!")
                return 3
        elif country == "Spain":
            y=input("What is the capital of Spain?: ")
            if y == "Madrid":
                print("Correct!")
                return 4
            else:
                print("WRONG!")
                return 3
        else:
            y=minipeli(country)
            return y