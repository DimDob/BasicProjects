class Calculate:
    @staticmethod
    def get_total_monthly_costs_for_every_room(rooms):
        return sum(room.expenses for room in rooms) + sum(room.room_cost for room in rooms)


    @staticmethod
    def calculate_expenses(args):
        result = 0
        for obj in args:
            for instance in obj:
                result += instance.cost * 30
        return result

    @staticmethod
    def is_payment_possible(rooms):
        result = f""
        for room in rooms:
            if room.budget >= room.expenses:
                room.budget -= room.expenses + room.room_cost
                result += f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {room.budget:.2f}$ left.\n"
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                rooms.remove(room)
        return result.strip()


    @staticmethod
    def status_repr(rooms):
        members_in_the_hotel = 0
        for room in rooms:
            members_in_the_hotel += room.members_count

        result = f"Total population: {members_in_the_hotel}\n"
        for room in rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if len(room.children) > 0:
                i = 1
                for child in room.children:

                    result += f"--- Child {i} monthly cost: {child.cost * 30:.2f}$\n"
                    i += 1

                result += f"--- Appliances monthly cost: {Calculate.calculate_expenses([room.appliances]):.2f}$\n"
            else:
                result += f"--- Appliances monthly cost: {Calculate.calculate_expenses([room.appliances]):.2f}$\n"

        return result.strip()