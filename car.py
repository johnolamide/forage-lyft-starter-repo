"""
Car class definition
"""
from servicable import Servicable

class Car(Servicable):
    def __init__(self, engine, battery):
        """
        car constructor with engine and battery property
        """
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battey.needs_service()
