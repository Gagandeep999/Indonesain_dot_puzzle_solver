import copy


class Play_Game():

    def __init__(self, board, max_d, max_node):
        self.board = board
        self.stack = [self.board]
        self.parentMap = {}
        self.visits = []
        self.max_d = int(max_d)
        self.max_node = int(max_node)
        self.depth = {}
    '''
    Takes a position and the board and depending on the position flips surrounding position and returns new board
    '''

    def flip_board(self, i, board):
        size = board.size
        parent = copy.deepcopy(board)
        board_1 = copy.deepcopy(board)
        if i % size == 0:
            board_1.flip(i - size)
            board_1.flip(i)
            board_1.flip(i + 1)
            board_1.flip(i + size)
        elif i % size == (size - 1):
            board_1.flip(i - size)
            board_1.flip(i - 1)
            board_1.flip(i)
            board_1.flip(i + size)
        else:
            board_1.flip(i - size)
            board_1.flip(i - 1)
            board_1.flip(i)
            board_1.flip(i + 1)
            board_1.flip(i + size)
        if str(board_1.current_state) not in self.parentMap:
            self.parentMap[str(board_1.current_state)] = str(parent.current_state)
        return board_1

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
        for i in range(board.size*board.size-1, -1, -1):
            kid = self.flip_board(i, board)
            if str(kid.current_state) not in self.visits:
                self.stack.append(kid)
                # gets the parents depth and adds to that
                self.depth[str(kid.current_state)] = self.depth.get((self.parentMap.get(str(kid.current_state)))) + 1
        pass

    '''
    This method is where all the action takes place.
    It start with checking if the stack is non empty; pop out the current state and check if it is final
    if final then return success; otherwise generate children and put them in stack; add the current_depth by 1 
    to keep track of the depth of tree.
    '''

    def play_game(self):
        self.parentMap[str(self.board.current_state)] = "root"
        self.depth[str(self.board.current_state)] = 0
        while self.stack.__len__() != 0:
            new_board = self.stack.pop()
            if self.is_final_state(new_board):
                self.generate_report()
                return
            # if we still can go deeper into the tree
            if self.max_d > self.depth.get(str(new_board.current_state)):
                # have we reached the max node count.
                if self.max_node > self.visits.__len__() and self.max_d > 0:
                    # node hasnt been visited yet
                    if str(new_board.current_state) not in self.stack:
                        self.visits.append(str(new_board.current_state))
                        self.generate_children(new_board)
                else:
                    # generate_failed_report()
                    self.stack.clear()
        print("no solution exists")
        return


    def generate_report(self):
        print('success')
        state = str([0 for i in range(self.board.size * self.board.size)])
        # print(parentMap)
        print(state)
        while self.parentMap.get(state) != "root":
            print(self.parentMap.get(state))
            state = self.parentMap.get(state)
        # method for printing all the appropriate shit