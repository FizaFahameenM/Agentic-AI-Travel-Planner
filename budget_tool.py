def calculate_budget(flight_price, hotel_price, days):

    local_expense = days * 1000

    total = (
        flight_price
        + hotel_price
        + local_expense
    )

    return {
        "flight_cost": flight_price,
        "hotel_cost": hotel_price,
        "local_expense": local_expense,
        "total_budget": total
    }
