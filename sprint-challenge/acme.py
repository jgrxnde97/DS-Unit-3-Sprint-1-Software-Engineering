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


    @classmethod
    def explode(Product):
        explo = flammability * weight

    def explode(self):
        explo = self.flammability * self.weight
        if explo < 10:
            return "fizzle..."
        elif steals >= 10 and steals <50:
            return "...boom"
        elif explo >= 10 and explo <50:
            return "...boom!"
        else:
            return "...BABOOM!!"
class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000,999999999)):
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

    def explode(self):
            return "...it's a glove."

    def punch(self):
        pun = self.weight
        if pun < 5:
            return "That tickles."
        elif pun >= 5 and pun <15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
