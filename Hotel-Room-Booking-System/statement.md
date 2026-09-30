# Project Statement

## Project Title

Aurora Grand Hotel - Room Booking Management System

## Problem Statement

Small hotels need to keep track of available rooms, customer information, bookings, payments and room status. Handling these tasks manually can make searching and updating information slower and can lead to mistakes.

This project creates a Python-based hotel room booking management system that keeps these activities in one simple application.

## Scope of the Project

The system covers room availability, customer information, room booking, booking search, cancellation, checkout, payment selection, room maintenance, billing and booking history.

The project is designed as a local console application and stores its data in a JSON file.

## Target Users

- Hotel reception staff
- Hotel administrators
- Small hotel operators

## High-Level Features

1. Room management
2. Customer management
3. Booking management
4. Billing and payment
5. Reports and dashboard
6. Data storage
7. Input validation and error handling

## Functional Requirements

### FR1 - Room Management
The system shall display room number, room type, price, capacity and current status.

### FR2 - Room Search
The system shall allow the user to find available rooms by room type.

### FR3 - Customer Management
The system shall collect and validate customer name and phone number.

### FR4 - Booking Management
The system shall create bookings, generate booking IDs and store booking details.

### FR5 - Booking Search
The system shall search bookings using booking ID, customer name or phone number.

### FR6 - Cancellation
The system shall allow active bookings to be cancelled and make the room available again.

### FR7 - Checkout
The system shall calculate the final bill, record payment method and complete checkout.

### FR8 - Maintenance
The system shall allow staff to mark available rooms as under maintenance.

### FR9 - Reporting
The system shall show dashboard statistics such as available rooms, booked rooms, occupancy and collected money.

### FR10 - Storage
The system shall save project data to a JSON file so data is available after restarting the program.

## Non-Functional Requirements

### Usability
The terminal menu should be easy to understand and should clearly show available operations.

### Reliability
Booking and room status changes should remain consistent when the program is running and after data is saved.

### Maintainability
The project is separated into modules so room, booking, billing, validation, reporting, storage and user-interface code can be updated separately.

### Error Handling
The system should validate common user inputs such as room numbers, phone numbers, dates and numeric values and show a useful message instead of stopping unexpectedly.

### Performance
The project should respond quickly for the small hotel dataset used by the application.

## Major Modules

- `rooms.py` - room details, availability and maintenance
- `customers.py` - customer information
- `bookings.py` - booking, search, cancellation and checkout logic
- `billing.py` - bill and GST calculation
- `reports.py` - dashboard and history data
- `data_manager.py` - JSON storage
- `validation.py` - input validation
- `ui.py` - terminal interface
- `main.py` - connects all modules and runs the application

## Storage Design

The system uses a JSON file containing two main parts:

```text
hotel_data.json
|
+-- rooms
|   +-- room number
|       +-- type
|       +-- price
|       +-- capacity
|       +-- status
|
+-- bookings
    +-- id
    +-- name
    +-- phone
    +-- room
    +-- room_type
    +-- guests
    +-- nights
    +-- check_in
    +-- room_charge
    +-- tax
    +-- total
    +-- status
    +-- payment
```

## Testing Approach

The project uses Python's built-in `unittest` framework.

Test cases cover:

- Bill calculation
- Booking creation
- Booking search
- Booking cancellation
- Checkout
- Phone number validation
- Date validation

## Project Boundaries

This is a local academic project. It does not include online room availability, multiple hotels, real payment processing, cloud storage or a web/mobile interface.
