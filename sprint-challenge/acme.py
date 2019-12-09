from numpy import random

class Product:
    """A Product of Acme Corp. Products have the
    following properties:
    Attributes:
        - `name` (string with no default)
        - `price` (integer with default value 10)
        - `weight` (integer with default value 20)
        - `flammability` (float with default value 0.5)
        - `identifier` (integer, automatically genererated as a random (uniform) number
           anywhere from 1000000 to 9999999, includisve)(inclusive).
    """

    def __init__(prod, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 999999999)):
        prod.name = name
        prod.price = price
        prod.weight = weight
        prod.flammability = flammability

    @classmethod
    def stealability(Product):
        steals = price/weight

    class Product(object):
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 999999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def stealability(self):
        steals = self.price/self.weight
        if steals < .5:
            return "Not so stealable..."
        elif steals >= .5 and steals <1:
            return "Kinda stealable."
        else:
            return "Very stealable!"
