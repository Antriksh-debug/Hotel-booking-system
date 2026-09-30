# Room related functions are kept in this file.

ROOMS = {
    101: {"type": "Single", "price": 1500, "capacity": 1, "status": "Available"},
    102: {"type": "Single", "price": 1500, "capacity": 1, "status": "Available"},
    103: {"type": "Single", "price": 1500, "capacity": 1, "status": "Available"},
    201: {"type": "Double", "price": 2500, "capacity": 2, "status": "Available"},
    202: {"type": "Double", "price": 2500, "capacity": 2, "status": "Available"},
    203: {"type": "Double", "price": 2500, "capacity": 2, "status": "Available"},
    301: {"type": "Deluxe", "price": 3500, "capacity": 4, "status": "Available"},
    302: {"type": "Deluxe", "price": 3500, "capacity": 4, "status": "Available"},
    303: {"type": "Deluxe", "price": 3500, "capacity": 4, "status": "Available"},
    401: {"type": "Suite", "price": 5000, "capacity": 5, "status": "Available"},
    402: {"type": "Suite", "price": 5000, "capacity": 5, "status": "Available"},
    403: {"type": "Suite", "price": 5000, "capacity": 5, "status": "Available"}
}


def get_room(room_no):
    return ROOMS.get(room_no)


def get_all_rooms():
    return ROOMS


def get_available_rooms(room_type="All"):
    available = []

    for room_no in sorted(ROOMS):
        room = ROOMS[room_no]

        if room["status"] == "Available":
            if room_type == "All" or room["type"] == room_type:
                available.append((room_no, room))

    return available


def set_room_status(room_no, status):
    if room_no in ROOMS:
        ROOMS[room_no]["status"] = status
        return True

    return False


def update_room_status(bookings):
    # Reset normal rooms first. Maintenance rooms stay in maintenance.
    for room_no in ROOMS:
        if ROOMS[room_no]["status"] != "Maintenance":
            ROOMS[room_no]["status"] = "Available"

    for booking in bookings:
        if booking["status"] == "Active":
            room_no = booking["room"]
            if room_no in ROOMS:
                ROOMS[room_no]["status"] = "Booked"
