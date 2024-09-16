import random
import mysql.connector
from geopy import distance
import tietokantatunnukset

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
    # Aloita random lentokentältä
    current = random.choice(get_airports())

    # Lennetyt kilometrit
    km_flown = 0

    # Main loop
    while True:
        print(f"\nWelcome to {current['country']}! You are currently at {current['name']}.")
        print(f"You have travelled {km_flown} km.")
        print("Where would you like to fly next?\n")

        # Hae 10 lähintä lentokenttää listaan
        #closest = get_closest_airports(current, 10)
        closest = get_airports_radius(current, 500)

        # Loop lähimpien kenttien läpi
        i = 1
        for airport in closest:

            # Tulosta kentän tiedot
            dist = round(calculate_distance(current, airport))
            print(f"[{i}] {airport['name']} ({airport['country']}) (Distance: {dist} km)")
            i += 1

        # Valitse ja päivitä tämänhetkinen kenttä & kilometrit
        # Eero: Nyt jos kirjoittaa kirjaimen se kysyy uudelleen numeroa
        while True:
            selection = input("\nEnter a number to continue: ")
            try:
                val = int(selection)
            except ValueError:
                print("That's not a number!")
            else:
                break
        selection = int(selection)-1
        km_flown += round(calculate_distance(current, closest[selection]))
        current = closest[selection]


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
    return distance.distance(a, b).km


def get_airports_radius(current, radius_km):
    airports = get_airports()
    out = []
    for i in airports:
        dist = calculate_distance(current, i)
        if dist < radius_km and current["name"] != i["name"]:
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

    # Palauta lista
    return airports


# Hae tietokannasta maan nimi ISO-koodin perusteella
def get_country_by_code(iso):
    sql = f'select name from country where iso_country = "{iso}"'
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0][0]


main()
