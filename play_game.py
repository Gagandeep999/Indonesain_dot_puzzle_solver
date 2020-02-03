'''
Takes a board as a parameter and has node class in it, each node is initialized with the board.
Creates a root node with initial config and calls check_final_state(board)
Creates children nodes puts them in a stack, and until the level max_d provided in the assignment
then makes a call to the check_final_state() to check.
Nodes need to keep track of parents.
Think about the output files; what kind of useful info to display.
'''
class Play_Game():

    def __init__(self, board, max_d):
        self.board = board
        self.stack = [self.board]
        self.max_d = max_d
        self.current_depth = 1

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
        for i, letter in enumerate(board.current_state):
            if board.current_state[i] == 1:
                return False
        return True

    '''
    This method is used to generate children of a given state of the board.
    It adds a new board configuration to the stack. 
    It takes a board as a parameter and creates a new board for every cell and adds the new board to the stack.
    '''
    def generate_children(self, board):
        self.current_depth += 1
        for i, _ in enumerate(board.current_state):
            self.stack.append(self.flip_board(i, board))
        pass

    '''
    This method is where all the action takes place.
    It start with checking if the stack is non empty; pop out the current state and check if it is final
    if final then return success; otherwise generate children and put them in stack; add the current_depth by 1 
    to keep track of the depth of tree.
    '''
    def play_game(self):
        while self.stack.__len__ != 0:
            new_board = self.stack.pop()
            if self.is_final_state(new_board):
                print('success')
                return
            else:
                self.generate_children(new_board)
                print('fail')
                return
