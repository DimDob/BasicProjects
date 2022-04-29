from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.rooms.calculate_expenses import Calculate
from project.rooms.crafting import CraftingObjects
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        laptops = CraftingObjects.craft_laptop_n_times(2)
        fridges = CraftingObjects.craft_fridge_n_times(2)
        tv = CraftingObjects.craft_TV_n_times(2)

        self.appliances = []
        self.appliances.extend(laptops)
        self.appliances.extend(fridges)
        self.appliances.extend(tv)
        self.expenses = Calculate.calculate_expenses([self.appliances])

