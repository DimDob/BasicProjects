from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.controller import Controller
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

controller = Controller()

aquarium = FreshwaterAquarium('aquarium2')

fish1 = FreshwaterFish('Nemo', 'idk', 4 )
fish2 = FreshwaterFish('fish2', 's2', 5)
fish3 = SaltwaterFish('fish3', 's3', 5)

aquarium.add_fish(fish1)
aquarium.add_fish(fish2)
aquarium.add_fish(fish3)



plant = Plant()
plant2 = Plant()
plant3= Plant()
plant4 = Plant()

aquarium.add_decoration(plant)
aquarium.add_decoration(plant2)
aquarium.add_decoration(plant3)
aquarium.add_decoration(plant4)

print(controller.add_aquarium('FreshwaterAquarium', 'aquarium2'))
controller.add_decoration('Plant')
controller.add_decoration('Plant')
controller.add_fish('aquarium2', 'FreshwaterFish', 'Nemo', 's3', 4)
controller.add_fish('aquarium2', 'FreshwaterFish', 'Nemo', 's3', 4)
controller.insert_decoration('aquarium2', 'Plant')

print(controller.calculate_value('aquarium2'))

print(controller.report())