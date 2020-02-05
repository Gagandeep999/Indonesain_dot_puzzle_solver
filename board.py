class Board:

    def __init__(self, size, my_name, parent_name, level):
        self.size = size
        self.current_state = [0 for i in range(self.size*self.size)]
        self.my_name = my_name
        self.parent_name = parent_name
        self.level = level

    def print_board(self):
        print(self.my_name, end=" ")
        pos = 0
        for i in range(self.size):
            for j in range(self.size):
                print(self.current_state[pos], end=" ")
                pos += 1
            # print()

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

    def is_same_as(self, board):
        for i, _ in enumerate(board.current_state):
            if self.current_state[i] != board.current_state[i]:
                return False
        return True
