import copy
from board import Board
from mystack import MyStack


class PlayGame:
    """
    The main class where all the action takes place. 
    """

    def __init__(self, max_d, solution, search):
        """
        Declares an open_stack; a closed_stack to keep track of non-visited an visited nodes.
        :param max_d: the max depth allowed for the tree
        """
        self.max_d = max_d
        self.solution_file = solution
        self.search_file = search
        self.open_stack = MyStack()
        self.open_list = []
        self.closed_list = []
        self.solution_stack = MyStack()
        self.solution_found = False

    def flip_board(self, i, board):
        """
        Takes a position and the board and depending on the position flips surrounding position and returns new board
        :param i: postion to flip
        :param board: the board on which the position is to be flipped
        :return: the board with the flipped position and corresponding positions
        """
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

    def is_final_state(self, board):
        """
        Check is the board passed is in final state
        :param board: the board to be checked
        :return: true if it is true state
        """
        list_current_state = list(board.current_state)
        for colour in list_current_state:
            if colour == '1':
                return False
        return True

    def lin_to_matrix(self, i, size):
        """
        Helper method that transform a 1-d representation to a 2-d array indices
        :param i: the position in the linear array
        :param size: size of board
        :return: the corresponding value on a 2-d board
        """
        row = int(i / size) + 65
        col = int(i % size)
        return chr(row)+str(col)

    def generate_children(self, board):
        """
        Generates size*size number of children for a given board config
        :param board: board whose children we want to generate
        :return: adds the children to the open stack
        """
        level = board.level + 1
        for i, _ in enumerate(board.current_state):
            prev_board = copy.deepcopy(board)
            if not isinstance(prev_board, Board):
                prev_board = Board(prev_board)
            new_board_config = self.flip_board(i, prev_board).current_state

            new_board = Board(size=prev_board.size, my_name=self.lin_to_matrix(i, prev_board.size),
                              board=board, level=level)
            new_board.initialize_board(new_board_config)
            # add child to stack and open_list only if it has not been discovered
            if not (new_board.current_state in self.open_list):
                self.open_stack.push(new_board)
                self.open_list.append(new_board_config)

    def backtrack(self, board):
        """
        Method that takes the solution board and recursively backtracks to the parent
        :param board: solution board whose parent is to be traced
        :return: prints to the terminal parents until the root node
        """
        self.solution_stack.push(board)
        if board.my_name != '0':
            self.backtrack(board.parent)
        self.solution_found = True

    def reports(self):
        """
        Method to generate the output files
        :return:
        """
        while not self.solution_stack.is_empty():
            board = self.solution_stack.pop()
            if not isinstance(board, Board):
                board = Board(board)
            print(board.my_name, board.current_state, file=self.solution_file)

    def DFS(self, board):
        """
        Implements the DFS algorithm
        :param board:
        :return:
        """
        self.open_stack.push(board)
        self.open_list.append(board.current_state)
        while self.open_stack.size() != 0 and self.solution_found is False:
            board = self.open_stack.pop()

            if self.is_final_state(board) and self.solution_found is False:
                self.backtrack(board)
                self.reports()
                break

            while board.level == self.max_d and self.solution_found is False:
                print(board.my_name, board.current_state, file=self.search_file)
                if self.is_final_state(board):
                    self.backtrack(board)
                    self.reports()
                    break
                if self.open_stack.is_empty():
                    break
                board = self.open_stack.pop()

            if board.level < self.max_d and self.solution_found is False:
                print(board.my_name, board.current_state, file=self.search_file)
                self.generate_children(board)

        if self.solution_found is False:
            print('no solution', file=self.solution_file)
