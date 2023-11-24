import unittest
from datetime import date,timedelta
from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days = 365 *5)
        result = NubbinBattery(current_date, last_service_date)

        self.assertTrue(result.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.today()
        last_service_date = current_date - timedelta(days = 365 *3)
        result = NubbinBattery(current_date, last_service_date)

        self.assertFalse(result.needs_service())

if __name__ == '__main__':
    unittest.main()