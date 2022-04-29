from project.calcs import Calculations
from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self. decorations = []

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        return Calculations.find_first_decoration_by_type(decoration_type, self.decorations)