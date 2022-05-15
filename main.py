#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from pprint import pprint
from datetime import datetime, timedelta

SHEETY_API = "https://api.sheety.co/ffa7d6acf87154b9924814f0eb95e7ee/flightsApi/sheet1/"

sheety_headers = {
    "Authorization": "Bearer ajsdlkjhlkh3123kj12l3kjl4kj123lk2j"
}

sheety_response = requests.get(url=SHEETY_API, headers=sheety_headers).json()

sheet_data = sheety_response["sheet1"]

cities_without_codes = {}

for item in sheety_response["sheet1"]:
    if item["iataCode"] == "":
        cities_without_codes[item['id']] = item['city']


# print(cities_without_codes)

KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_SEARCH_FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/search"
KIWI_KEY = "Xdwsu-vJ0DgKrVgnw_b2fa0760VvI6Z5"

kiwi_headers = {
    "apikey": "Xdwsu-vJ0DgKrVgnw_b2fa0760VvI6Z5",
}

if cities_without_codes:
    for city in cities_without_codes:
        city_name = cities_without_codes[city]
        city_id = city
        kiwi_params = {
            "term": city_name,
            "location_types": "city"
        }
        kiwi_response = requests.get(url=KIWI_ENDPOINT, params=kiwi_params, headers=kiwi_headers).json()
        city_code = kiwi_response["locations"][0]["code"]
        print(city_code)

        sheety_payload = {
            "sheet1": {
                "iataCode": city_code,
            }
        }

        sheety_edit_row_with_city_code = requests.put(url=f"{SHEETY_API}/{city_id}",
                                                      headers=sheety_headers, json=sheety_payload)
        print(sheety_edit_row_with_city_code)


all_cities_in_sheet = requests.get(url=SHEETY_API, headers=sheety_headers).json()["sheet1"]

all_city_codes = []

for city in all_cities_in_sheet:
    all_city_codes.append(city["iataCode"])

# print(all_city_codes)

def search_flights(all_city_codes, tomorrow, six_month_from_today):

    for city in all_city_codes:
        from_time = tomorrow
        to_time = six_month_from_today

        flight_params = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(url=KIWI_SEARCH_FLIGHT_ENDPOINT, params=flight_params, headers=kiwi_headers).json()
        try:
            flight_details = f"{response['data'][0]['cityTo']} £{response['data'][0]['price']}"
            print(flight_details)

            sheety_response = requests.get(url=SHEETY_API, headers=sheety_headers).json()



        except IndexError:
            print("No flights found. ")


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

search_flights(all_city_codes, tomorrow, six_month_from_today)





