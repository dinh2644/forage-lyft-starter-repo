import unittest
from tires.carrigan import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        wear_sensors = [0.1,0.2,0.3,0.9]
        result = CarriganTires(wear_sensors)

        self.assertTrue(result.needs_service())

    def test_tires_should_not_be_serviced(self):
        wear_sensors = [0.1,0.2,0.1,0.1]
        result = CarriganTires(wear_sensors)

        self.assertFalse(result.needs_service())

if __name__ == '__main__':
    unittest.main()