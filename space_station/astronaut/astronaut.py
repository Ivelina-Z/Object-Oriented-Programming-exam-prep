from abc import ABC, abstractmethod


class Astronaut(ABC):
    BREATH_UNITS = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Astronaut name cannot be empty string or whitespace!')
        self.__name = value

    @abstractmethod
    def breathe(self):
        self.oxygen -= self.BREATH_UNITS

    @abstractmethod
    def increase_oxygen(self, amount: int):
        self.oxygen += amount
