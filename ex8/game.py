#############################################################
# FILE : ship.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex8 2016 - 2017
# DESCRIPTION: In this file we implemented the Ship class.
#############################################################


import game_helper as gh
import ship


# Magic Numbers:
TIME_IS_TICKING = 1
BOMBS_LIFE = 3
TIME_IS_OVER = 0
LAST_TURN_OF_A_BOMB = 1


class Game:

    """
    A class representing a battleship game.
    A game is composed of ships that are moving on a square board and a user
    which tries to guess the locations of the ships by guessing their
    coordinates.
    """

    def __init__(self, board_size, ships):

        """
        Initialize a new Game object.
        :param board_size: Length of the side of the game-board
        :param ships: A list of ships that participate in the game.
        :return: A new Game object.
        """

        self.board_size = board_size
        self.ships_list = ships
        self.initial_ship_amount = len(self.ships_list)
        self.total_ships_coord = self.get_total_ships_coords()
        self.terminated_ships = []
        self.total_hit_coord = []
        self.bombs_dict = {}
        self.total_terminations = []

    def get_total_ships_coords(self):

        """
        This function returns all the ships' coordinates as a list of
        tuples which each tuple represent the current location of each cell.
        """

        total_ships_coord = []
        for ship in self.ships_list:
            for coord in ship.coordinates():
                total_ships_coord.append(coord)
        return total_ships_coord

    def update_bombs(self):

        """
        This function updates all the bombs' statuses in the game which are
        in a dictionary.
        """

        for bomb in self.bombs_dict:
            self.bombs_dict[bomb] -= TIME_IS_TICKING

        bombs_to_delete = []
        for bomb in self.bombs_dict:
            if self.bombs_dict[bomb] == TIME_IS_OVER:
                bombs_to_delete.append(bomb)
        for bomb in bombs_to_delete:
            del self.bombs_dict[bomb]

    def update_ships(self):

        """
        This function updates the ships in the game and returns the
        current turn hits number and current turn terminations number.
        """

        current_turn_hits = []
        current_turn_terminations = []
        hits_in_this_turn = []
        for ship in self.ships_list:
            if ship in self.terminated_ships:
                for coord in ship.coordinates():
                    self.total_hit_coord.remove(coord)
                self.ships_list.remove(ship)
                continue
            ship.move()
            for bomb in self.bombs_dict:
                if ship.hit(bomb):
                    ship.hit(bomb)
                    hits_in_this_turn.append(bomb)
                    current_turn_hits.append(bomb)
                    self.total_hit_coord.append(bomb)
            if ship.terminated() and ship not in self.total_terminations:
                current_turn_terminations.append(ship)
                self.total_terminations.append(ship)
                self.terminated_ships.append(ship)
        self.total_ships_coord = self.get_total_ships_coords()
        for bomb in hits_in_this_turn:
            self.bombs_dict[bomb] = LAST_TURN_OF_A_BOMB
        return current_turn_hits, current_turn_terminations

    def __play_one_round(self):

        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. The logic defined by this function must be implemented
        but if you wish to do so in another function (or some other functions)
        it is ok.

        Te function runs one round of the game :
            1. Get user coordinate choice for bombing.
            2. Move all game's ships.
            3. Update all ships and bombs.
            4. Report to the user the result of current round (number of hits
            and terminated ships)
        :return:
            (some constant you may want implement which represents) Game
            status :
            GAME_STATUS_ONGOING if there are still ships on the board or
            GAME_STATUS_ENDED otherwise.
        """

        # Get user coordinates
        self.update_bombs()

        new_bomb = gh.get_target(self.board_size)
        self.bombs_dict[new_bomb] = BOMBS_LIFE
        current_turn_hits, current_turn_terminations = self.update_ships()

        print(gh.board_to_string(self.board_size, current_turn_hits,
                                 self.bombs_dict, self.total_hit_coord,
                                 self.total_ships_coord))
        gh.report_turn(len(current_turn_hits), len(current_turn_terminations))

    def __repr__(self):

        """
        Return a string representation of the board's game
        :return: A tuple converted to string. The tuple should contain
        (maintain the following order):
            1. Board's size.
            2. A dictionary of the bombs found on the board
                 {(pos_x, pos_y) : remaining turns}
                For example :
                 {(0, 1) : 2, (3, 2) : 1}
            3. A list of the ships found on the board (each ship should be
                represented by its __repr__ string).
        """

        return str((self.board_size, self.bombs_dict, self.ships_list))

    def play(self):

        """
        The main driver of the Game. Manages the game until completion.
        completion.
        :return: None
        """

        gh.report_legend()
        print(gh.board_to_string(self.board_size, [], {}, [],
                                 self.get_total_ships_coords()))
        while len(self.terminated_ships) < self.initial_ship_amount:
            self.__play_one_round()
        clear_last_bombs = []
        for bomb in self.bombs_dict:
            for ship in self.ships_list:
                if bomb in ship.coordinates():
                    clear_last_bombs.append(bomb)
        for bomb in clear_last_bombs:
            del self.bombs_dict[bomb]
        self.ships_list = []
        gh.report_gameover()
