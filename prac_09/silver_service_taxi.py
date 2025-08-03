"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name=name, fuel=fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * self.fanciness
        self.flagfall = 4.5

    def __str__(self):
        return f"{super().__str__()}, plus flagfall ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall


if __name__ == '__main__':
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(18)
    print(taxi.get_fare())
