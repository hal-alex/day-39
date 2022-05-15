import requests

KIWI_ENDPOINT = "https://tequila-api.kiwi.com/location/query"
KIWI_KEY = "Xdwsu-vJ0DgKrVgnw_b2fa0760VvI6Z5"


class FlightSearch:

    def get_iata_code(self, city_name):
        self.city = city_name
        list_of_cities = []
        list_of_cities.append(self.city)
        return list_of_cities
