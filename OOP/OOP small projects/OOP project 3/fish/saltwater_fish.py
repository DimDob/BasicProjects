from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    FISH_SIZE_INCREASE = 2

    def __init__(self, name: str, species: str,  price: float):
        self.name = name
        self.species = species
        self.price = price
        self.size = 5


    def eat(self):
        self.size += self.FISH_SIZE_INCREASE
