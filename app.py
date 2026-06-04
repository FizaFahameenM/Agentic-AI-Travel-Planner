import streamlit as st

from tools.flight_tool import search_flights
from tools.hotel_tool import recommend_hotels
from tools.places_tool import recommend_places
from tools.budget_tool import calculate_budget
from tools.weather_tool import get_weather


st.title("✈️ AI Travel Planner")


source = st.text_input("Enter Source City")

destination = st.text_input("Enter Destination City")

days = st.slider("Number of Days", 1, 7)

budget_limit = st.number_input("Enter Budget")


# Generate Day-wise Itinerary
def generate_itinerary(places, days):

    itinerary = {}

    places_per_day = max(1, len(places) // days)

    index = 0

    for day in range(1, days + 1):

        itinerary[f"Day {day}"] = []

        for _ in range(places_per_day):

            if index < len(places):

                itinerary[f"Day {day}"].append(
                    places[index]["name"]
                )

                index += 1

    return itinerary


# Button Click
if st.button("Generate Travel Plan"):

    with st.spinner("Generating AI Travel Plan..."):

        # Flight Search
        flight = search_flights(source, destination)

        # Error Handling for Flight
        if not flight:
            st.error("No flights found")
            st.stop()

        # Hotel Search
        hotels = recommend_hotels(destination, budget_limit)

        # Error Handling for Hotels
        if not hotels:
            st.error("No hotels found")
            st.stop()

        # Places Search
        places = recommend_places(destination)

        # Error Handling for Places
        if not places:
            st.error("No tourist places found")
            st.stop()

        # Generate itinerary
        itinerary = generate_itinerary(places, days)

        # Weather
        weather = get_weather(19.0760, 72.8777)

        # Budget
        budget = calculate_budget(
            flight["price"],
            hotels[0]["price_per_night"] * days,
            days
        )

        st.success("Trip Plan Generated Successfully ✈️")

        # Flight Details
        st.header("✈️ Flight Details")

        st.write(f"Airline: {flight['airline']}")
        st.write(f"From: {flight['from']}")
        st.write(f"To: {flight['to']}")
        st.write(f"Price: ₹{flight['price']}")

        # Hotel Details
        st.header("🏨 Recommended Hotel")

        best_hotel = hotels[0]

        st.write(f"Hotel Name: {best_hotel['name']}")
        st.write(f"City: {best_hotel['city']}")
        st.write(f"Stars: ⭐ {best_hotel['stars']}")
        st.write(f"Price Per Night: ₹{best_hotel['price_per_night']}")

        # Itinerary
        st.header("🗓 Day-wise Itinerary")

        for day, activities in itinerary.items():

            st.subheader(day)

            for activity in activities:

                st.write(f"📍 {activity}")

        # Weather Forecast
        st.header("🌤 Weather Forecast")

        for i, temp in enumerate(weather[:days]):

            st.write(f"Day {i+1}: {temp}°C")

        # Budget Breakdown
        st.header("💰 Budget Breakdown")

        st.write(f"Flight Cost: ₹{budget['flight_cost']}")
        st.write(f"Hotel Cost: ₹{budget['hotel_cost']}")
        st.write(f"Local Expenses: ₹{budget['local_expense']}")

        st.success(f"Total Estimated Budget: ₹{budget['total_budget']}")

        # AI Summary
        st.header("🤖 AI Travel Summary")

        summary = f"""
        Your {days}-day trip from {source} to {destination} includes comfortable accommodation,
        popular tourist attractions, weather forecasting, and optimized budget planning.

        The trip is designed to give a balanced experience of sightseeing,
        relaxation, and local exploration while staying within your specified budget.
        """

        st.write(summary)