import random
import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="",
    password="",
    autocommit=True
)

player = {}
enemy = {}


def main():
    current = random.choice(get_airports())

    while True:
        print(f"\nWelcome to {current['country']}! You are currently at {current['name']}.\n")
        print("Where would you like to fly next?\n")

        closest = get_closest_airports(current, 10)
        i = 1
        for airport in closest:
            dist = round(calculate_distance(current, airport))
            print(f"[{i}] {airport['name']} ({airport['country']}) (Distance: {dist} km)")
            i += 1

        current = closest[int(input("\nEnter a number to continue: "))-1]


def get_closest_airports(current, count):
    airports = get_airports()
    airports.sort(key=lambda d: calculate_distance(current, d))
    return airports[1:count+1]


def calculate_distance(current, target):
    a = (current["latitude"], current["longitude"])
    b = (target["latitude"], target["longitude"])
    return distance.distance(a, b).km


def get_airports():
    sql = "select name, latitude_deg, longitude_deg, iso_country from airport where continent='EU' and type='large_airport'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    airports = []
    for i in result:
        airport = {
            "name": i[0],
            "latitude": i[1],
            "longitude": i[2],
            "country": get_country_by_code(i[3]),
        }
        airports.append(airport)

    return airports


def get_country_by_code(iso):
    sql = f'select name from country where iso_country = "{iso}"'
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0][0]


main()
