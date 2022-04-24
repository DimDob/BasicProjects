from project.rooms.calculate_expenses import Calculate
from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = Calculate.get_total_monthly_costs_for_every_room(self.rooms)
        return f"Monthly consumption: {result:.2f}$."

    def pay(self):
        return Calculate.is_payment_possible(self.rooms)

    def status(self):
        return Calculate.status_repr(self.rooms)