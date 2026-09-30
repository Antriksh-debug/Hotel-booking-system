# Main program for the hotel room booking system.

from modules import rooms
from modules import customers
from modules import bookings as booking_module
from modules import reports
from modules import billing
from modules import data_manager
from modules import validation
from modules import ui


HOTEL_NAME = "AURORA GRAND HOTEL"
DATA_FILE = "data/hotel_data.json"


def save_current_data():
    data_manager.save_data(
        DATA_FILE,

        rooms.get_all_rooms(),
        booking_list
    )


def print_booking_bill(booking):
    print("\n" + ui.GREEN + "*" * 62 + ui.RESET)
    print(ui.BOLD + "                         BOOKING CONFIRMED" + ui.RESET)
    print(ui.GREEN + "*" * 62 + ui.RESET)

    print("Booking ID      :", booking["id"])
    print("Customer        :", booking["name"])
    print("Room            :", booking["room"])
    print("Room Type       :", booking["room_type"])
    print("Check-in        :", booking["check_in"])
    print("Number of days  :", booking["nights"])
    print("Guests          :", booking["guests"])

    ui.line()

    print("Room Charges    :", billing.money(booking["room_charge"]))
    print("GST (5%)        :", billing.money(booking["tax"]))
    print(ui.BOLD + "Total Amount    : " + billing.money(booking["total"]) + ui.RESET)


def new_booking():
    ui.title("NEW BOOKING")

    print("Enter customer details")
    ui.line()

    customer = customers.get_customer_details()



    ui.show_rooms(rooms.get_all_rooms())
    print()

    room_input = input("Enter room number : ").strip()

    if room_input.isdigit() is False:
        print(ui.RED + "Invalid room number." + ui.RESET)
        return

    room_no = int(room_input)
    room = rooms.get_room(room_no)

    if room is None:
        print(ui.RED + "Room does not exist." + ui.RESET)
        return

    if room["status"] != "Available":
        print(ui.RED + "Sorry, this room is not available." + ui.RESET)
        return

    guests = validation.get_positive_input("Number of guests : ")

    if guests > room["capacity"]:
        print(ui.RED + "Too many guests for this room." + ui.RESET)
        return

    nights = validation.get_positive_input("Number of nights : ")
    check_in = validation.get_date_input()

    booking, message = booking_module.create_booking(
        booking_list,
        rooms.get_all_rooms(),
        customer,
        room_no,
        guests,
        nights,
        check_in
    )

    if booking is False:
        print(ui.RED + message + ui.RESET)
        return

    save_current_data()
    print_booking_bill(booking)
    print(ui.GREEN + "\nBooking saved successfully!" + ui.RESET)


def find_available_room():
    ui.title("SEARCH AVAILABLE ROOM")

    print("1. Single")
    print("2. Double")
    print("3. Deluxe")
    print("4. Suite")

    print("5. Show all")

    choice = input("\nChoose room type : ").strip()

    room_types = {
        "1": "Single",
        "2": "Double",
        "3": "Deluxe",
        "4": "Suite",
        "5": "All"
    }

    if choice not in room_types:
        print(ui.RED + "Wrong choice." + ui.RESET)
        return

    selected_type = room_types[choice]
    available = rooms.get_available_rooms(selected_type)

    print("\nAvailable rooms:\n")

    if len(available) == 0:
        print(ui.RED + "No room is available in this category." + ui.RESET)
        return

    for room_no, room in available:
        print(
            ui.GREEN +
            "Room {} | {} | {} per day | {} person(s)".format(
                room_no,
                room["type"],
                billing.money(room["price"]),


                room["capacity"]
            ) +
            ui.RESET
        )


def show_active_bookings():
    ui.title("CURRENT BOOKINGS")

    found = False

    for booking in booking_list:
        if booking["status"] == "Active":
            ui.show_booking(booking)
            found = True



    if found is False:
        print(ui.YELLOW + "There are no active bookings." + ui.RESET)


