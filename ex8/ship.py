#############################################################
# FILE : ship.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex8 2016 - 2017
# DESCRIPTION: In this file we implemented the Ship class.
#############################################################


import ship_helper
import copy


# Magic Numbers:
MOVE = 1


class Direction:

    """
    Class representing a direction in 2D world.
    You may not change the name of any of the constants (UP, DOWN, LEFT, RIGHT,
     NOT_MOVING, VERTICAL, HORIZONTAL, ALL_DIRECTIONS), but all other
     implementations are for you to carry out.
    """

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    NOT_MOVING = 4

    VERTICAL = (UP, DOWN)
    HORIZONTAL = (LEFT, RIGHT)

    ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)


############################################################
# Class definition
############################################################


class Ship:

    """
    A class representing a ship in Battleship game.
    A ship is 1-dimensional object that could be laid in either horizontal or
    vertical alignment. A ship sails on its vertical\horizontal axis back and
    forth until reaching the board's boarders and then changes its direction to
    the opposite (left <--> right, up <--> down).
    If a ship is hit in one of its coordinates, it ceases its movement in all
    future turns.
    A ship that had all her coordinates hit is considered terminated.
    """

    def __init__(self, pos, length, direction, board_size):

        """
        A constructor for a Ship object
        :param pos: A tuple representing The ship's head's (x, y) position
        :param length: Ship's length
        :param direction: Initial direction in which the ship is sailing
        :param board_size: Board size in which the ship is sailing
        """

        self._pos = pos
        self._length = length
        self._act_direction = direction
        self._board_size = board_size
        self._hits = []

    def __repr__(self):

        """
        Return a string representation of the ship.
        :return: A tuple converted to string. The tuple's content should be (in
        the exact following order):
            1. A list of all the ship's coordinates.
            2. A list of all the ship's hit coordinates.
            3. Last sailing direction.
            4. The size of the board in which the ship is located.
        """

        descriptive_tpl = str(tuple((self.coordinates(), self._hits,
                                     ship_helper.direction_repr_str(
                                         Direction, self._act_direction),
                                     self._board_size)))
        return descriptive_tpl

    def move(self):

        """
        Make the ship move one board unit.
        Movement is in the current sailing direction, unless such movement
        would take it outside of the board in which case the ship switches
        direction and sails one board unit in the new direction.
        the ship :return: A direction object representing the current
        movement direction.
        """

        if self._act_direction == Direction.DOWN:
            if self._pos[1] + self._length < self._board_size:
                self._pos = (self._pos[0], self._pos[1] + MOVE)
            else:
                self._act_direction = Direction.UP
                self._pos = (self._pos[0], self._pos[1] - MOVE)
        elif self._act_direction == Direction.UP:
            if self._pos[1] > 0:
                self._pos = (self._pos[0], self._pos[1] - MOVE)
            else:
                self._act_direction = Direction.DOWN
                self._pos = (self._pos[0], self._pos[1] + MOVE)
        elif self._act_direction == Direction.RIGHT:
            if self._pos[0] + self._length < self._board_size:
                self._pos = (self._pos[0] + MOVE, self._pos[1])
            else:
                self._act_direction = Direction.LEFT
                self._pos = (self._pos[0] - MOVE, self._pos[1])
        elif self._act_direction == Direction.LEFT:
            if self._pos[0] > 0:
                self._pos = (self._pos[0] - MOVE, self._pos[1])
            else:
                self._act_direction = Direction.RIGHT
                self._pos = (self._pos[0] + MOVE, self._pos[1])
        elif self._act_direction == Direction.NOT_MOVING:
            self._pos = self._pos
        return self._act_direction

    def hit(self, pos):

        """
        Inform the ship that a bomb hit a specific coordinate. The ship updates
         its state accordingly.
        If one of the ship's body's coordinate is hit, the ship does not move
         in future turns. If all ship's body's coordinate are hit, the ship is
         terminated and removed from the board.
        :param pos: A tuple representing the (x, y) position of the hit.
        :return: True if the bomb generated a new hit in the ship, False
         otherwise.
        """

        if pos not in self.coordinates():
            return False
        else:
            if pos not in self._hits:
                self._hits.append(pos)
                self.last_direction = self._act_direction
                self._act_direction = Direction.NOT_MOVING
                return True
            return False

    def terminated(self):

        """
        :return: True if all ship's coordinates were hit in previous turns,
        False otherwise.
        """

        return len(self._hits) == self._length

    def __contains__(self, pos):

        """
        Check whether the ship is found in a specific coordinate.
        :param pos: A tuple representing the coordinate for check.
        :return: True if one of the ship's coordinates is found in the given
        (x, y) coordinates, False otherwise.
        """

        return pos in self.coordinates()

    def coordinates(self):

        """
        Return ship's current positions on board.
        :return: A list of (x, y) tuples representing the ship's current
        position.
        """

        x_axis, y_axis = 0, 1
        if self._act_direction == Direction.NOT_MOVING:
            return self.last_coords
        if self._act_direction == Direction.UP or self._act_direction == \
                Direction.DOWN:
            fixed_coord = x_axis
            len_coord = y_axis
        else:
            fixed_coord = y_axis
            len_coord = x_axis

        coords = []
        if fixed_coord == x_axis:
            for value in range(self._pos[len_coord],
                               self._pos[len_coord] + self._length):
                coords.append((self._pos[fixed_coord], value))
        else:
            for value in range(self._pos[len_coord],
                               self._pos[len_coord] + self._length):
                coords.append((value, self._pos[fixed_coord]))
        self.last_coords = coords
        return coords

    def damaged_cells(self):

        """
        Return the ship's hit positions.
        :return: A list of tuples representing the (x, y) coordinates of the
         ship which were hit in past turns (If there are no hit coordinates,
         return an empty list). There is no importance to the order of the
         values in the returned list.
        """

        hit_list = copy.deepcopy(self._hits)
        return hit_list

    def get_un_damaged_cells(self):

        """
        This function returns the ship's fixed positions as a list
        of tuples, in the same way of the function damaged_cells.
        """

        coor = self.coordinates()
        hitted = self._hits
        for hit in hitted:
            coor.remove(hit)
        return coor

    def direction(self):

        """
        Return the ship's current sailing direction.
        :return: One of the constants of Direction class :
         [UP, DOWN, LEFT, RIGHT] according to current
         sailing direction or NOT_MOVING if the ship is hit and not moving.
        """

        return self._act_direction

    def cell_status(self, pos):

        """
        Return the state of the given coordinate (hit\not hit)
        :param pos: A tuple representing the coordinate to query.
        :return:
            if the given coordinate is not hit : False
            if the given coordinate is hit : True
            if the coordinate is not part of the ship's body : None 
        """

        if pos not in self.coordinates():
            return None
        else:
            return pos in self._hits
