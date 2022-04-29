
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 1 or value.isspace():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type == 'Bread':
            food = Bread(name,price)
            for f in self.food_menu:
                if f.name == name:
                    raise Exception(f"{food_type} {name} is already in the menu!")
            self.food_menu.append(food)
            return f"Added {name} ({food.__class__.__name__}) to the food menu"
        elif food_type == 'Cake':
            food = Cake(name, price)
            for f in self.food_menu:
                if f.name == name:
                    raise Exception(f"{food_type} {name} is already in the menu!")
            self.food_menu.append(food)
            return f"Added {name} ({food.__class__.__name__}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        if drink_type == 'Tea':
            drink = Tea(name, portion, brand)
            for d in self.drinks_menu:
                if d.name == name:
                    raise Exception(f"{drink_type} {name} is already in the menu!")

            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

        elif drink_type == 'Water':
            drink = Water(name, portion, brand)
            for d in self.drinks_menu:
                if d.name == name:
                    raise Exception(f"{drink_type} {name} is already in the menu!")

            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type == 'InsideTable':
            table = InsideTable(table_number, capacity)
            for t in self.tables_repository:
                if t.table_number == table_number:
                    raise Exception(f"Table {table_number} is already in the bakery!")
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"
        elif table_type == 'OutsideTable':
            table = OutsideTable(table_number, capacity)
            for t in self.tables_repository:
                if t.table_number == table_number:
                    raise Exception(f"Table {table_number} is already in the bakery!")
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.is_reserved:
                continue
            if table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def find_table_by_number(self, table_number, tables):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

    def find_food_by_name(self, food_name, foods):
        for f in foods:
            if f.name == food_name:
                return f

    def find_food_by_class_name(self, food_name, foods):
        for f in foods:
            if f.__class__.__name__==  "Bread" or f.__class__.__name__==  "Cake":
                return f


    def order_food (self, table_number: int, *foods):

        table = self.find_table_by_number(table_number, self.tables_repository)
        if table is None:
            return f"Could not find table {table_number}"

        ordered = f'Table {table_number} ordered:\n'
        missing_foods = f'{self.name} does not have in the menu:\n'
        for food_name in foods:
            food = self.find_food_by_name(food_name, self.food_menu)
            if food is not None:
                table.order_food(food)
                ordered += f'{food}\n'
            else:
                missing_foods += f'{food_name}\n'

        return ordered.strip() + '\n' + missing_foods.strip()



    def order_drink (self, table_number: int,*drinks):
        table = self.find_table_by_number(table_number, self.tables_repository)
        if table is None:
            return f"Could not find table {table_number}"


        ordered = f'Table {table_number} ordered:\n'
        missing_drinks = f'{self.name} does not have in the menu:\n'
        for drink_name in drinks:
            drink = self.find_drink_by_name(drink_name, self.drinks_menu)
            if drink is not None:
                table.order_drink(drink)
                ordered += f'{drink}\n'
            else:
                missing_drinks += f'{drink_name}\n'

        return ordered.strip() + '\n' + missing_drinks.strip()

    def leave_table (self, table_number: int):
        table = self.find_table_by_number(table_number, self.tables_repository)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        result = f'Table: {table.table_number}\nBill: {bill:.2f}'
        return result.strip()

    def get_free_tables_info(self):
        result = f''
        for table in self.tables_repository:
            if not table.is_reserved:
                result += f'{table.free_table_info()}\n'
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def find_drink_by_name(self, drink_name, drinks_menu):
        for d in drinks_menu:
            if d.name == drink_name:
                return d

