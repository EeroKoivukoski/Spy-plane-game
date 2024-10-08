import random
import mysql.connector
from geopy import distance
import tietokantatunnukset
import minipeli
import asci_lib

# asenna python packaget geopy, mysql-connector-python 8.0.29

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user=tietokantatunnukset.user,
    password=tietokantatunnukset.password,
    autocommit=True)


def main():
    #aloitus arvot
    continue_check=0
    all_airports = get_airports()
    suspect = generate_person()
    current = random.choice(all_airports)
    last = 0
    enemy_airport = random.choice(all_airports)

    asci_lib.asci("intro")
    username = input("Enter your name to start the game: ")

    player = {
        "name": username,
        "currentname":current["name"] ,
        "currentcountry": current["country"],
        "currentlatitude": current["latitude"],
        "currentlongitude": current["longitude"],
        "suspectheight": suspect["height"],
        "suspectage": suspect["age"],
        "suspectgender": suspect["gender"],
        "suspectclothes": suspect["clothes"],
        "suspecthead": suspect["head"],
        "enemy_airport_name": enemy_airport["name"],
        "enemy_airport_country": enemy_airport["country"],
        "enemy_airport_latitude": enemy_airport["latitude"],
        "enemy_airport_longitude": enemy_airport["longitude"],
        "madness": 0,
        "foodpoisoning": 0,
        "gun": 0,
        "guns": 0,
        "km_flown": 0,
        "day": 0,
        "last_move_day": 0,
        "given_clues": "Given@Clues",
    }

    data = get_player_data(username)

    if data:
        sel = input("[1]Uusi peli \n[2]Jatka vanhaa")
        sel = minipeli.numerochecker(sel, 2)
        if sel == 2:
            player = data
            continue_check = 1

        # Valitaan uusi peli = päivitetään rivi tietokannan taulussa
        else:
            update_player(player)
            continue_check = 2

    # Dataa ei löytynyt -> lisätään rivi tauluun
    else:
        insert_new_player(player)

    suspect = {"height": player["suspectheight"], "age": player["suspectage"],"gender":player["suspectgender"], "clothes":player["suspectclothes"], "head":player["suspecthead"]}
    current = {"name": player["currentname"], "country": player["currentcountry"],"latitude": float(player["currentlatitude"]),"longitude": float(player["currentlongitude"])}
    enemy_airport = {"name": player["enemy_airport_name"], "country": player["enemy_airport_country"], "latitude": float(player["enemy_airport_latitude"]), "longitude": float(player['enemy_airport_longitude'])}
    madness = player["madness"]
    foodpoisoning = player["foodpoisoning"]
    gun = player["gun"]
    guns = player["guns"]
    km_flown = player["km_flown"]
    day = player["day"]
    last_move_day = player["last_move_day"]
    given_clues=player["given_clues"]
    given_clues = list(given_clues.split("@"))



    # Tutorial
    if continue_check == 0:
        asci_lib.asci('tutorial')
        tutorial = input('')
        tutorial = minipeli.numerochecker(tutorial, 2)
        if tutorial == 1:
            print("you selected option 1")
        else:
            print("you selected option 2")
        input("press any key to continue")

    if continue_check == 2 or continue_check == 0:
        asci_lib.asci("loreone")
        mission = input()
        mission = minipeli.numerochecker(mission, 2)
        if mission == 2:
            asci_lib.asci('missionnah')
            exit()

    if len(given_clues) > 2:
        x=len(given_clues)-2
        while x != 0:
            print(f"You know the spies following features: {suspect[given_clues[1+x]]}")
            x-=1
    # Main loop
    while True:
        if day < 0:
            day = 0
        # Lopeta peli jos päivät täynnä
        if 30 < day:
            asci_lib.asci("gameover")
            exit()


        # Tulosta info
        if last == 0:
            print(f"Good Luck!\nWelcome to {current['country']}! You are currently at {current['name']}.\n")
            last = current
        elif last['country'] == current['country'] and last['name'] != current['name']:
            print(f"\nWelcome to {current['name']}!")
            last = current
        elif last != current:
            print(f"\nWelcome to {current['country']}! You are currently at {current['name']}.\n")
            last = current
        else:
            print(f"\nYou are still in {current['country']} at {current['name']}.\n")
        print(f"You have travelled {km_flown} km in {day} day(s).\n")
        print(f"You have {30 - day} days left.")

        # Siirrä rosvoa
        if day - last_move_day >= 5:
            print("You see on the tracker that the suspect has fled to another airport!")
            enemy_airport = random.choice(all_airports)
            last_move_day = day

        # Haluatko lentää vai minipeli?
        # Vaihtoehdot voisi olla esim: [1] Fly to another airport [2] Stay and look for clues
        # todo: jos samalla kentällä kuin rosvo -> suoraan guess who-arvailuun, ei muita vaihtoehtoja (miksi?)
        if current == enemy_airport:
            eveningoptions = input(
                '\n[1] Fly to another airport \n[2] Look around \n[3] try to guess who the spy is at this airport \nWhat do you want to do: ')
            eveningoptions = minipeli.numerochecker(eveningoptions, 3)
        else:
            eveningoptions = input(
                '\n[1] Fly to another airport \n[2] Stay at this airport  \nWhat do you want to do: ')
            eveningoptions = minipeli.numerochecker(eveningoptions, 2)

        # Lennä muualle
        if eveningoptions == 1:
            day += 1
            print("Where would you like to fly next?")
            print(f"You are currently at {current['name']} in {current['country']}.")
            print(f"{navigation(current, enemy_airport)}\n")

            # Hae n lähintä lentokenttää listaan
            # TODO: fiksumpi tapa tehdä tämä, näin voi jäädä kenttiä pois tai jumiin
            # Listaa ensin maat, sitten maan perusteella kentät(?)
            # Näytä onko kenttä lähempänä vai kauempana rosvosta kuin nykyinen kenttä(?)
            # Nyt navigointi on aika hämärää -> kestää kauan ja tylsää pelaajalle
            closest = get_closest_airports(current, 15)

            # Loop lähimpien kenttien läpi
            i = 1
            for airport in closest:
                # Tulosta kentän tiedot
                dist = calculate_distance(current, airport)
                print(f"[{i}] {airport['name']} ({airport['country']}) (Distance: {dist} km)")
                i += 1

            # Valitse ja päivitä tämänhetkinen kenttä & kilometrit
            # Tämä numerofunktioon?
            while True:
                selection = input("\nEnter a number to continue: ")
                try:
                    closest[int(selection) - 1]
                except ValueError:
                    print("That's not a number!")
                except IndexError:
                    print("That's not a valid number!")
                else:
                    selection = int(selection) - 1
                    if selection < 0:
                        print("That's not a valid number!")
                    else:
                        break

            km_flown += calculate_distance(current, closest[selection])
            current = closest[selection]

        # Koodi toistuu
        # todo: minipelin tulos toiseen funktioon (rakennetta uusiksi?)
        elif eveningoptions == 2:
            minipelitulos = minipeli.minipeli(current['country'], madness, foodpoisoning, gun, guns)
            if minipelitulos == 2:
                print_clue(suspect, given_clues)
            elif minipelitulos == 3:
                print("You lost a day!")
                day += 1
            elif minipelitulos == 4:
                print("You travel faster than expected! You gain an extra day.")
                day -= 1
            elif minipelitulos == 1:
                print("Nothing happens.")
            elif minipelitulos == 5:
                print('You gained the trait "Mad"')
                madness = 1
            elif minipelitulos == 6:
                print('You gained the trait "Food poisoning".')
                foodpoisoning = 1
            elif minipelitulos == 7:
                print("You lost a day!")
                day += 1
                print('You lost the trait "Food poisoning"... Good.')
                foodpoisoning = 0
            elif minipelitulos == 8:
                print("You got a gun... even though it seems to be an antique.")
                gun = 1
                guns = 1
                asci_lib.asci("GUN")
            elif minipelitulos == 9:
                print("You lost a day but got a clue!")
                day += 1
                print_clue(suspect, given_clues)
            elif minipelitulos == 10:
                print("You lost your gun!")
                gun = 0
            elif minipelitulos == 11:
                print("You lost your gun... But gained a clue.")
                gun = 0
                print_clue(suspect, given_clues)
            elif minipelitulos == 12:
                print('You regain your sanity. (Lost trait "Mad")')
                madness = 0
            input('\nPress enter to continue')

        # Tee tämä suoraan jos samalla kentällä kuin rosvo
        elif eveningoptions == 3 and current == enemy_airport:
            print("You see the following people...\nWho is the thief?\n")
            enemy_index = random.randint(0, 9)
            last_move_day = day
            for i in range(10):
                if i == enemy_index:
                    print(f"{[i + 1]} {describe_person(suspect)}")
                else:
                    npc = generate_person()
                    while npc == suspect:
                        npc = generate_person()
                    print(f"[{i + 1}] {describe_person(npc)}")

            selection = int(input("\nEnter a number to arrest a person: ")) - 1
            if selection == enemy_index:
                print("You arrested the thief!")
                asci_lib.asci("vakooja")
                print("You win! \nYou won in", day - 1, "Days!")
                exit()
            else:
                print("You arrested an innocent person. The spy hears about it and moves to another airport.")
                enemy_airport = random.choice(all_airports)

        given_clues="@".join(given_clues)
        player = {
            "name": username,
            "currentname":current["name"] ,
            "currentcountry": current["country"],
            "currentlatitude": current["latitude"],
            "currentlongitude": current["longitude"],
            "suspectheight": suspect["height"],
            "suspectage": suspect["age"],
            "suspectgender": suspect["gender"],
            "suspectclothes": suspect["clothes"],
            "suspecthead": suspect["head"],
            "enemy_airport_name": enemy_airport["name"],
            "enemy_airport_country": enemy_airport["country"],
            "enemy_airport_latitude": enemy_airport["latitude"],
            "enemy_airport_longitude": enemy_airport["longitude"],
            "madness": madness,
            "foodpoisoning": foodpoisoning,
            "gun": gun,
            "guns": guns,
            "km_flown": km_flown,
            "day": day,
            "last_move_day": last_move_day,
            "given_clues": given_clues,
        }
        update_player(player)
        given_clues = list(given_clues.split("@"))