def search_booking():
    ui.title("SEARCH BOOKING")

    print("1. Search using Booking ID")
    print("2. Search using Customer Name")
    print("3. Search using Phone Number")

    choice = input("\nChoose : ").strip()
    results = []

    if choice == "1":
        value = input("Enter booking ID : ").strip()

        if value.isdigit():
            result = booking_module.search_by_id(booking_list, int(value))
            if result is not None:
                results.append(result)
        else:
            print(ui.RED + "Invalid booking ID." + ui.RESET)
            return

    elif choice == "2":
        value = input("Enter customer name : ").strip()
        results = booking_module.search_by_name(booking_list, value)

    elif choice == "3":
        value = input("Enter phone number : ").strip()
        results = booking_module.search_by_phone(booking_list, value)

    else:

        print(ui.RED + "Invalid option." + ui.RESET)
        return

    if len(results) == 0:
        print(ui.RED + "\nNo booking found." + ui.RESET)
        return

    for booking in results:
        ui.show_booking(booking)


def cancel_booking():
    ui.title("CANCEL BOOKING")

    value = input("Enter booking ID : ").strip()

    if value.isdigit() is False:
        print(ui.RED + "Invalid booking ID." + ui.RESET)
        return

    booking = booking_module.search_by_id(booking_list, int(value))

    if booking is None:
        print(ui.RED + "Booking ID not found." + ui.RESET)
        return

    ui.show_booking(booking)

    if booking["status"] != "Active":
        print(ui.YELLOW + "This booking is already closed." + ui.RESET)
        return

    confirm = input("Do you really want to cancel it? (yes/no) : ").lower()

    if confirm != "yes":
        print(ui.YELLOW + "Booking was not cancelled." + ui.RESET)
        return

    success, message = booking_module.cancel_booking(
        booking_list,
        rooms.get_all_rooms(),

        int(value)
    )

    if success:
        save_current_data()
        print(ui.GREEN + message + ui.RESET)
    else:
        print(ui.RED + message + ui.RESET)


def checkout():
    ui.title("GUEST CHECKOUT")

    value = input("Enter booking ID : ").strip()

    if value.isdigit() is False:
        print(ui.RED + "Invalid booking ID." + ui.RESET)
        return

    booking = booking_module.search_by_id(booking_list, int(value))

    if booking is None:
        print(ui.RED + "Booking not found." + ui.RESET)
        return

    if booking["status"] != "Active":
        print(ui.YELLOW + "This booking is already closed." + ui.RESET)
        return

    print("\nGuest details:")
    ui.show_booking(booking)

    print("\nPayment Method")
    print("1. Cash")
    print("2. UPI")
    print("3. Card")


  
    payment_choice = input("\nChoose payment method : ").strip()

    payments = {
        "1": "Cash",
        "2": "UPI",
        "3": "Card"
    }

    if payment_choice not in payments:
        print(ui.RED + "Invalid payment option." + ui.RESET)
        return

    print("\n" + ui.BLUE + "=" * 45 + ui.RESET)
    print(ui.BOLD + "                 FINAL BILL" + ui.RESET)
    print(ui.BLUE + "=" * 45 + ui.RESET)

    print("Hotel        :", HOTEL_NAME)
    print("Booking ID   :", booking["id"])
    print("Customer     :", booking["name"])
    print("Room         :", booking["room"])
    print("Room Charge  :", billing.money(booking["room_charge"]))
    print("GST          :", billing.money(booking["tax"]))
    print(ui.BOLD + "Total        : " + billing.money(booking["total"]) + ui.RESET)
    print("Payment      :", payments[payment_choice])
    print(ui.BLUE + "=" * 45 + ui.RESET)

    confirm = input("\nConfirm checkout? (yes/no) : ").lower()

    if confirm != "yes":
        print(ui.YELLOW + "Checkout cancelled." + ui.RESET)
        return

    success, message = booking_module.checkout_booking(
        booking_list,
        rooms.get_all_rooms(),
        int(value),
        payments[payment_choice]
    )

    if success:
        save_current_data()
        print(ui.GREEN + "\n" + message + ui.RESET)
    else:
        print(ui.RED + message + ui.RESET)


def room_maintenance():
    ui.title("ROOM MAINTENANCE")

    value = input("Enter room number : ").strip()

    if value.isdigit() is False:
        print(ui.RED + "Invalid room number." + ui.RESET)
        return

    room_no = int(value)
    room = rooms.get_room(room_no)

    if room is None:
        print(ui.RED + "Room does not exist." + ui.RESET)
        return

    if room["status"] == "Booked":
        print(ui.RED + "A booked room cannot be put under maintenance." + ui.RESET)
        return

    print("\nCurrent status :", room["status"])
    print("\n1. Put room under maintenance")
    print("2. Make room available")

    choice = input("\nChoose : ").strip()

    if choice == "1":
        rooms.set_room_status(room_no, "Maintenance")
        print(ui.YELLOW + "Room marked for maintenance." + ui.RESET)

    elif choice == "2":
        rooms.set_room_status(room_no, "Available")
        print(ui.GREEN + "Room is available again." + ui.RESET)

    else:
        print(ui.RED + "Wrong choice." + ui.RESET)
        return


    save_current_data()


