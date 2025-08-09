"""
CP1404/CP5632 Practical
UnreliableCar class
"""

from car import Car
from random import randint

MIN = 0
MAX = 100

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name=name, fuel=fuel)
        #Error checking added to make sure correct reliability range entered
        self.reliability = self.valid_reliability(reliability, MIN, MAX)

    def drive(self, distance):
        """Only drive car if reliability is greater random number between 0 and 100"""
        reliability_test = randint(0, 100)
        if self.reliability < reliability_test :
            print(f"{reliability_test} poor reliability")
            return 0
        else:
            print(f"{reliability_test} acceptable reliability")
            return super().drive(distance)

    def valid_reliability(self,reliability, min, max):
        """"Make sure the reliability is within range"""
        if reliability < min or reliability > max:
            print(f"{reliability} out of range")
            return 0.0
        else:
            return reliability

# if __name__ == '__main__':
#     ucar = UnreliableCar("Car", 100, 50)
#     ucar.drive(90)
#     print(ucar)
