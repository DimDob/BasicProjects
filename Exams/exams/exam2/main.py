from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.bakery import Bakery
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

table = OutsideTable(51, 10)
bakery = Bakery('Nedelya')
print(bakery.add_table('OutsideTable', 51, 10))
print(bakery.add_table('OutsideTable', 54, 10))
print(bakery.add_food('Bread', 'Sussame', 2.50))
print(bakery.add_food('Cake', 'Nedelya', 4.50))
print(bakery.add_food('Bread', 'Susamme', 3.50))
print(bakery.reserve_table(10))
print(bakery.reserve_table(10))
print(bakery.reserve_table(10))

bakery.add_drink('Tea', 'GreenTea', 250, 'Nestle')
bakery.add_drink('Tea', 'WhiteTea', 250, 'Norton')
bakery.add_drink('Water', 'Mineral', 250, 'Bankya')

print(bakery.order_food(51, 'Pizza', 'Nedelya', 'Sussame', 'Pasta', 'Pork'))
print(bakery.order_drink(51, 'Fanta', 'GreenTea', 'Mineral', 'WhiteTea', 'Whiskey'))
# print(bakery.leave_table(51))
#
# print(bakery.get_free_tables_info())
# print(bakery.get_total_income())