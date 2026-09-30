import sys
import unittest

sys.path.insert(0, ".")

from modules.billing import calculate_bill
from modules.bookings import create_booking, search_by_id, cancel_booking, checkout_booking
from modules.validation import valid_phone, valid_date


class HotelSystemTests(unittest.TestCase):

    def setUp(self):
        self.rooms = {
            101: {
                "type": "Single",
                "price": 1500,
                "capacity": 1,
                "status": "Available"
            }
        }
        self.bookings = []

    def test_bill_calculation(self):
        room_charge, tax, total = calculate_bill(1500, 2)

        self.assertEqual(room_charge, 3000)
        self.assertEqual(tax, 150)
        self.assertEqual(total, 3150)

    def test_create_booking(self):
        customer = {
            "name": "Test User",
            "phone": "9876543210"
        }

        booking, message = create_booking(
            self.bookings,
            self.rooms,
            customer,
            101,
            1,
            2,
            "01-10-2026"
        )

        self.assertTrue(booking)
        self.assertEqual(self.rooms[101]["status"], "Booked")
        self.assertEqual(len(self.bookings), 1)

    def test_search_booking(self):
        customer = {
            "name": "Test User",
            "phone": "9876543210"
        }

        booking, message = create_booking(
            self.bookings,
            self.rooms,
            customer,
            101,
            1,
            1,
            "01-10-2026"
        )

        result = search_by_id(self.bookings, booking["id"])
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "Test User")

    def test_cancel_booking(self):
        customer = {
            "name": "Test User",
            "phone": "9876543210"
        }

        booking, message = create_booking(
            self.bookings,
            self.rooms,
            customer,
            101,
            1,
            1,
            "01-10-2026"
        )

        success, message = cancel_booking(
            self.bookings,
            self.rooms,
            booking["id"]
        )

        self.assertTrue(success)
        self.assertEqual(self.rooms[101]["status"], "Available")
        self.assertEqual(self.bookings[0]["status"], "Cancelled")

    def test_checkout(self):
        customer = {
            "name": "Test User",
            "phone": "9876543210"
        }

        booking, message = create_booking(
            self.bookings,
            self.rooms,
            customer,
            101,
            1,
            1,
            "01-10-2026"
        )

        success, message = checkout_booking(
            self.bookings,
            self.rooms,
            booking["id"],
            "UPI"
        )

        self.assertTrue(success)
        self.assertEqual(self.rooms[101]["status"], "Available")
        self.assertEqual(self.bookings[0]["status"], "Checked Out")
        self.assertEqual(self.bookings[0]["payment"], "UPI")

    def test_validation(self):
        self.assertTrue(valid_phone("9876543210"))
        self.assertFalse(valid_phone("12345"))
        self.assertTrue(valid_date("01-10-2026"))
        self.assertFalse(valid_date("99-99-2026"))


if __name__ == "__main__":
    unittest.main()
