import requests
import json


while True:
    hotel_name = input("enter a hotel name: ")
    url = "https://www.holidaycheck.de/svc/search-mixer/search"
    params = {
        "query": hotel_name,
        "tenant": "hc-search",
        "page": "/",
        "scope": "hotel",
        "travelkind": "hotel"
    }
    r = requests.get(url=url, params=params)
    data = json.loads(r.text)
    hotels = data["transformedResults"]
    print("Possible Hotels\n")
    for i,hotel in enumerate(hotels[:-1]):
        if hotel["kind"] != "hotel":
            continue
        hotel_city = hotel["description"].replace("<strong>", "").replace("</strong>", "")
        print(f'hotel name: {hotel["originalName"]}\nhotel city: {hotel_city}\nhotel id: {hotel["id"]}\n')
