# Aurora Grand Hotel - Room Booking Management System

## Overview

Aurora Grand Hotel is a Python-based hotel room booking management system made for the VITyarthi Build Your Own Project.

The project provides a simple terminal user interface for managing hotel rooms, customers, bookings, billing and reports.

The project is intentionally built with Python standard-library modules so that the code stays understandable for a first-year programming project.

## Features

- Hotel dashboard
- Room directory
- Search available rooms by room type
- New room booking
- Automatic booking ID generation
- Customer details and validation
- 5% GST bill calculation
- Search booking by ID, name or phone
- Cancel booking
- Guest checkout
- Cash, UPI and card payment choices
- Room maintenance status
- Booking history
- JSON data storage
- Basic automated tests
- Coloured terminal interface

## Technologies Used

- Python 3
- Python `json` module
- Python `os` module
- Python `datetime` module
- Python `unittest` module

No external packages are required.

## Project Structure

```text
Hotel-Room-Booking-System/
|
|-- main.py
|-- modules/
|   |-- __init__.py
|   |-- rooms.py
|   |-- bookings.py
|   |-- customers.py
|   |-- billing.py
|   |-- reports.py
|   |-- data_manager.py
|   |-- validation.py
|   |-- ui.py
|
|-- data/
|   |-- hotel_data.json
|
|-- tests/
|   |-- test_hotel.py
|
|-- docs/
|   |-- design_diagrams.md
|
|-- README.md
|-- statement.md
```

## How to Run

1. Install Python 3.
2. Open the project folder in VS Code or another Python editor.
3. Run:

```bash
python main.py
```

The program creates and updates `data/hotel_data.json` automatically.

## Testing

Run the test file from the project folder:

```bash
python -m unittest discover -s tests -v
```

## Main Workflow

```text
Start
  |
  v
Main Menu
  |
  +---- View Rooms
  |
  +---- Find Available Room
  |
  +---- New Booking --> Customer Details --> Room --> Bill --> Save
  |
  +---- Search Booking
  |
  +---- Cancel Booking --> Free Room --> Save
  |
  +---- Checkout --> Payment --> Free Room --> Save
  |
  +---- Dashboard / History / Maintenance
  |
  v
Exit
```

## Data Storage

The program uses one JSON file for local storage. It stores room information and booking records.

Example booking fields:

```text
id
name
phone
room
room_type
guests
nights
check_in
room_charge
tax
total
status
payment
```

## Future Enhancements

Possible future improvements include a graphical interface, login system, database support, room images, online payment integration and email/SMS confirmation.

## References

- VITyarthi - Build Your Own Project: General Project Instructions & Submission Guidelines.
- Python Standard Library documentation.
