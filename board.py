class Board:

    def __init__(self, size):
        self.size = size
        self.current = [0 for i in range(size*size)]

    def print_board(self):
        pos = 0
        for i in range(self.size):
            for j in range(self.size):
                print(self.current[pos], end=" ")
                pos += 1
            print()

    def initialize_board(self, initial):
        for i,letter in enumerate(initial):
            # print('at pos {0} letter is {1}'.format(i, letter))
            # print(type(letter))
            self.current[i] = int(letter)

    def flip(self):
        pass