def get_closest_airports(current, count):
    # Hae kaikki kentät listaan
    airports = get_airports()

    # Järjestä lista: jokaisen kohdalla laskee etäisyyden
    airports.sort(key=lambda d: calculate_distance(current, d))

    # Palauta listasta indeksit 1 -> count+1 (0 = nykyinen kenttä)
    return airports[1:count + 1]


def calculate_distance(current, target):
    # Laskee etäisyyden koordinaattien välillä geopy-kirjaston avulla
    a = (current["latitude"], current["longitude"])
    b = (target["latitude"], target["longitude"])
    dist = round(distance.distance(a, b).km)
    return dist


# Palauta lista lentokentistä säteen (km) sisällä
def get_airports_radius(current, radius_km):
    airports = get_airports()
    out = []
    for i in airports:
        dist = calculate_distance(current, i)
        if dist <= radius_km and current["name"] != i["name"]:
            out.append(i)
    return out


# Hakee kaikki lentokentät
def get_airports():
    # SQL-kysely
    sql = "select airport.name, latitude_deg, longitude_deg, country.name from airport, country where country.iso_country = airport.iso_country and airport.continent='EU' and airport.type='large_airport'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    # Tee lista johon tulee lentokentät
    airports = []

    # Loop tuloksien läpi, luo sanakirja lentokentälle -> sanakirja listaan
    for i in result:
        airport = {
            "name": i[0],
            "latitude": i[1],
            "longitude": i[2],
            "country": i[3],
        }
        airports.append(airport)

    return airports


