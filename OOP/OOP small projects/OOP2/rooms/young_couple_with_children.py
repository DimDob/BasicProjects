from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.rooms.calculate_expenses import Calculate
from project.rooms.crafting import CraftingObjects
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, len(children)+2)
        self.children.extend(children)
        self.room_cost = 30
        total_members = len(children) + 2
        laptops = CraftingObjects.craft_laptop_n_times(total_members)
        tvs = CraftingObjects.craft_TV_n_times(total_members)
        fridges = CraftingObjects.craft_fridge_n_times(total_members)

        self.appliances = []

        self.appliances.extend(laptops)
        self.appliances.extend(tvs)
        self.appliances.extend(fridges)

        self.expenses = Calculate.calculate_expenses([self.children, self.appliances])
