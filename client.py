import sys
import requests
import time
from faker import Faker
from random import seed, randint, gauss

seed(1)
fake = Faker()
median = 3
standard_deviation = 0.4

url_from_cli = sys.argv[1] if len(sys.argv) > 1 else None
url = url_from_cli or "http://127.0.0.1:8000/"

def start():
    while True:
        data ={
            "name": fake.name(),
            "blood_pressure": randint(2, 10),
            "sugar_level": randint(6, 14)
        }

        response = requests.post(url, json=data)
        print("Status Code: ", response.status_code)
        print("Response: ", response.json())
        time.sleep(gauss(median, standard_deviation))
