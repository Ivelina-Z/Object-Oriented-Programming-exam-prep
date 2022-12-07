from astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    BREATH_UNITS = 15

    def __init__(self, name: str, oxygen: int = 90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.BREATH_UNITS

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
