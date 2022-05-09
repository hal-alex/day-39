#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
from pprint import pprint
from flight_search import FlightSearch


sheety_headers = {
    "Authorization": "Bearer ajsdlkjhlkh3123kj12l3kjl4kj123lk2j"
}

# sheety_payload = {
#     "sheet1": {
#         "date": today_date,
#         "time": now_time,
#         "exercise": exercise["name"].title(),
#         "duration": exercise["duration_min"],
#         "calories": exercise["nf_calories"],
#     }
#
# }

sheety_response = requests.get(url=SHEETY_API, headers=sheety_headers).json()
# print(pprint(sheety_response))



for item in sheety_response["sheet1"]:
    search_flight = FlightSearch()
    if item["iataCode"] == "":
        city_name = item["city"]

        search_flight.get_iata_code()