def show_dashboard():
    ui.title("HOTEL DASHBOARD")

    data = reports.get_dashboard(
        rooms.get_all_rooms(),
        booking_list
    )

    print("\nTotal Rooms       :", data["total_rooms"])
    print(ui.GREEN + "Available Rooms   : {}".format(data["available"]) + ui.RESET)
    print(ui.RED + "Booked Rooms      : {}".format(data["booked"]) + ui.RESET)
    print(ui.YELLOW + "Under Maintenance : {}".format(data["maintenance"]) + ui.RESET)

    print("\nActive Bookings   :", data["active"])
    print("Checked Out       :", data["checked_out"])
    print("Cancelled         :", data["cancelled"])

    print("\nOccupancy Rate    : {:.1f}%".format(data["occupancy"]))
    print("Money Collected   :", ui.GREEN + billing.money(data["collected"]) + ui.RESET)


def booking_history():
    ui.title("BOOKING HISTORY")

    if len(booking_list) == 0:
        print(ui.YELLOW + "No booking history yet." + ui.RESET)
        return

    print("{:<10} {:<20} {:<10} {:<18} {}".format(
        "ID", "Customer", "Room", "Status", "Amount"
    ))
    ui.line()

    for booking in reports.get_booking_history(booking_list):
        print("{:<10} {:<20} {:<10} {:<18} {}".format(
            booking["id"],
            booking["name"][:20],
            booking["room"],
            booking["status"],
            billing.money(booking["total"])
        ))


def main_menu():
    while True:
        ui.header(HOTEL_NAME)

        dashboard_data = reports.get_dashboard(
            rooms.get_all_rooms(),
            booking_list
        )

        print(
            "   " +
            ui.GREEN + str(dashboard_data["available"]) + " Available" + ui.RESET +
            "       " +
            ui.RED + str(dashboard_data["booked"]) + " Booked" + ui.RESET
        )

        print("\n" + ui.BOLD + "                     MAIN MENU" + ui.RESET)

        print("""
        [1]  Hotel Dashboard
        [2]  View All Rooms
        [3]  Find Available Room
        [4]  New Booking
        [5]  Current Bookings
        [6]  Search Booking
        [7]  Cancel Booking
        [8]  Guest Checkout
        [9]  Room Maintenance
        [10] Booking History

        [0]  Exit
        """)

        choice = input("        Enter choice : ").strip()

        if choice == "1":
            ui.clear_screen()
            show_dashboard()
            ui.pause()

        elif choice == "2":
            ui.clear_screen()
            ui.show_rooms(rooms.get_all_rooms())
            ui.pause()

        elif choice == "3":
            ui.clear_screen()
            find_available_room()
            ui.pause()

        elif choice == "4":

            ui.clear_screen()
            new_booking()
            ui.pause()

        elif choice == "5":
            ui.clear_screen()
            show_active_bookings()
            ui.pause()

        elif choice == "6":

            ui.clear_screen()
            search_booking()
            ui.pause()

        elif choice == "7":
            ui.clear_screen()
            cancel_booking()
            ui.pause()

        elif choice == "8":
            ui.clear_screen()
            checkout()
            ui.pause()

        elif choice == "9":
            ui.clear_screen()
            room_maintenance()
            ui.pause()

        elif choice == "10":
            ui.clear_screen()
            booking_history()
            ui.pause()

        elif choice == "0":
            save_current_data()
            ui.clear_screen()
            print("\n" + ui.GREEN + "Thank you for visiting " + HOTEL_NAME + "!" + ui.RESET)
            print("                  Have a nice day :)\n")
            break

        else:
            print(ui.RED + "\n        Invalid choice. Try again." + ui.RESET)
            ui.pause()


# A list is kept here so all modules work with the same booking data.
loaded_rooms, booking_list = data_manager.load_data(DATA_FILE, rooms.get_all_rooms())
rooms.ROOMS.clear()
rooms.ROOMS.update(loaded_rooms)
rooms.update_room_status(booking_list)


if __name__ == "__main__":
    main_menu()
