from random import randint

class Die():
    """The class representing one six-sided die"""

    def __init__(self, num_sides=6):
        """Assumption that a die is the form of a cube"""
        self.num_sides = num_sides

    def roll(self):
        """Return value from 1 to the number of sides a die has"""
        return randint(1, self.num_sides)