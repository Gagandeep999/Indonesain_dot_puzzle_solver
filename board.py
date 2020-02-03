class Board:

    def __init__(self, size):
        self.size = size
        self.current_state = [0 for i in range(self.size*self.size)]

    def print_board(self):
        pos = 0
        for i in range(self.size):
            for j in range(self.size):
                print(self.current_state[pos], end=" ")
                pos += 1
            print()

    def initialize_board(self, initial):
        for i, letter in enumerate(initial):
            self.current_state[i] = int(letter)

    def flip(self, pos):
        if pos < 0 or pos > (self.size*self.size-1):
            pass
        elif self.current_state[pos] == 1:
            self.current_state[pos] = 0
        else:
            self.current_state[pos] = 1

    def is_same_to(self, board):
        for i in enumerate(board.current_state):
            if self.current_state[i] != board.current_state[i]:
                return False
            return True


class BoardBuilder(object):

    def __init__(self, size):
        self.size = size
        self.current_state = None

    def build(self):
        return Board(self.size, self.current_state)