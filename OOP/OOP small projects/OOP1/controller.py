from project.Factory import Factory


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []


    def create_car(self, car_type: str, model: str, speed_limit: int):
        for c in self.cars:
            if c.model == model:
                raise Exception(f"Car {model} is already created!")

        car = Factory.create_car(car_type, model, speed_limit)

        self.cars.append(car)
        return f"{car_type} {model} is created."


    def create_driver(self, driver_name: str):
        if any(d for d in self.drivers if d.name == driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Factory.create_driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."


    def create_race(self, race_name: str):
        if any(r for r in self.races if r.name == race_name):
            raise Exception(f"Race {race_name} is already created!")
        race = Factory.create_race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = Factory.find_driver_by_name(driver_name, self.drivers)
        car = Factory.find_last_free_car(self.cars, car_type)

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            old_car = driver.car
            driver.car = car
            car.is_taken = True
            old_car.is_taken = False
            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."


        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."


    def add_driver_to_race(self, race_name:str, driver_name: str):
        driver = Factory.find_driver_by_name(driver_name, self.drivers)
        race = Factory.find_race_by_name(race_name, self.races)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = Factory.find_race_by_name(race_name, self.races)

        if race is None:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")


        sorted_racers = sorted(race.drivers, key=lambda x: x.car.speed_limit, reverse=True)[:3]

        result = f""
        for racer in sorted_racers:
            racer.number_of_wins += 1
            result += f"Driver {racer.name} wins the {race_name} race with a speed of {racer.car.speed_limit}.\n"
        return result.strip()