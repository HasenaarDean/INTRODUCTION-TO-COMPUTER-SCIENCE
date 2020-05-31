from random import randint
import math

SHIP_RADIUS = 1
SHIP_START_LIFE = 3


class Ship:
    """this class represents a spaceship in an asteroids game.
    the ship can move in all direction, accelerate and shoot torpedos
    if the ship is hit by an asteroid - then the game ends.
    """
    def __init__(self):
        """ A constructor for a Ship object.
        """
        x = randint(-500, 500)
        y = randint(-500, 500)
        self._pos = (x, y)

        self._x_velocity = 0
        self._y_velocity = 0

        self._direction = 0

        self.life = SHIP_START_LIFE

    def set_pos(self, update_pos):
        """this method updates the ship's position"""
        self._pos = update_pos

    def get_pos(self):
        """this method returns the ship's position"""
        return self._pos

    def x(self):
        """this method returns the x value of the ship"""
        x = self._pos[0]
        return x

    def y(self):
        """this method returns the y value of the ship"""
        y = self._pos[1]
        return y

    def get_x_velocity(self):
        """this method returns the velocity of x coordinate of the ship"""
        return self._x_velocity

    def get_y_velocity(self):
        """this method returns the velocity of y coordinate of the ship"""
        return self._y_velocity

    def set_x_velocity(self, update):
        """this method sets the velocity of x coordinate of the ship"""
        self._x_velocity = update

    def set_y_velocity(self, update):
        """this method sets the velocity of y coordinate of the ship"""
        self._y_velocity = update

    def get_direction(self):
        """this method returns the ship's direction"""
        return self._direction

    def change_direction(self, direction):
        """this method changes the direction of the ship"""
        if direction == "left":
            self._direction += 7
        else:
            self._direction -= 7

    def accelerate(self):
        """this method accelerates the ship's velocity"""
        radian_heading = math.radians(self._direction)
        self._x_velocity += math.cos(radian_heading)
        self._y_velocity += math.sin(radian_heading)

    def radius(self):
        """this method returns the ship's radius"""
        return SHIP_RADIUS