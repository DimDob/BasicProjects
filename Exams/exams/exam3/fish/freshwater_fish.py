from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    FISH_SIZE_INCREASE = 3

    def __init__(self, name: str, species: str, price: float):
        self.name = name
        self.species = species
        self.price = price
        self.size = 3

    def eat(self):
        self.size += self.FISH_SIZE_INCREASE

