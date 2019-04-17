# skylines api stuff
import requests
import json


def get_flights_by_airport(airport_number):
        answer = requests.get('https://skylines.aero/api/flights/airport/451')
        # data = json.loads(answer.content)
        # data = json.loads(answer.text)
        data = json.loads(answer.text)
        flights = data["flights"]
        return flights[:5]

