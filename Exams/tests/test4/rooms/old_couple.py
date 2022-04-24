from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.rooms.calculate_expenses import Calculate
from project.rooms.crafting import CraftingObjects
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = 15
        stoves = CraftingObjects.craft_stove_n_times(2)
        tvs = CraftingObjects.craft_TV_n_times(2)
        fridges = CraftingObjects.craft_fridge_n_times(2)
        self.appliances = []
        self.appliances.extend(tvs)
        self.appliances.extend(fridges)
        self.appliances.extend(stoves)
        self.expenses = Calculate.calculate_expenses([self.appliances])
