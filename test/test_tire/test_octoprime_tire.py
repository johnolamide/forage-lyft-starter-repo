import unittest
from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_values = [0.7, 0.5, 1, 0.9]
        tire = OctoprimeTire(sensor_values)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        sensor_values = [0, 0.1, 0.4, 0.2]
        tire = OctoprimeTire(sensor_values)
        self.assertFalse(tire.needs_service())
