import json

with open("data/flights.json", "r") as f:
    flights = json.load(f)


def search_flights(source, destination):

    results = []

    for flight in flights:

        if (
            flight["from"].lower() == source.lower()
            and flight["to"].lower() == destination.lower()
        ):
            results.append(flight)

    if not results:
        return "No flights found"

    cheapest = min(results, key=lambda x: x["price"])

    return cheapest



