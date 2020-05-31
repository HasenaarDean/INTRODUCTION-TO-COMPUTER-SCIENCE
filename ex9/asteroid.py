import random
from itertools import chain

MAX_ASTROID_SIZE = 3
SIZE_COEFFICIENT = 10
NORMALIZATION_FACTOR = -5


class Asteroid:
    """this class represents all the asteroids in the game.
    if a torpedo hits an asteroid for first time then the asteroid splits
    to two smaller parts with opposite directions; and so in the same way
    for the second hit, but when the asteroid is hit for the third time
    then it disappears.
    """

    def __init__(self, ship, size=MAX_ASTROID_SIZE):
        """ A constructor for an asteroid object in an asteroids game.
        :param ship = the ship that is in the game
        :param size = the size of the asteroid.
        """
        self.size = size

        x = random.randint(-500, 500)
        if x == ship.x():
            new_range = chain(range(-500, ship.y()), range(ship.y() + 1, 500))
            range_in_list = list(new_range)
            y = random.choice(range_in_list)
        else:
            y = random.randint(-500, 500)
        self._pos = (x, y)

        self._x_velocity = random.randint(1, 6)
        self._y_velocity = random.randint(1, 6)

    def set_pos(self, update_pos):
        """this method sets the position of an asteroid."""
        self._pos = update_pos

    def get_pos(self):
        """this method returns the position of an asteroid."""
        return self._pos

    def x(self):
        """this method returns the x value of the asteroid"""
        x = self._pos[0]
        return x

    def y(self):
        """this method returns the y value of the asteroid"""
        y = self._pos[1]
        return y

    def get_x_velocity(self):
        """this method returns the velocity of x coordinate of the asteroid"""
        return self._x_velocity

    def get_y_velocity(self):
        """this method returns the velocity of y coordinate of the asteroid"""
        return self._y_velocity

    def set_x_velocity(self, update):
        """this method sets the velocity of x coordinate of the ship"""
        self._x_velocity = update

    def set_y_velocity(self, update):
        """this method sets the velocity of y coordinate of the ship"""
        self._y_velocity = update

    def radius(self):
        """this method returns the radius of the asteroid"""
        return self.size * SIZE_COEFFICIENT - NORMALIZATION_FACTOR

    def has_intersection(self, obj):
        """this method returns weather or not there was an intersection
        between an asteroid and a torpedo (by returning True or False
        respectively)"""
        distance = ((obj.x() - self.x()) ** 2 + (obj.y() - self.y()) ** 2) ** (
        1 / 2)
        if distance <= self.radius() + obj.radius():
            return True
        else:
            return False

    def get_size(self):
        """this method returns the asteroid's size"""
        return self.size
