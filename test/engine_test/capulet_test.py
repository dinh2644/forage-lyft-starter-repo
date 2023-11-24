import unittest
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 200000
        last_service_mileage = 150000
        result = CapuletEngine(current_mileage, last_service_mileage)

        self.assertTrue(result.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 200000
        last_service_mileage = 195000
        result = CapuletEngine(current_mileage, last_service_mileage)

        self.assertFalse(result.needs_service())

if __name__ == '__main__':
    unittest.main()