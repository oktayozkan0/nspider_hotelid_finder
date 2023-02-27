import requests
import json


while True:
    hotel_name = input("enter a hotel name: ")

    url = "https://urlaub.check24.de/autocompleter"
    params = {
        "v": "2_0_0",
        "callback": "jQuery19104410931914134564_1677499550228",
        "term": hotel_name
    }
    r = requests.get(url=url, params=params)
    start_idx = r.text.find("({")
    data = json.loads(r.text[start_idx+1:-2])
    hotels = data["data"][-1]["data"]

    print("Possible Hotels\n")
    for hotel in hotels:
        print(f'hotel name: {hotel["label"]}\nhotel city: {hotel["cityName"]}\nhotel id: {hotel["id"]}\n')
    print("------------------end------------------")
