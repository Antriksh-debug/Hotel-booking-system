from modules.billing import calculate_bill

def create_booking(bookings, rooms, customer, room_no, guests, nights, check_in):
    if room_no not in rooms:
        return False, "Room does not exist."

    if rooms[room_no]["status"] != "Available":
        return False, "Room is not available."

    if guests > rooms[room_no]["capacity"]:
        return False, "Too many guests for this room."

    room_charge, tax, total = calculate_bill(

        rooms[room_no]["price"], nights

    )

    if len(bookings) == 0:
        booking_id = 1001
    else:
        booking_id = max(item["id"] for item in bookings) + 1

    booking = {
        "id": booking_id,
        "name": customer["name"],
        "phone": customer["phone"],
        "room": room_no,
        "room_type": rooms[room_no]["type"],
        "guests": guests,
        "nights": nights,
        "check_in": check_in,
        "room_charge": room_charge,
        "tax": tax,
        "total": total,
        "status": "Active",
        "payment": "Pending"
    }

    bookings.append(booking)
    rooms[room_no]["status"] = "Booked"

    return booking, "Booking created."

def search_by_id(bookings, booking_id):

    for booking in bookings:
        if booking["id"] == booking_id:
            return booking

    return None

def search_by_name(bookings, name):

    result = []
    name = name.lower()

    for booking in bookings:
        if name in booking["name"].lower():
            result.append(booking)

    return result

def search_by_phone(bookings, phone):

    result = []

    for booking in bookings:
        if booking["phone"] == phone:
            result.append(booking)

    return result

def cancel_booking(bookings, rooms, booking_id):

    booking = search_by_id(bookings, booking_id)

    if booking is None:
        return False, "Booking not found."

    if booking["status"] != "Active":
        return False, "This booking is already closed."

    booking["status"] = "Cancelled"
    booking["payment"] = "Not Applicable"

    rooms[booking["room"]]["status"] = "Available"

    return True, "Booking cancelled successfully."

def checkout_booking(bookings, rooms, booking_id, payment):

    booking = search_by_id(bookings, booking_id)

    if booking is None:
        return False, "Booking not found."

    if booking["status"] != "Active":
        return False, "This booking is already closed."

    booking["status"] = "Checked Out"
    booking["payment"] = payment

    rooms[booking["room"]]["status"] = "Available"

    return True, "Checkout completed successfully."
