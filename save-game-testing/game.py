# Tallenna ja lataa peli tietokannasta
# Tästä siis sovitetaan pääprojektiin jos ehtii/jaksaa


import mysql.connector
import random
from geopy import distance

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="",
    password="",
    autocommit=True
)


def main():
    # LOGIN, UUSI/LATAA PELI
    username = input("Anna käyttäjä: ")
    all_airports = get_all_airports()

    hki = {
        "latitude": 60.3172,
        "longitude": 24.963301
    }

    # Pelaajan oletusmuuttujat
    player = {
        "name": username,
        "airport": random.choice(all_airports),
        "money": 10000,
        "distance_to_helsinki": -1,
    }
    player["distance_to_helsinki"] = calculate_distance(player["airport"], hki)

    data = get_player_data(username)
    if data:
        selection = input("Uusi peli vai lataa edellinen? (uusi/lataa): ").lower()
        while selection not in ["uusi", "lataa"]:
            selection = input("Uusi peli vai lataa edellinen? (uusi/lataa): ").lower()
        if selection == "lataa":
            player = data
            # Lentokentän nimi -> kenttä-dictionary
            for airport in all_airports:
                if airport["name"] == player["airport"]:
                    player["airport"] = airport
        elif selection == "uusi":
            update_player(player)
    else:
        insert_new_player(player)

    # MAIN LOOP
    while True:
        print(f"\nSijaintisi: {player['airport']['name']}")
        print(f"Olet {player['distance_to_helsinki']} km päässä Helsinki-Vantaalta.")
        print(f"Sinulla on {player['money']} €.")
        print(f"Minne haluat lentää?\n")

        for i in range(len(all_airports)):
            index = f"[{i+1}]"
            print(f"{index:<4} {all_airports[i]['name']:32} ({calculate_distance(player['airport'], all_airports[i])} €)")

        selection = int(input("\nSyötä numero: ")) - 1
        player["money"] -= calculate_distance(player["airport"], all_airports[selection])
        player["airport"] = all_airports[selection]
        player["distance_to_helsinki"] = calculate_distance(player["airport"], hki)

        update_player(player)


def calculate_distance(airport1, airport2):
    a = (airport1["latitude"], airport1["longitude"])
    b = (airport2["latitude"], airport2["longitude"])
    dist = round(distance.distance(a,b).km)
    return dist


def update_player(player):
    sql = f"""
    update test_game
    set airport = '{player["airport"]["name"]}',
    money = {player["money"]},
    distance_to_helsinki = {player["distance_to_helsinki"]}
    where name = '{player["name"]}'
    """
    cursor = connection.cursor()
    cursor.execute(sql)


def insert_new_player(player):
    sql = f"""
    insert into test_game values
    ('{player["name"]}',
    '{player["airport"]["name"]}',
    {player["money"]},
    {player["distance_to_helsinki"]})
    """
    cursor = connection.cursor()
    cursor.execute(sql)


def get_player_data(username):
    sql = f"""
    select name, airport, money, distance_to_helsinki from test_game
    where name = '{username}'
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    data = {}
    if result:
        data = {
            "name": result[0][0],
            "airport": result[0][1],
            "money": result[0][2],
            "distance_to_helsinki": result[0][3]
        }
    return data


def get_all_airports():
    sql = """
    select name, latitude_deg, longitude_deg from airport
    where iso_country = 'FI'
    and (type = 'large_airport' or type = 'medium_airport')
    """
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    airports = []
    for row in result:
        airport = {
            "name": row[0],
            "latitude": row[1],
            "longitude": row[2],
        }
        airports.append(airport)

    return airports


main()