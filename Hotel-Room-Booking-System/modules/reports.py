# Dashboard and report related functions.


def get_dashboard(rooms, bookings):
    total_rooms = len(rooms)
    available = 0
    booked = 0
    maintenance = 0

    for room_no in rooms:
        status = rooms[room_no]["status"]

        if status == "Available":
            available += 1
        elif status == "Booked":
            booked += 1
        else:
            maintenance += 1

    active = 0
    checked_out = 0
    cancelled = 0
    collected = 0

    for booking in bookings:
        status = booking["status"]

        if status == "Active":
            active += 1
        elif status == "Checked Out":
            checked_out += 1
            collected += booking["total"]
        elif status == "Cancelled":
            cancelled += 1

    if total_rooms == 0:
        occupancy = 0
    else:
        occupancy = (booked / total_rooms) * 100

    return {
        "total_rooms": total_rooms,
        "available": available,
        "booked": booked,
        "maintenance": maintenance,
        "active": active,
        "checked_out": checked_out,
        "cancelled": cancelled,
        "collected": collected,
        "occupancy": occupancy
    }


def get_booking_history(bookings):
    return bookings
