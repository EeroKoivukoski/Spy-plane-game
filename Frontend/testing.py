import random
import mysql.connector
from geopy import distance
import tietokantatunnukset
from Usualsuspects import numerochecker

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

    # Pelaaja ja rosvo random kentillä (todo: varmista että rosvo tarpeeksi kaukana pelaajasta)
    current = random.choice(all_airports)
    enemy_airport = random.choice(all_airports)

    # Muuttujat
    km_flown = 0
    day = 0

    # Main loop
    while True:
        print(f"\nWelcome to {current['country']}! You are currently at {current['name']}.")
        print(f"You have travelled {km_flown} km in {day} day(s).\n")

        day += 1

        # Aloita minipeli
        voitto = minipeli(random.randint(1,5))
        if voitto == 2:
            print("You gained a clue!")
        elif voitto == 3:
            print("You wasted a day!")
            day+=1

        input("\nPress Enter to continue...\n")

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
        # Eero: Nyt jos kirjoittaa kirjaimen se kysyy uudelleen numeroa
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


# Eero: tähän funktioon tulee satunnaisten tapahtumien koodi jotka tapahtuvat jokaisen lennon jälkeen
def minipeli(x):
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
the call is you and tells you that they found new data on the suspect.
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


main()
