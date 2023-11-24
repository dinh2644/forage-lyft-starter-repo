import unittest
from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        result = SternmanEngine(warning_light_is_on)

        self.assertTrue(result.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        result = SternmanEngine(warning_light_is_on)

        self.assertFalse(result.needs_service())
