class Board:

    def __init__(self, size):
        self.size = size
        self.current_state = [0 for _ in range(self.size*self.size)]
        self.fn = 0

    def initialize_board(self, initial):
        """
        :param initial: the config of the board to be initialized with
        :return: the current state of the board as an integer value
        """
        for i, letter in enumerate(initial):
            self.current_state[i] = int(letter)

    def flip(self, pos):
        """
        Flips only on position of the board
        :param pos: The position to flip
        :return: Same board with flipped config
        """
        if pos < 0 or pos > (self.size*self.size-1):
            pass
        elif self.current_state[pos] == 1:
            self.current_state[pos] = 0
        else:
            self.current_state[pos] = 1

    def is_same_to(self, board):
        """
        Method to compare two board configurations
        :param board:
        :return: a boolean value
        """
        for i in enumerate(board.current_state):
            if self.current_state[i] != board.current_state[i]:
                return False
            return True
