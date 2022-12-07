from astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    BREATH_UNITS = 5

    def __init__(self, name: str, oxygen: int = 70):
        super().__init__(name, oxygen)
        
    def breathe(self):
        self.oxygen -= self.BREATH_UNITS

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
