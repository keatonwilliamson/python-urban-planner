from building import Building
from city import City

print("hey")

five_hundred_interstate = Building("500 Interstate Blvd S", 4)
plus_park = Building("301 PLus Park Blvd", 4)
best_building_ever = Building("1234 amazing street", 80)
smallest_building_ever = Building("1234 smol street", 1)

five_hundred_interstate.purchase("Steve")
plus_park.purchase("Guy")
best_building_ever.purchase("John")
smallest_building_ever.purchase("Dude")

five_hundred_interstate.width, five_hundred_interstate.depth = 2, 2
plus_park.width, plus_park.depth = 3, 3
best_building_ever.width, best_building_ever.depth = 4, 4
smallest_building_ever.width, smallest_building_ever.depth = 1, 1

five_hundred_interstate.construct()
plus_park.construct()
best_building_ever.construct()
smallest_building_ever.construct()

nashville = City()

nashville.add_building(five_hundred_interstate)
nashville.add_building(plus_park)
nashville.add_building(best_building_ever)
nashville.add_building(smallest_building_ever)

for building in nashville.buildings:
    print(building)



