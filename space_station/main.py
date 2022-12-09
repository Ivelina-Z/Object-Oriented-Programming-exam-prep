from project.space_station import SpaceStation

station = SpaceStation()
print(station.add_astronaut('Biologist', 'B'))
print(station.add_astronaut('Biologist', 'B Senior'))
print(station.add_astronaut('Meteorologist', 'M'))
print(station.add_astronaut('Geodesist', 'G'))
print(station.add_planet('Mars', 'stone, gems, sand'))
print(station.add_planet('Mars', 'stone'))
print(station.retire_astronaut('B Senior'))

for a in station.astronaut_repository.astronauts:
    print(a.oxygen, a.name)
station.recharge_oxygen()
for a in station.astronaut_repository.astronauts:
    print(a.oxygen, a.name)

print(station.send_on_mission('Mars'))
print(station.report())
