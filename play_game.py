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


class myStack:
    def __init__(self):
        self.container = []  # You don't want to assign [] to self - when you do that, you're just assigning to a new local variable called `self`.  You want your stack to *have* a list, not *be* a list.

    def isEmpty(self):
        return self.size() == 0  # While there's nothing wrong with self.container == [], there is a builtin function for that purpose, so we may as well use it.  And while we're at it, it's often nice to use your own internal functions, so behavior is more consistent.

    def push(self, item):
        self.container.append(item)  # appending to the *container*, not the instance itself.

    def pop(self):
        return self.container.pop()  # pop from the container, this was fixed from the old version which was wrong

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack empty!")
        return self.container[-1]  # View element at top of the stack

    def size(self):
        return len(self.container)  # length of the container

    def show(self):
        return self.container  # display the entire stack as list


class PlayGame:

    def __init__(self, max_d):
        # self.board = board
        self.open_stack = myStack()
        self.max_d = max_d
        self.current_depth = 0
        self.closed_stack = myStack()
        self.children_list = []
        self.solution_found = False


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
                if not child.is_same_as(existing):
                    count += 1
            if count == self.closed_list.__len__():
                self.stack.push(child)

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
        level = board.level + 1
        for i, _ in enumerate(board.current_state):
            prev_board = copy.deepcopy(board)
            new_board = Board(size=prev_board.size, my_name=self.lin_to_matrix(i, prev_board.size),
                              parent_name=prev_board.my_name, level=level)
            new_board.initialize_board(self.flip_board(i, prev_board).current_state)
            self.open_stack.push(new_board)

    def backtrack(self, board):
        '''
        method that takes the solution board and backtracks to the parent
        :param board:
        :return:
        '''

        while board.my_name != '0':
            board_parent = self.closed_stack.pop()
            if not isinstance(board_parent, Board):
                board_parent = Board(board_parent)
            if board.parent_name == board_parent.my_name and board_parent.level == board.level-1:
                board_parent.print_board()
                print()
                self.backtrack(board_parent)
                return

        # for board_parent in self.closed_list:
        #     if board.parent_name == board_parent.my_name and board_parent.level == board.level-1\
        #             and board.parent_name is not None:
        #         board_parent.print_board()
        #         print()
        #         self.backtrack(board_parent)
        #         return

    '''
    This method is where all the action takes place.
    It start with checking if the stack is non empty; pop out the current state and check if it is final
    if final then return success; otherwise generate children and put them in stack; add the current_depth by 1 
    to keep track of the depth of tree.
    '''
    def play_game(self, board):
        '''
        remove board from stack and add to closed list
        if board.level != max_depth
            generate child with level++ and add to child_list
            discard already discovered boards with same config
            put the remaining in the stack
        else
            while board.level == max_depth
                check if final state
                then pop from board; this was the last one is not popped
        :return:
        '''
        self.open_stack.push(board)
        while self.open_stack.size() != 0 and self.solution_found is False:
            board = self.open_stack.pop()

            while board.level == self.max_d and self.solution_found is False:
                if self.is_final_state(board):
                    print('final state found beak loop')
                    board.print_board()
                    print()
                    self.backtrack(board)
                    self.solution_found = True
                    break
                board = self.open_stack.pop()

            if self.is_final_state(board) and self.solution_found is False:
                print('final state found')
                board.print_board()
                print()
                self.backtrack(board)
                self.solution_found = True

            if board.level < self.max_d and self.solution_found is False:
                self.generate_children(board)

            self.closed_stack.push(board)

        if self.solution_found is False:
            print('no solution')