def navigation(current, target):
    if calculate_distance(current, target) == 0:
        return "You are at the same airport as your target!"

    current_coords = (current["latitude"], current["longitude"])

    target_coords = (target["latitude"], current["longitude"])
    latitude_dist = round(distance.distance(current_coords, target_coords).km)
    if current["latitude"] <= target["latitude"]:
        latitude_out = f"{latitude_dist} km north"
    else:
        latitude_out = f"{latitude_dist} km south"

    target_coords = (current["latitude"], target["longitude"])
    longitude_dist = round(distance.distance(current_coords, target_coords).km)
    if current["longitude"] <= target["longitude"]:
        longitude_out = f"{longitude_dist} km east"
    else:
        longitude_out = f"{longitude_dist} km west"

    return f"Your target is {latitude_out} and {longitude_out} of you."


def generate_person():
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
             "dark hair",
             "long hair",
             "a bald head",
             "a baseball cap",
             "sunglasses",
             "headphones",
             "a clearly fake moustache"],
        "clothes":
            ["a hawaiian shirt",
             "a suit",
             "a dress",
             "a hoodie",
             "a denim jacket",
             "sweatpants",
             "student overalls"]
    }

    person = {}
    for feature in features:
        person[feature] = random.choice(features[feature])

    return person


def describe_person(p):
    return f"{p['height']} {p['age']} {p['gender']} with {p['head']} and {p['clothes']}"


