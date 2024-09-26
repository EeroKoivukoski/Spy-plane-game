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
    valinta = random.randint(1, 8)
    # Esimerkki
    if valinta == 1:
        print("""
Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki Esimerkki...

You dont know why you're thinking example in finnish.
The thought passes and you continue about your day.
""")
        return 1
    # HQ saa selville ulkonäön osan
    elif valinta == 2:
        print("""
You get a call from HQ 
The Call is from your boss who tells you that they found new data on the suspect.
""")
        return 2
    # Ruokaika
    elif valinta == 3:
        print("""
You felt quite hungry and chose to go for a bite.
You ate at the airport like normal.
""")
        return 1
    # Hukkunut lippu
    elif valinta == 4:
        print("""
While walking through the airport like normal, you notice that your ticket is missing.
You probably accidentally dropped your ticket.
""")
        choice = input(f"[1] Yes\n[2] No\n\nDo you stay a day to find your ticket?")
        choice = numerochecker(choice,2)
        if choice == 1:
            z=random.randint(1,10)
            if z < 7:
                print("You search for it but when you find it you have missed the flight.")
                return 3
            if z > 6:
                choiceinfo=input("""
You find your ticket under a bench. You notice that under the bench next to your ticket is a message
which says "You dont know me. But I know who you are searching for". Then the ticket details a deal 
between you and the messager. The deal is you drop off a file under a bridge nearby then after that 
you will get a location where info of the suspect is hidden.

[1] Yes
[2] No

Do you want the make a deal.:
 """)
                if choiceinfo == 1:
                    rng=random.randint(1,10)
                    if rng < 7:
                        print("You hide the file under the bridge but never get an answer.")
                        return 3
                    if rng > 6:
                        print("You hide the file under the bridge... and get the location of the info!")
                        return 4
                if choiceinfo == 2:
                    print("You leave the airport thinking about what could have been")
        else:
            print("You leave the airport thinking about your dear lost ticket :(.")
            return 1
    # Tappelu konnien kanssa
    elif valinta == 5:
        print('''
You are moving through the airport until you come accross three intimidating fellows.
One of the goons whispers to the other "hey, isn't that the guy we're supposed to whack".

[1] Fight (50% reward, 50% penalty)
[2] Run(100% success)
''')
        choice = input('Do you want to fight the goons?: ')
        choice = numerochecker(choice,2)
        if choice == 1:
            tappelu = random.randint(1, 10)
            if tappelu == 1:
                print("You win the fight and interrogate the goons!")
                return 2
            else:
                print("You lose to the goons and have to waste a day resting.")
                return 3
        else:
            print("You successfully run away!")
            return 1
#Mainos "ständi"
    elif valinta == 6:
        print('''
While moving through the airport, you spot a advertisement stand.
You have to walk past them to get to the seats.

[1] Try to iqnore them and walk past em'
[2] Talk with the advertisers?
''')
        choice=input('Do you want to ignore the advertisers')
        choice = numerochecker(choice, 2)
        if choice == 1:
            print("You ignored the workers despite the advertisers best attempts.")
            return 1
        if choice == 2:
            rngkoju=random.randint(1,4)
            if rngkoju == 1:
                print('''
You for some reason decide to talk with the advertisers.
They apparently are advetising a rocket travel company and are
offering a free test ride to the first customer.
''')
                return 4
            if rngkoju == 2:
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
            if rngkoju == 3:
                print('''
You for some reason decide to talk with the advertisers.
They apparently are advetising a worldwide detective agency.
You laugh into their faces when they tell you they can locate any man in the world.
They get aggrevated by your laughter so they ask you if you are looking for anyone.
You decide to ask them about the spy you're tracking and
To your suprise they actually find a picture of him.
''')
                return 2
            if rngkoju == 4:
                print('''
You for some reason decide to talk with the advertisers.
They apparently are advetising a worldwide detective agency.
You laugh into their faces when they tell you they can locate any man in the world.
They get aggrevated by your laughter so they ask you if you are looking for anyone.
You decide to ask them about the spy you're tracking and
they do not find him and you leave the stand with a grin on your face.
''')
                return 1
    elif valinta == 7:
        print('''
You are walking at the airport and you feel that the world is against you.
[1] Fight
[2] What?
        ''')
        schizo = input('Do you want to fight the airport: ')
        schizo = numerochecker(schizo,2)
        if schizo == 1:
            print('You fight the airport')
            return 3
        else:
            print('you do not fight the airport')
            return 1
    #trivia
    elif valinta == 8:
        if country == "Finland":
            answer=(input("What is the capital of Finland?: ")).upper()
            if answer == "HELSINKI":
                print("Correct!")
                return 4
            else:
                print("WRONG!")
                return 3
        elif country == "France":
            answer=(input("What is the capital of France?: ")).upper()
            if answer == "PARIS":
                print("Correct!")
                return 4
            else:
                print("WRONG!")
                return 3
        elif country == "Germany":
            answer=(input("What is the capital of Germany?: ")).upper()
            if answer == "BERLIN":
                print("Correct!")
                return 4
            else:
                print("WRONG!")
                return 3
        elif country == "Italy":
            answer=(input("What is the capital of Italy?: ")).upper()
            if answer == "ROME":
                print("Correct!")
                return 4
            else:
                print("WRONG!")
                return 3
        elif country == "Spain":
            answer=(input("What is the capital of Spain?: ")).upper()
            if answer == "MADRID":
                print("Correct!")
                return 4
            else:
                print("WRONG!")
                return 3
        else:
            noneofthesegoddamncountries = minipeli(country)
            return noneofthesegoddamncountries

    elif valinta == 10:
        print("""
Your gut feels off. You suspect that the food you just ate was spoiled. 

[1] Fly
[2] Don't fly
""")
        poopypants = input("Do you risk the flight?: ")
        poopypants = numerochecker(poopypants,2)
        if poopypants == 1:
            tragdialaskuri = random.randint(1,3)
            if tragdialaskuri == 1:
                print("""
You lay waste on the plane. Your sewage was potent enough to cancel the flight. 
The airport staff never found out it was you but they will remember. 
You wasted a day due to your cancelled flight
""")
                return 3
            else:
                print("You survived the flight. ")
                return 1
        elif poopypants != 1:
            nextflightlaskuri = random.randint(1,2)
            if nextflightlaskuri == 1:
                print("Luckily you were able to get on the next flight and only lost a few hours! ")
                extraclue = random.randint(1,7)
                if extraclue > 1:
                    return 1
                if extraclue == 1:
                    print("You got a tip of your target from an unknown source. ")
                    return 2
            if nextflightlaskuri == 2:
                print("You waste the day at the airport. ")
                return 3



def minipelitulos(z):
    if z == 1:
        print("You gained nothing.")
        return 0
    elif z == 2:
        print("You gained a clue!")
        return 2
    elif z == 3:
        print("You wasted a day!")
        return 1
    elif z == 4:
        print("You travel fast!(save a day.)")
        return -1


