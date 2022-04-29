from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV


class CraftingObjects:
    @staticmethod
    def craft_stove_n_times(number):
        objects = []
        for n in range(number):
            objects.append(Stove())

        return objects

    @staticmethod
    def craft_laptop_n_times(number):
        objects = []
        for n in range(number):
            objects.append(Laptop())
        return objects

    @staticmethod
    def craft_TV_n_times(number):
        objects = []
        for n in range(number):
            objects.append(TV())
        return objects

    @staticmethod
    def craft_fridge_n_times(number):
        objects = []
        for n in range(number):
            objects.append(Fridge())
        return objects