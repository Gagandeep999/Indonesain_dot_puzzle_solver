class Board:
    """
    This is the board class on which the game is played.
    """

    def __init__(self, size, my_name, board, level):
        """
        Constructor of the board; initialized with all 0's
        :param size: size of the board eg 3 for a 3X3 board
        :param my_name: name of the board depending on the token touched
        :param parent_name: name of the board on which the token was touched
        :param level: depth of the tree
        """
        self.size = size
        self.current_state = ''
        self.my_name = my_name
        self.parent = board
        self.level = level

    def print_board(self):
        """
        Prints the board
        :return: prints the board to the terminal
        """
        print(self.my_name, end=" ")
        print(self.current_state)

    def initialize_board(self, config):
        """
        This method takes a configuration of the board and initializes it to that config
        :param config: the configuration passed as a string
        :return: initialize the board with config
        """
        self.current_state = config

    def flip(self, pos):
        """
        Method to flip the tokens
        :param pos: index of the token on the board to flip
        :return: the opposite of what was passed
        """
        list_to_string = ''
        list_current_state = list(self.current_state)
        if pos < 0 or pos > (self.size*self.size-1):
            pass
        elif list_current_state[pos] == '1':
            list_current_state[pos] = '0'
        else:
            list_current_state[pos] = '1'
        self.current_state = list_to_string.join(list_current_state)

    def is_same_as(self, board):
        """
        This method compares two board objects
        :param board: board object
        :return: true if they are same
        """
        if self.current_state != board.current_state:
            return False
        return True
