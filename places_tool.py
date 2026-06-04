import json

with open("data/places.json", "r") as f:
    places = json.load(f)


def recommend_places(city):

    filtered = []

    for place in places:

        if place["city"].lower() == city.lower():

            filtered.append(place)

    sorted_places = sorted(
        filtered,
        key=lambda x: x["rating"],
        reverse=True
    )

    return sorted_places[:5]
