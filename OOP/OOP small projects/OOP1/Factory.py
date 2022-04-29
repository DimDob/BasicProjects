from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Factory:
    @staticmethod
    def create_car(car_type, model, speed_limit):
        if car_type not in ['MuscleCar', 'SportsCar']:
            return
        if car_type == 'MuscleCar':
            return MuscleCar(model, speed_limit)
        return SportsCar(model, speed_limit)

    @staticmethod
    def create_driver(driver_name):
        return Driver(driver_name)

    @staticmethod
    def create_race(race_name):
        return Race(race_name)

    @staticmethod
    def find_last_free_car(cars, car_type):
        for car in cars[::-1]:
            if car.is_taken:
                continue
            if car_type == car.__class__.__name__ and not car.is_taken:
                return car
    @staticmethod
    def find_driver_by_name(driver_name, drivers):
        for driver in drivers:
            if driver.name == driver_name:
                return driver

    @staticmethod
    def find_race_by_name(race_name, races):
        for r in races:
            if r.name == race_name:
                return r