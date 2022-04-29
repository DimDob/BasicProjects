class PriceForAllToys:
    @staticmethod
    def calculate_price_for_toys(toys):
        result = sum([toy for toy in toys])
        return result