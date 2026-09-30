# All terminal UI related functions are kept here.

import os

RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def line():
    print(CYAN + "-" * 70 + RESET)


def title(text):
    print("\n" + CYAN + "=" * 70 + RESET)
    print(BOLD + " " + text.center(68) + RESET)
    print(CYAN + "=" * 70 + RESET)


def header(hotel_name):
    clear_screen()

    print(CYAN + "=" * 70 + RESET)
    print(BOLD + BLUE)
    print("                    A U R O R A   G R A N D")
    print("                          H O T E L")
    print(RESET + CYAN + "=" * 70 + RESET)
    print("                 HOTEL ROOM BOOKING SYSTEM")
    print()


def room_status(status):
    if status == "Available":
        return GREEN + "Available" + RESET
    elif status == "Booked":
        return RED + "Booked" + RESET
    else:
        return YELLOW + "Maintenance" + RESET


def show_rooms(rooms):
    title("ROOM DETAILS")

    print()
    print("Room      Type        Price/Day        Capacity       Status")
    line()

    for room_no in sorted(rooms):
        room = rooms[room_no]

        print("{:<9} {:<11} {:<16} {:<14} {}".format(
            room_no,
            room["type"],
            "Rs. " + format(room["price"], ",.2f"),
            str(room["capacity"]) + " person",
            room_status(room["status"])
        ))


def show_booking(booking):
    line()

    print("Booking ID     :", booking["id"])
    print("Customer       :", booking["name"])
    print("Phone          :", booking["phone"])
    print("Room           :", booking["room"])
    print("Room Type      :", booking["room_type"])
    print("Guests         :", booking["guests"])
    print("Nights         :", booking["nights"])
    print("Check-in       :", booking["check_in"])
    print("Total          : Rs. " + format(booking["total"], ",.2f"))
    print("Status         :", booking["status"])
    print("Payment        :", booking["payment"])

    line()
