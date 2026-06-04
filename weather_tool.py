import requests


def get_weather(latitude, longitude):

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max&timezone=auto"

    response = requests.get(url)

    data = response.json()

    return data["daily"]["temperature_2m_max"]


weather = get_weather(15.2993, 74.1240)

