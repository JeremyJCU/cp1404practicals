from unreliable_car import UnreliableCar

MIN_RANGE = 1
MAX_RANGE = 101

reliability_test = UnreliableCar("Car", 100, 30)
reliability_test.drive(90)

reliability_test = UnreliableCar("Car", 100, 30)
for i in range(MIN_RANGE, MAX_RANGE):
    reliability_test.drive(1)
print(reliability_test)
