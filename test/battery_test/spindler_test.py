import unittest
from datetime import date,timedelta
from battery.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days = 365 *3)
        result = SpindlerBattery(current_date, last_service_date)

        self.assertTrue(result.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days = 365 *1)
        result = SpindlerBattery(current_date, last_service_date)

        self.assertFalse(result.needs_service())
