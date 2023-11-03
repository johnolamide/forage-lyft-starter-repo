from tire import Tire


class OctoprimeTire(Tire):

    def __init__(self, sensor_values):
        self.sensor_values = sensor_values

    def needs_service(self):
        values_sum = 0
        for value in self.sensor_values:
            values_sum += value
        if values_sum >= 3:
            return True
        else:
            return False
