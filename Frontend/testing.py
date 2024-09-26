import random
import mysql.connector
from geopy import distance
import tietokantatunnukset
import Usualsuspects

#asenna python packaget geopy, mysql-connector-python 8.0.29

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user=tietokantatunnukset.user,
    password=tietokantatunnukset.password,
    autocommit=True
)

player = {}
enemy = {}


def main():
    all_airports = get_airports()
    #Rosvon ulkonäkö
    suspect = generate_person()

    # Pelaaja ja rosvo random kentillä (todo: varmista että rosvo tarpeeksi kaukana pelaajasta)
    current = random.choice(all_airports)
    enemy_airport = random.choice(all_airports)

    # Muuttujat
    km_flown = 0
    day = 0
    last_move_day = 0
    clues = 0

    # Main loop
    while True:
        print(f"\nWelcome to {current['country']}! You are currently at {current['name']}.")
        print(f"You have travelled {km_flown} km in {day} day(s).\n")
        if day-last_move_day >= 5:
            print("You see on the tracker that the suspect changed places")
            enemy_airport = random.choice(all_airports)
            last_move_day = day
        day += 1

        # Aloita minipeli
        z = int(Usualsuspects.minipelitulos(Usualsuspects.minipeli(current['country'])))

        if z == 2:
            clues = 1
        if z == 1 or z == -1:
            day = day + z
        input('\nPress enter to continue')
        if current == enemy_airport:
            z=input('\n[1] Fly to another airport \n[2] Stay at this airport \n[3] try to guess who the spy is at this airport \nWhat do you want to do: ')
            z = Usualsuspects.numerochecker(z, 3)
        else:
            z = input('\n[1] Fly to another airport \n[2] Stay at this airport  \nWhat do you want to do: ')
            z = Usualsuspects.numerochecker(z, 2)
        if z == 3 and current == enemy_airport :
            print("You see the following people...\nWho is the thief?\n")
            enemy_index = random.randint(0, 9)
            last_move_day=day
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
                print("You arrested the thief! You win!")
                exit()
            else:
                print("You arrested an innocent person. The spy hears about it and moves to another airport.")
                enemy_airport = random.choice(all_airports)

        elif z == 1:
            print("Where would you like to fly next?")
            print(f"You are currently at {current['name']} in {current['country']}.")
            # Navigaatiosysteemi kokeilun vuoksi - ei pakko käyttää
            print(f"{navigation(current, enemy_airport)}\n")

            # Hae 10 lähintä lentokenttää listaan
            # TODO: fiksumpi tapa tehdä tämä, näin voi jäädä kenttiä pois tai jumiin
            closest = get_closest_airports(current, 15)
            #closest = get_airports_radius(current, 500)

            # Loop lähimpien kenttien läpi
            i = 1
            for airport in closest:
                # Tulosta kentän tiedot
                dist = calculate_distance(current, airport)
                print(f"[{i}] {airport['name']} ({airport['country']}) (Distance: {dist} km)")
                i += 1

            # Valitse ja päivitä tämänhetkinen kenttä & kilometrit
            while True:
                selection = input("\nEnter a number to continue: ")
                try:
                    closest[int(selection) - 1]
                except ValueError:
                    print("That's not a number!")
                except IndexError:
                    print("That's not a valid number!")
                else:
                    selection = int(selection)-1
                    if selection < 0:
                        print("That's not a valid number!")
                    else:
                        break

            km_flown += calculate_distance(current, closest[selection])
            current = closest[selection]
        elif z == 2:
            z = int(Usualsuspects.minipelitulos(Usualsuspects.minipeli(current['country'])))
            if z == 2:
                clues = 1
            if z == 1 or z == -1:
                day = day + z
            input('\nPress enter to continue')


def get_closest_airports(current, count):
    # Hae kaikki kentät listaan
    airports = get_airports()

    # Järjestä lista: jokaisen kohdalla laskee etäisyyden
    airports.sort(key=lambda d: calculate_distance(current, d))

    # Palauta listasta indeksit 1 -> count+1 (0 = nykyinen kenttä)
    return airports[1:count+1]


def calculate_distance(current, target):
    # Laskee etäisyyden koordinaattien välillä geopy-kirjaston avulla
    a = (current["latitude"], current["longitude"])
    b = (target["latitude"], target["longitude"])
    dist = round(distance.distance(a,b).km)
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
    sql = "select name, latitude_deg, longitude_deg, iso_country from airport where continent='EU' and type='large_airport'"
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
            "country": get_country_by_code(i[3]),
        }
        airports.append(airport)

    return airports


# Hae tietokannasta maan nimi ISO-koodin perusteella
def get_country_by_code(iso):
    sql = f'select name from country where iso_country = "{iso}"'
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0][0]


def navigation(current, target):
    if calculate_distance(current, target) == 0:
        return "You are at the same airport as your target!"

    current_coords = (current["latitude"], current["longitude"])

    target_coords = (target["latitude"], current["longitude"])
    latitude_dist = round(distance.distance(current_coords, target_coords).km)
    latitude_out = ""
    if current["latitude"] <= target["latitude"]:
        latitude_out = f"{latitude_dist} km north"
    else:
        latitude_out = f"{latitude_dist} km south"

    target_coords = (current["latitude"], target["longitude"])
    longitude_dist = round(distance.distance(current_coords, target_coords).km)
    longitude_out = ""
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


def print_clue(suspect):
    feature = random.choice(suspect.keys())
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
    else:
        print("This is supposed to be a clue - something went wrong!")


main()
