"""
Car class definition
"""
from servicable import Servicable

class Car(Servicable):
    def __init__(self, engine, battery, tire):
        """
        car constructor with engine, battery and tire property
        """
        self.engine = engine
        self.battery = battery
        self.tire = tire

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
