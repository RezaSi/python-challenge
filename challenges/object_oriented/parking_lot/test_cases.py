import os
import sys
import unittest

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now you can import the ParkingLot class from solution.py
from solution import ParkingLot

class TestParkingLot(unittest.TestCase):
    def setUp(self):
        self.parking_lot = ParkingLot(5)

    def test_initial_state(self):
        self.assertEqual(self.parking_lot.num_spaces, 5)
        self.assertEqual(self.parking_lot.available_spaces, 5)
        self.assertEqual(self.parking_lot.parked_vehicles, {})

    def test_park_vehicle(self):
        self.assertTrue(self.parking_lot.park_vehicle("ABC123"))
        self.assertEqual(self.parking_lot.available_spaces, 4)
        self.assertIn("ABC123", self.parking_lot.parked_vehicles)

    def test_park_vehicle_full(self):
        for i in range(5):
            self.parking_lot.park_vehicle(f"CAR{i:03}")
        self.assertFalse(self.parking_lot.park_vehicle("EXTRA"))
        self.assertEqual(self.parking_lot.available_spaces, 0)

    def test_remove_vehicle(self):
        self.parking_lot.park_vehicle("DEF456")
        self.assertTrue(self.parking_lot.remove_vehicle("DEF456"))
        self.assertEqual(self.parking_lot.available_spaces, 5)
        self.assertNotIn("DEF456", self.parking_lot.parked_vehicles)

    def test_remove_nonexistent_vehicle(self):
        self.assertFalse(self.parking_lot.remove_vehicle("GHOST"))
        self.assertEqual(self.parking_lot.available_spaces, 5)

    def test_get_status(self):
        self.parking_lot.park_vehicle("ABC123")
        self.parking_lot.park_vehicle("DEF456")
        available_spaces, parked_vehicles = self.parking_lot.get_status()
        self.assertEqual(available_spaces, 3)
        self.assertCountEqual(parked_vehicles, ["ABC123", "DEF456"])

if __name__ == '__main__':
    unittest.main()