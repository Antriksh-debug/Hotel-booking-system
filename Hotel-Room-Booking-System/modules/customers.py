# Customer related input is handled here.

from modules.validation import valid_name, get_phone_input


def get_customer_details(input_function=input):
    while True:
        name = input_function("Customer name : ").strip()

        if valid_name(name):
            break

        print("Name cannot be empty.")

    phone = get_phone_input(input_function)

    return {
        "name": name,
        "phone": phone
    }
