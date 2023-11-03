from car import Car
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date,
                        current_mileage, last_service_mileage,
                        sensor_values):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(sensor_values)
        car = Car(engine, battery, tire)
        return car


    @staticmethod
    def create_glissade(current_date, last_service_date,
                        current_mileage, last_service_mileage,
                        sensor_values)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(sensor_values)
        car = Car(engine, battery, tire)
        return car


    @staticmethod
    def create_palindrome(current_date, last_service_date,
                          warning_light_on, sensor_values):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(sensor_values)
        car = Car(engine, battery, tire)
        return car


    @staticmethod
    def create_rorschach(current_date, last_service_date,
                         current_mileage, last_service_mileage,
                         sensor_values):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(sensor_values)
        car = Car(engine, battery, tire)
        return car


    @staticmethod
    def create_thovex(current_date, last_service_date,
                      current_mileage, last_service_mileage,
                      sensor_values):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinEngine(last_service_date, current_date)
        tire = CarriganTire(sensor_values)
        car = Car(engine, battery, tire)
        return car
