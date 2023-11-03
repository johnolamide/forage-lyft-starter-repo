from tire import Tire


class CarriganTire(Tire):

    def __init__(self, sensor_values):
        self.sensor_values = sensor_values

    def needs_service(self):
        for value in self.sensor_values:
            if value >= 0.9:
                return True
        return False
