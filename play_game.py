# from board import BoardBuilder
from board import Board
import copy


'''
Takes a board as a parameter and has node class in it, each node is initialized with the board.
Creates a root node with initial config and calls check_final_state(board)
Creates children nodes puts them in a stack, and until the level max_d provided in the assignment
then makes a call to the check_final_state() to check.
Nodes need to keep track of parents.
Think about the output files; what kind of useful info to display.
'''


class PlayGame:

    def __init__(self, board, max_d):
        self.board = board
        self.stack = [self.board]
        self.max_d = max_d
        self.current_depth = 0
        self.closed_list = []
        self.children_list = []


    '''
    Takes a position and the board and depending on the position flips surrounding position and returns new board
    '''
    def flip_board(self, i, board):
        size = board.size
        if i % size == 0:
            board.flip(i-size)
            board.flip(i)
            board.flip(i+1)
            board.flip(i+size)
        elif i % size == (size-1):
            board.flip(i-size)
            board.flip(i-1)
            board.flip(i)
            board.flip(i+size)
        else:
            board.flip(i-size)
            board.flip(i-1)
            board.flip(i)
            board.flip(i+1)
            board.flip(i+size)

        return board

    '''
    Helper method to check if the current state of the board is the final state
    '''
    def is_final_state(self, board):

        # if not isinstance(board, Board):
        #     board = Board(board)

        for i, letter in enumerate(board.current_state):
            if board.current_state[i] == 1:
                return False
        return True

    '''
    Check if the children of the current board state are already in the closed_list or not
    '''
    def add_to_stack(self):
        for child in self.children_list:
            count = 0
            for existing in self.closed_list:
                if not isinstance(child, Board):
                    child = Board(child)
                if not isinstance(existing, Board):
                    existing = Board(existing)
                if (not child.is_same_as(existing)):
                    count += 1
            if count == self.closed_list.__len__():
                self.stack.append(child)

    '''
    Helper method to convert the list indices to matrix representation.
    '''

    def lin_to_matrix(self, i, size):
        row = int(i / size) + 97
        col = int(i % size)
        return chr(row)+str(col)

    '''
    This method is used to generate children of a given state of the board.
    It adds a new board configuration to the stack. 
    It takes a board as a parameter and creates a new board for every cell and adds the new board to the stack.
    '''
    def generate_children(self, board):
        self.current_depth += 1
        for i, _ in enumerate(board.current_state):
            prev_board = copy.deepcopy(board)
            new_board = Board(board.size, parent=self.lin_to_matrix(i, board.size))
            new_board.initialize_board(self.flip_board(i, prev_board).current_state)
            self.children_list.append(new_board)


    '''
    This method is where all the action takes place.
    It start with checking if the stack is non empty; pop out the current state and check if it is final
    if final then return success; otherwise generate children and put them in stack; add the current_depth by 1 
    to keep track of the depth of tree.
    '''
    def play_game(self):
        while self.stack.__len__ != 0:
            board = self.stack.pop()
            self.closed_list.append(board)
            board.print_board()
            print()
            #if we have reached the max_d then do not generate more child. Instead pop from the stack and check
            # if (self.currentdepth == max_d)
            #   then current depth - 1
            #   pop size*size kida and check them
            #   if final state is discovered then trace back the parents to find the path
            #else
            #   generate children()
            #   add to stack
            if self.is_final_state(board):
                print('success')

                return
            else:
                self.generate_children(board)
                self.add_to_stack()
                self.children_list = []
                # return
        return 'fail'