def print_clue(suspect, given_clues):
    # Jos annetut vihjeet on tuntomerkkien määrä -> kaikki vihjeet annettu
    if (len(given_clues))-2 == len(suspect.keys()):
        print("All clues given!")
        return

    # Valitse random tuntomerkki, tarkista ettei ole jo annettu
    feature = random.choice(list(suspect.keys()))
    while feature in given_clues:
        feature = random.choice(list(suspect.keys()))
    given_clues.append(feature)

    # Tulosta tuntomerkki
    if feature == "height":
        print(f"The suspect is {suspect[feature]}.")
    elif feature == "age":
        print(f"The suspect is {suspect[feature]}.")
    elif feature == "gender":
        print(f"The suspect is a {suspect[feature]}.")
    elif feature == "head":
        print(f"The suspect has {suspect[feature]}.")
    elif feature == "clothes":
        print(f"The suspect is wearing {suspect[feature]}.")


def get_player_data(username):
    sql = f"""
    select name, currentname,currentcountry,currentlatitude,currentlongitude, suspectheight,suspectage,suspectgender,suspectclothes,suspecthead,enemy_airport_name, enemy_airport_country, enemy_airport_latitude,enemy_airport_longitude, madness, foodpoisoning, gun, guns, km_flown, day, last_move_day, given_clues from test_game
    where name = '{username}'
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    data = {}
    if result:
        data = {
            "name": result[0][0],
            "currentname": result[0][1],
            "currentcountry": result[0][2],
            "currentlatitude": result[0][3],
            "currentlongitude": result[0][4],
            "suspectheight": result[0][5],
            "suspectage": result[0][6],
            "suspectgender": result[0][7],
            "suspectclothes": result[0][8],
            "suspecthead": result[0][9],
            "enemy_airport_name": result[0][10],
            "enemy_airport_country": result[0][11],
            "enemy_airport_latitude": result[0][12],
            "enemy_airport_longitude": result[0][13],
            "madness": result[0][14],
            "foodpoisoning": result[0][15],
            "gun": result[0][16],
            "guns": result[0][17],
            "km_flown": result[0][18],
            "day": result[0][19],
            "last_move_day": result[0][20],
            "given_clues": result[0][21],
        }
    return data


def update_player(player):
    sql = f"""
    update test_game
    set currentname = '{player["currentname"]}',
    currentcountry = '{player["currentcountry"]}',
    currentlatitude = '{player["currentlatitude"]}',
    currentlongitude ='{player["currentlongitude"]}',
    suspectheight = '{player["suspectheight"]}',
    suspectage = '{player["suspectage"]}',
    suspectgender = '{player["suspectgender"]}',
    suspectclothes = '{player["suspectclothes"]}',
    suspecthead = '{player["suspecthead"]}',
    enemy_airport_name = '{player["enemy_airport_name"]}',
    enemy_airport_country = '{player["enemy_airport_country"]}',
    enemy_airport_latitude = '{player["enemy_airport_latitude"]}',
    enemy_airport_longitude = '{player["enemy_airport_longitude"]}',
    madness = '{player["madness"]}',
    foodpoisoning = '{player["foodpoisoning"]}',
    gun = '{player["gun"]}',
    guns = '{player["guns"]}',
    km_flown = '{player["km_flown"]}',
    day = '{player["day"]}',
    last_move_day = '{player["last_move_day"]}',
    given_clues = '{player["given_clues"]}'
    where name = '{player["name"]}'
    """
    cursor = connection.cursor()
    cursor.execute(sql)


def insert_new_player(player):
    sql = f"""
    insert into test_game values
    ('{player["name"]}',
    '{player["currentname"]}',
    '{player["currentcountry"]}',
    '{player["currentlatitude"]}',
    '{player["currentlongitude"]}',
    '{player["suspectheight"]}',
    '{player["suspectage"]}',
    '{player["suspectgender"]}',
    '{player["suspectclothes"]}',
    '{player["suspecthead"]}',
    '{player["enemy_airport_name"]}',
    '{player["enemy_airport_country"]}',
    '{player["enemy_airport_latitude"]}',
    '{player["enemy_airport_longitude"]}',
    '{player["madness"]}',
    '{player["foodpoisoning"]}',
    '{player["gun"]}',
    '{player["guns"]}',
    '{player["km_flown"]}',
    '{player["day"]}',
    '{player["last_move_day"]}',
    '{player["given_clues"]}')
"""
    cursor = connection.cursor()
    cursor.execute(sql)


main()
