from project.calcs import Calculations
from project.decoration.decoration_repository import DecorationRepository


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []


    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        result = Calculations.create_aquarium(aquarium_type, aquarium_name)
        if not result:
            return "Invalid aquarium type."
        self.aquariums.append(result)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        decoration = Calculations.adding_decoration(decoration_type)
        if not decoration:
            return "Invalid decoration type."
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        result = Calculations.inserting_decoration(aquarium_name, decoration_type, self.aquariums, self.decorations_repository.decorations)

        if not result:
            return f"There isn't a decoration of type {decoration_type}."
        return f"Successfully added {decoration_type} to {aquarium_name}."


    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid = Calculations.validate_fish_type(fish_type)
        if not valid:
           return f"There isn't a fish of type {fish_type}."
        aquarium = Calculations.find_aquarium_by_name(aquarium_name, self.aquariums)

        if len(aquarium.fish) >= aquarium.capacity:
            return "Not enough capacity."



        if (fish_type == 'SaltwaterFish' and aquarium.__class__.__name__ != 'SaltwaterAquarium') \
                or (fish_type == 'FreshwaterFish' and aquarium.__class__.__name__ != 'FreshwaterAquarium'):
            return "Water not suitable."

        fish = Calculations.create_fish(fish_type, fish_name, fish_species, price)
        aquarium.add_fish(fish)
        return f"Successfully added {fish_type} to {aquarium_name}."


    def feed_fish(self, aquarium_name: str):
        aquarium = Calculations.find_aquarium_by_name(aquarium_name, self.aquariums)
        aquarium.feed()
        fish_fed = len(aquarium.fish)
        return f"Fish fed: {fish_fed}"


    def calculate_value(self, aquarium_name: str):
        aquarium = Calculations.find_aquarium_by_name(aquarium_name, self.aquariums)
        return Calculations.aquarium_value(aquarium.fish, aquarium.decorations)


    def report(self):
        return Calculations.report_result(self.aquariums)

