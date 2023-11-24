import unittest
from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 200000
        last_service_mileage = 150000
        result = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertTrue(result.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 200000
        last_service_mileage = 195000
        result = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(result.needs_service())
