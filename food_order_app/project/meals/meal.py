from abc import ABC, abstractmethod


class Meal(ABC):
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.ordered = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) != 0:
            self.__name = value
        else:
            raise ValueError('Name cannot be an empty string!')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0.0:
            self.__price = value
        else:
            raise ValueError('Invalid price!')

    @abstractmethod
    def details(self):
        pass
