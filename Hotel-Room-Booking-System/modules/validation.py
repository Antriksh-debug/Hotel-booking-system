# Small input checking functions.

from datetime import datetime


def valid_name(name):
    return name.strip() != ""


def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def valid_positive_number(value):
    return value.isdigit() and int(value) > 0


def valid_date(date_text):
    try:
        datetime.strptime(date_text, "%d-%m-%Y")
        return True
    except ValueError:
        return False


def get_phone_input(input_function=input):
    while True:
        phone = input_function("Phone number : ").strip()

        if valid_phone(phone):
            return phone

        print("Please enter a valid 10 digit phone number.")


def get_positive_input(message, input_function=input):
    while True:
        value = input_function(message).strip()

        if valid_positive_number(value):
            return int(value)

        print("Please enter a valid positive number.")


def get_date_input(input_function=input):
    while True:
        date_text = input_function("Check-in date (DD-MM-YYYY) : ").strip()

        if valid_date(date_text):
            return date_text

        print("Invalid date. Example: 10-10-2026")
