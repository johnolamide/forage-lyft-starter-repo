import unittest
from tire.carigan_tire import CariganTire


class TestCariganTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_values = [0, 1, 0.2, 0.5]
        tire = CariganTire(sensor_values)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        sensor_values = [0, 0.1, 0.2, 0.4]
        tire = CariganTire(sensor_values)
        self.assertFalse(tire.needs_service())
