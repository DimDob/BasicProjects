from project.people.price_for_all_toys import PriceForAllToys


class Child:
    def __init__(self, food_cost: int, *toys_cost):
        price = PriceForAllToys.calculate_price_for_toys(toys_cost)
        self.cost = food_cost + price
