# Billing calculations for the hotel.

GST_RATE = 0.05


def calculate_bill(price, nights):
    room_charge = price * nights
    tax = room_charge * GST_RATE
    total = room_charge + tax

    return room_charge, tax, total


def money(amount):
    return "Rs. " + format(amount, ",.2f")
