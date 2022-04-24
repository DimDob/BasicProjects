from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Calculations:

    @staticmethod
    def total_decorations_comfort(decorations):
        result = 0
        for decoration in decorations:
            result += decoration.comfort
        return result

    @staticmethod
    def adding_fish(fish_type, capacity, fishes):
        if capacity <= len(fishes):
            return False
        if fish_type == 'FreshwaterFish' or fish_type == 'SaltwaterFish':
            return True

    @staticmethod
    def feeding_all_fishes(fishes):
        for fish in fishes:
            fish.eat()

    @staticmethod
    def find_first_decoration_by_type(decoration_type,decorations):
        for decoration in decorations:
            if decoration.type == decoration_type:
                return decoration
        return 'None'

    @staticmethod
    def create_aquarium(aquarium_type, aquarium_name):
        if aquarium_type == 'FreshwaterAquarium':
            return FreshwaterAquarium(aquarium_name)
        elif aquarium_type == 'SaltwaterAquarium':
            return SaltwaterAquarium(aquarium_name)
        return False

    @staticmethod
    def adding_decoration(decoration_type):
        if decoration_type == 'Ornament':
            return Ornament()
        elif decoration_type == 'Plant':
            return Plant()
        return False

    @staticmethod
    def find_aquarium_by_name(name, aquariums):
        for aquarium in aquariums:
            if aquarium.name == name:
                return aquarium

    @staticmethod
    def find_decoration_by_type(decoration_type, decorations):
        for decoration in decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration

    @staticmethod
    def inserting_decoration(aquarium_name, decoration_type, aquariums, decorations):
        aquarium = Calculations.find_aquarium_by_name(aquarium_name, aquariums)
        decoration = Calculations.find_decoration_by_type(decoration_type, decorations)

        if decoration is None or aquarium is None:
            return False

        aquarium.decorations.append(decoration)
        decorations.remove(decoration)
        return True

    @staticmethod
    def validate_fish_type(fish_type):
        if fish_type == 'SaltwaterFish' or fish_type == 'FreshwaterFish':
            return True
        return False

    @staticmethod
    def create_fish(type,name,species,price):
        if type == 'FreshwaterFish':
            return FreshwaterFish(name, species, price)
        elif type == 'SaltwaterFish':
            return SaltwaterFish(name, species, price)

    @staticmethod
    def aquarium_value(fishes, decorations):
        fishes_sum = sum(fish.price for fish in fishes)
        decorations_sum = sum(decoration.price for decoration in decorations)
        return fishes_sum + decorations_sum

    @staticmethod
    def report_result(aquariums):
        result = f""
        for aquarium in aquariums:
            result += f"{str(aquarium)}\n"
        return result.strip()
