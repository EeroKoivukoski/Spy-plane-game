import random

from asci_lib import asci

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


def minipeli(country,madness,foodpoisoning,gun,guns):
    valinta = random.randint(1, 11)
    # Madness good event
    if valinta == 1 and madness == 1:
        asci('maniac')
        print("You imagine yourself going back in time. Your madness becomes reality. ")
        return 4
    # Madness trait
    elif valinta == 1:
        mielentila = input("""
The walls are closing in. 

[1] Fight
[2] Accept

Do you fight back or accept the new reality?: """)
        mielentila = numerochecker(mielentila, 2)
        if mielentila == 1:
            print("You shake your head and the world seems normal again.")
            return 1
        if mielentila == 2:
            asci('maniac')
            print("You hit your head against a wall until it goes numb. ")
        return 5
    #HQ lähettää sinulle aseen
    elif valinta == 2 and gun == 0 and guns==0:
        print("""
You get a call from HQ 
The Call is from your boss who tells you that they got new funding for weapons.
Apparently you are getting your very own pistol!
""")
    # Uusi ase, ensimmäinen hävitetty
        return 8
    elif valinta == 2 and gun == 0 and guns == 1:
        print("""
You get a call from HQ 
Your application for a replacement pistol has been processed...   and accepted!
This will impact your next salary.
""")
        return 8
    # HQ saa selville ulkonäön osan
    elif valinta == 2:
        asci("radio")
        print("""
You get a call from HQ 
The Call is from your boss who tells you that they found new data on the suspect.
""")
        return 2
    # Ruokaika
    elif valinta == 3:
        asci('RUOKA')
        print("""
You felt quite hungry and chose to go for a bite.
You ate street food at a grill for cheap.
""")
        illness = random.randint(1, 10)
        if illness == 1:
            return 6
        else:
            return 1
    # Hukkunut lippu (todo: voisi tehdä kiinnostavamman, myös ascii)
    elif valinta == 4:
        print("""
While walking through the city like you usually do, 
you notice that your company credit card is missing.
You probably accidentally dropped your card.
""")
        choice = input(f"[1] Try looking for it\n[2] Just get a new one \n\nDo you use the day to find your card or do you order a new one?: ")
        choice = numerochecker(choice,2)
        if choice == 1:
            z=random.randint(1,10)
            if z < 7:
                print("You search for it but when you find it, it is too late do anything else. ")
                return 3
            if z > 6:
                choiceinfo=input("""
You find your card under a bench you sat at before. You noticed that under the bench next to your card is a message
which says "You dont know me. But I know who you are searching for. Let's make a deal!". 
The deal is you drop off a file under a bridge nearby then after that 
you will get a location where info of the suspect is hidden.

[1] Make a deal with the stranger
[2] Just dismiss the message and be happy about finding your credit card

Do you want the make a deal?: """)
                choiceinfo=numerochecker(choiceinfo,2)
                if choiceinfo == 1:
                    rng=random.randint(1,10)
                    if rng < 7:
                        print("You hide the file under the bridge but never get an answer.")
                        return 3
                    if rng > 6:
                        print("You hide the file under the bridge...   and get the location of the info!")
                        return 2
                if choiceinfo == 2:
                    print("You leave the message alone thinking about what could have been.")
        else:
            print("You leave the card behind while thinking about the possibility that it could have been stolen. :(")
            return 1
    # Tappelu konnien kanssa
    elif valinta == 5:
        asci('intimidating')
        print('''You are moving through the city until you come accross three intimidating fellows.
One of the goons whispers to the other "hey, isn't that the guy we're supposed to whack".
    
[1] Fight
[2] Run
''')
        if gun == 0:
            choice = input('Do you want to fight the goons?: ')
            choice = numerochecker(choice, 2)
        else:
            choice = input('Do you want to fight the goons?: ')
            choice = numerochecker(choice, 2)
            if choice == 1:
                choice=int(3)
        if choice == 1:
            tappelu = random.randint(1, 10)
            if tappelu == 1:
                print("You win the fight and interrogate the goons!")
                return 2
            else:
                print("You lose to the goons and have to waste a day resting.")
                return 3
        if choice == 2:
            print("You successfully run away!")
            return 1
        if choice == 3:
            print("You win the fight and interrogate the goons!"
                  "You lose your gun in the mettle.")
            return 11

    # Mainos "ständi" (todo: eri ascii eri ständeihin, myös jos jaksaa voisi lisätä ständejä)
    elif valinta == 6:
        print('''
While moving through the a local shopping mall, you spot an advertisement stand.
You have to walk past them.

[1] Try to iqnore them.
[2] Talk with the advertisers?
''')
        choice=input('Do you want to ignore the advertisers: ')
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
    # Madness bad event
    elif valinta == 7 and madness == 1:
        print('''
You are walking at the airport and you feel that the world is against you.
[1] Fight
[2] What?
        ''')
        schizo = input('Do you want to fight the airport: ')
        schizo = numerochecker(schizo,2)
        if schizo == 1:
            asci('maniac')
            print("""You fight the airport and punch a hole through a wall. You got detained 
but your violence felt justified. """)
            return 12
        else:
            asci('maniac')
            print("""You fight the airport and break a door despite your decision.
You waste a day in jail. """)
            return 3
    # Uneasy feeling (todo: kiinnostavampi)
    elif valinta == 7:
        print("You feel a sense of unease but carry on.")
        return 1
    # Trivia based on current country (todo: voisi lisätä maita ja mahdollisesti toisia mahdollisia kysymyksiä)
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
            noneofthesegoddamncountries = minipeli(country,madness,foodpoisoning,gun,guns)
            return noneofthesegoddamncountries
    # Old man encounter
    elif valinta == 9:
        asci('VANHAMIES')
        choice = input('''
A strange old man with a thick accent asks you for directions. 
He seems quite nervous..
Do you help the man, interrogate him or escape the situation?

[1] Help
[2] Interrogate
[3] Escape

What do you want to do?: ''')
        choice = numerochecker(choice, 3)
        if choice == 1:
            helpe = random.randint(1, 10)
            if helpe <= 3:
                print("The man thanks you and leaves")
                return 1
            elif helpe >= 7:
                print("The man attacks you when you least expect it and leaves you injured")
                return 3
            elif 6 >= helpe >= 4:
                print("The man abruptly hands you a piece of paper that seems important, and leaves")
                return 2
        elif choice == 2:
            intero = random.randint(1, 3)
            if intero == 1:
                print('''
You interrogate a poor old man who barely understands you.
He's clearly innocent and you make a fool of yourself.
            ''')
                return 1
            elif intero == 2:
                print('''
The man calls you a fool and hands you a piece of paper that seems important.
                    ''')
                return 2
            elif intero == 3:

                chase = input('''
The man instantly recognizes what you're doing and starts running away.

[1] Yes
[2] No

Do you chase him?: ''')
                chase = numerochecker(chase, 2)
                if chase == 1:
                    chaseresult = random.randint(1, 3)
                    if chaseresult == 1:
                        print("You chase the man for a while, but after a lengthy chase you lose sight of him")
                        return 1

                    elif chaseresult == 2:
                        print('''
The old man doesn't stand a chance running away from you, and you catch up to him soon after
He hands you a piece of paper that seems important, and proves he is there to help you.

                    ''')
                        return 2

                    elif chaseresult == 3:
                        print('''
You chase the old man into an alley full of suspicious individuals who stop you in your tracks.
Thankfully, they spare all but your phone and wallet.

                    ''')
                        return 3
                if choice == 3:
                    print("You escape from the old man with no problems")
                    return 1
    # Ruokamyrkytys lopputulos :) (todo: ascii :( )
    elif valinta == 10 and foodpoisoning == 1:
        print("""
Your gut feels off. You suspect that the food you just ate was spoiled. 

[1] Fly
[2] Don't fly
""")
        vessavalinta = input("Do you risk the flight?: ")
        vessavalinta = numerochecker(vessavalinta,2)
        if vessavalinta == 1:
            tragedialaskuri = random.randint(1,3)
            if tragedialaskuri == 1:
                print("""
You lay waste on the plane. Your sewage was potent enough to cancel the flight. 
The airport staff never found out it was you but they will remember. 
You wasted a day due to your cancelled flight.
""")
                return 7
            else:
                print("You survived the flight.")
                return 1
        elif vessavalinta != 1:
            nextflightlaskuri = random.randint(1,2)
            if nextflightlaskuri == 1:
                print("Luckily you were able to get on the next flight and only lost a few hours!")
                extraclue = random.randint(1,7)
                if extraclue > 1:
                    return 1
                if extraclue == 1:
                    print("Apparently an informant whose phone died was coming to you, and since you stayed you got to talk with him.")
                    return 2
            if nextflightlaskuri == 2:
                print("There were no other flights to your destination today, so waste the day at the airport.")
                return 3

    elif valinta == 10:
        print('''
You are walking trough the city until a car stops in front of you.
The door opens and you think about entering this luxurious limousine.
 
 [1] Enter the car
 [2] Don't enter the car
 ''')
        auto=input('Do you enter?: ')
        auto=numerochecker(auto,2)
        if madness == 1:
            asci('maniac')
            print('''Instantly you jump in the car and jump past the man in the back. You pry yourself from the back of the limo to the frontseats. There are 
two very confused men. You manage to kick both of the men out of the limo and you take the wheel. Then you drive to the airport way over
the speed limit.
''')
            return 4
        elif auto == 1:
            if random.randint(1,2) == 1:
                print("You sit in the limo and it's your childhood friend, he tells you he saw you on the streets and decided to give you a ride")
                return 4
            else:
                print("You sit in the car and immediately the door closes behind you. You look up but before you see who is standing inside the limo\n you get knocke out.\n\nYou wake up in the middle of the city and you noctice the day has gone.")
                return 3
        elif auto == 2:
            if random.randint(1,2) == 1:
                if gun == 1:
                    print("The car starts chasing you and you have to decide on the counteraction!\n\n[1] Try to get to the nearby alley\n\n[2] Try to dodge the car\n\n[3] Shoot at the car")
                    autokarku = input('What do you want to do: ')
                    autokarku = numerochecker(autokarku, 3)
                    if autokarku == 1:
                        if random.randint(1, 3) <= 2:
                            print("You barely got hit by the car! the car leaves while you lay on the ground and you go to the hospital.")
                            return 3
                        else:
                            print("The Car barely misses you since it didn't fit in the alley. You pull the driver out of the  car and get\ninformation about the spy for letting him leave.")
                            return 2
                    elif autokarku == 2:
                        if random.randint(1, 3) <= 2:
                            print("You got hit by the car and end up in the hospital.")
                            return 3
                        else:
                            print("You dodge the car and you run away.")
                            return 1
                    else:
                        print("You shoot at the driver and hit him.\nThe car stops and you interrogate the driver while giving him aid.\nYour gun broke when you fired it. I guess you shouldnt use antiques.")
                        return 11
                if gun == 0:
                    print("The car starts chasing you and you have to decide on the counteraction!\n\n[1] Try to get to the nearby alley\n\n[2] Try to dodge the car")
                    autokarku=input('What do you want to do: ')
                    autokarku=numerochecker(autokarku,2)
                    if autokarku == 1:
                        if random.randint(1, 3) <= 2:
                            print(
                                "You barely got hit by the car! The car leaves while you lay on the ground. \You somehow don't feel like anythings broken but you go to the hospital anyways.")
                            return 3
                        else:
                            print(
                                "The Car barely misses you since it didn't fit in the alley. You pull the driver out of the  car and get\ninformation about the spy for letting him leave.")
                            return 2
                    else:
                        if random.randint(1, 3) <= 2:
                            print("You got hit by the car and end up in the hospital. Gladly you somehow only strained your ankle.")
                            return 3
                        else:
                            print("You dodge the car and you run away unharmed.")
                            return 1
        else:
                input("You leave the car alone.")
                return 1

    elif valinta == 11 and madness == 1:
        hullumyrskylentovalinta = input("""
the weather report is talking about a hurricane later today in the area.
You remember the helicopter the hotel owns. 

[1] Steal the helicopter!
[2] What?!

Do you want to fly??: """)
        hullumyrskylentovalinta = numerochecker(hullumyrskylentovalinta, 2)
        if hullumyrskylentovalinta == 1:
            asci('maniac')
            print("""You jump on the helicopter and pierce the stormy sky.
You will do whatever it takes to find your target.""")
            return 1
        else:
            asci('maniac')
            print("""Your sentient body drags your reluctant mind inside the helicopter.
You fly though the thundering skies realizing that your body has a mission of its own""")
            return 1


    elif valinta == 11:
        print("The weather report talks about a small hurricane in the area.\nThe hotel you are staying at isn't letting anyone leave today.")
        myrskylentovalinta = input("""
[1] Spend the day piecing together possible clues at the hotel.
[2] Explain the "nuclear" situation to the hotel management to get out of the hotel

Do you stay at the hotel: """)
        myrskylentovalinta = numerochecker(myrskylentovalinta, 2)
        if myrskylentovalinta == 1:
            lentovihjemahdollisuus = random.randint(1, 6)
            if lentovihjemahdollisuus == 1:
                print("After a long night of looking at your files of the case, you noctice a person you didn't see before"
"in the cctv footage from the night of the nuke robbery")
                return 9
            else:
                print("You spent the night staring at the ceiling not seeing any possible connections in your files.")
                return 3
        else:
            lentosiirtomahdollisuus = random.randint(1, 6)
            if lentosiirtomahdollisuus == 1:
                print('They suprisingly let you out saying "These so called hurricanes happen all the time here".')
                return 1
            else:
                print("They called you a liar and told you to wait for tomorrow.")
                return 3
