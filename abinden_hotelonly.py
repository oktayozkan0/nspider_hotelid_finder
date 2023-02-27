import requests
import json

while True:
    hotel_name = input("enter a hotel name: ")
    url = "https://www.ab-in-den-urlaub.de/ac/autocompletion"
    "originContentThread=start&type=ownarrival&mode=regions&page=0&search=rixos+belek"
    params = {
        "originContentThread": "start",
        "type": "ownarrival",
        "mode": "regions",
        "page": "0",
        "search": hotel_name
    }
    r = requests.get(url=url, params=params)
    hotels = json.loads(r.text)

    print("Possible Hotels\n")
    for hotel in hotels:
        if hotel["type"] != "hotel":
            continue
        print(f'hotel name: {hotel["name"]}\nhotel city: {hotel["cityname"]}\nhotel id: {hotel["id"]}\n')
    print("------------------end------------------")
