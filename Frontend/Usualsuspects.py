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
def minipeli():
    x = random.randint(1, 5)
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
        y = int(y)
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