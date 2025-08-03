from taxi import Taxi

taxi = Taxi("Prius 1", 100)
taxi.drive(40)
print(f"Taxi details: {taxi} Current fair: {taxi.get_fare()}")
taxi.start_fare()
taxi.drive(100)
print(f"Taxi details: {taxi} Current fair: {taxi.get_fare()}")
