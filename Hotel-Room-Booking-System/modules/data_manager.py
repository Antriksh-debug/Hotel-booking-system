# This file saves and loads the project data.

import json
import os


def save_data(file_name, rooms, bookings):
    data = {
        "rooms": rooms,
        "bookings": bookings
    }

    try:
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError:
        return False


def load_data(file_name, default_rooms):
    if os.path.exists(file_name) is False:
        return default_rooms.copy(), []

    try:
        with open(file_name, "r") as file:
            data = json.load(file)

        loaded_rooms = default_rooms.copy()
        saved_rooms = data.get("rooms", {})

        for room_no in saved_rooms:
            loaded_rooms[int(room_no)] = saved_rooms[room_no]

        bookings = data.get("bookings", [])

        return loaded_rooms, bookings

    except (OSError, json.JSONDecodeError, ValueError):
        return default_rooms.copy(), []
