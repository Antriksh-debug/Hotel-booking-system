# Design Diagrams

The following diagrams describe the design of the hotel room booking system. GitHub can render Mermaid diagrams when this file is viewed in a compatible Markdown viewer.

## 1. System Architecture

```mermaid
flowchart TD
    U[Reception Staff / User] --> M[main.py]
    M --> UI[ui.py]
    M --> C[customers.py]
    M --> R[rooms.py]
    M --> B[bookings.py]
    M --> BI[billing.py]
    M --> RP[reports.py]
    M --> V[validation.py]
    M --> DM[data_manager.py]
    DM --> J[(hotel_data.json)]
```

## 2. Workflow Diagram

```mermaid
flowchart TD
    A[Start Program] --> B[Main Menu]
    B --> C{Choose Operation}
    C -->|New Booking| D[Enter Customer Details]
    D --> E[Select Available Room]
    E --> F[Enter Nights and Check-in Date]
    F --> G[Calculate Bill]
    G --> H[Save Booking]
    H --> B
    C -->|Search| I[Find Booking]
    I --> B
    C -->|Cancel| J[Cancel Booking]
    J --> K[Make Room Available]
    K --> B
    C -->|Checkout| L[Select Payment]
    L --> M[Generate Final Bill]
    M --> N[Complete Checkout]
    N --> B
    C -->|Maintenance| O[Update Room Status]
    O --> B
    C -->|Exit| P[Save Data and Exit]
```

## 3. Use Case Diagram

```mermaid
flowchart LR
    User[Reception Staff]
    User --> A((View Rooms))
    User --> B((Find Available Room))
    User --> C((Create Booking))
    User --> D((Search Booking))
    User --> E((Cancel Booking))
    User --> F((Checkout Guest))
    User --> G((Manage Maintenance))
    User --> H((View Dashboard))
    User --> I((View Booking History))
```

## 4. Sequence Diagram - New Booking

```mermaid
sequenceDiagram
    actor User as Reception Staff
    participant Main as main.py
    participant Customer as customers.py
    participant Room as rooms.py
    participant Booking as bookings.py
    participant Bill as billing.py
    participant Store as data_manager.py

    User->>Main: Select New Booking
    Main->>Customer: Get customer details
    Customer-->>Main: Name and phone
    Main->>Room: Check room status
    Room-->>Main: Room available
    Main->>Booking: Create booking
    Booking->>Bill: Calculate bill
    Bill-->>Booking: Charges, GST, total
    Booking-->>Main: Booking created
    Main->>Store: Save booking and room status
    Store-->>Main: Data saved
    Main-->>User: Show confirmation and bill
```

## 5. Component / Module Diagram

```mermaid
flowchart TD
    Main[main.py]
    Main --> UI[ui.py]
    Main --> Rooms[rooms.py]
    Main --> Customers[customers.py]
    Main --> Bookings[bookings.py]
    Main --> Billing[billing.py]
    Main --> Reports[reports.py]
    Main --> Validation[validation.py]
    Main --> Data[data_manager.py]
    Data --> JSON[(hotel_data.json)]
```

## 6. Storage / ER-style Diagram

```mermaid
erDiagram
    ROOM {
        int room_no PK
        string type
        int price
        int capacity
        string status
    }

    BOOKING {
        int booking_id PK
        string customer_name
        string phone
        int room_no FK
        string room_type
        int guests
        int nights
        string check_in
        float room_charge
        float tax
        float total
        string status
        string payment
    }

    ROOM ||--o{ BOOKING : "has"
```
