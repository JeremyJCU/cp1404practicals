from silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Hummer", 200, 2)
taxi.drive(18)
print(taxi.get_fare())
assert taxi.get_fare() == 48.8

