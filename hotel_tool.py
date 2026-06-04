import json

with open("data/hotels.json", "r") as f:
    hotels = json.load(f)


def recommend_hotels(city, budget):

    filtered = []

    for hotel in hotels:

        if (
            hotel["city"].lower() == city.lower()
            and hotel["price_per_night"] <= budget
        ):

            filtered.append(hotel)

    sorted_hotels = sorted(
        filtered,
        key=lambda x: x["stars"],
        reverse=True
    )

    return sorted_hotels[:3]
