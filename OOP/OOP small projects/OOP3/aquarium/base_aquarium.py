from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity

        self.decorations = []
        self.fish = []


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return False
        if fish.__class__.__name__ == 'FreshwaterFish' or fish.__class__.__name__  == 'SaltwaterFish':
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        return "Not enough capacity."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_names = ' '.join(fish.name for fish in self.fish) if len(self.fish) > 0 else 'none'

        result = f"{self.name}:\n" \
                 f"Fish: {fish_names}\n" \
                 f"Decorations: {len(self.decorations)}\n" \
                 f"Comfort: {self.calculate_comfort()}"
        return result.strip()
