from astronaut.astronaut_repository import AstronautRepository
from astronaut.biologist import Biologist
from astronaut.geodesist import Geodesist
from astronaut.meteorologist import Meteorologist
from planet.planet import Planet
from planet.planet_repository import PlanetRepository


class SpaceStation:
    successful_missions = 0
    unsuccessful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        valid_astronaut_types = ["Biologist", "Geodesist", "Meteorologist"]
        if astronaut_type not in valid_astronaut_types:
            raise Exception('Astronaut type is not valid!')

        if self.astronaut_repository.find_by_name(name):
            return f'{name} is already added.'

        new_astronaut = None
        if astronaut_type == 'Biologist':
            new_astronaut = Biologist(name)
        elif astronaut_type == 'Geodesist':
            new_astronaut = Geodesist(name)
        elif astronaut_type == 'Meteorologist':
            new_astronaut = Meteorologist(name)
        self.astronaut_repository.add(new_astronaut)
        return f'Successfully added {new_astronaut.__class__.__name__}: {new_astronaut.name}.'

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f'{name} is already added.'

        items_to_add = items.split(', ')
        new_planet = Planet(name)
        new_planet.items = items_to_add
        self.planet_repository.add(new_planet)
        return f'Successfully added Planet: {new_planet.name}.'

    def retire_astronaut(self, name: str):
        if not self.astronaut_repository.find_by_name(name):
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(self.astronaut_repository.find_by_name(name))
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):
        [astronaut.increase_oxygen(10) for astronaut in self.astronaut_repository.astronauts]

    def send_on_mission(self, planet_name: str):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception('Invalid planet name!')
        planet = self.planet_repository.find_by_name(planet_name)

        astronauts_for_mission = self.__choose_astronauts_for_mission()
        astronauts_used = 0
        mission_completed = False
        for astronaut in astronauts_for_mission:
            if len(planet.items) == 0:
                mission_completed = True
                break
            astronauts_used += 1
            while astronaut.oxygen > 0:
                if len(planet.items) == 0:
                    mission_completed = True
                    break
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()

        if mission_completed:
            self.successful_missions += 1
            return f'Planet: {planet_name} was explored. {astronauts_used} astronauts participated in collecting items.'
        self.unsuccessful_missions += 1
        return f'Mission is not completed.'

    def __choose_astronauts_for_mission(self):
        astronauts_with_oxygen_above_30 = [astronauts for astronauts in self.astronaut_repository.astronauts if
                                           astronauts.oxygen > 30]
        if not astronauts_with_oxygen_above_30:
            raise Exception('You need at least one astronaut to explore the planet!')
        astronauts = sorted(astronauts_with_oxygen_above_30, key=lambda a: -a.oxygen)[0:5]
        return astronauts

    def report(self):
        result = [
            f'{self.successful_missions} successful missions!',
            f'{self.unsuccessful_missions} missions were not completed!',
            "Astronauts' info:"
        ]
        for astronaut in self.astronaut_repository.astronauts:
            astronaut_data = [f'Name: {astronaut.name}', f'Oxygen: {astronaut.oxygen}']
            astronaut_data.append(f"Backpack items: {', '.join(astronaut.backpack)}") if len(astronaut.backpack) > 0 else astronaut_data.append('Backpack items: none')
            result.append('\n'.join(astronaut_data))
        return '\n'.join(result)

