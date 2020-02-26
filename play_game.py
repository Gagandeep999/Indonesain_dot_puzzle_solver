import copy


class Play_Game:

    def __init__(self, board, max_d, max_node, game_number, type):
        self.type = type
        self.board = board
        self.game_number = str(game_number)
        self.stack = [self.board]
        self.parentMap = {}
        self.visits = []
        self.depth = {}
        self.max_d = int(max_d)
        self.max_node = int(max_node)
        self.solution_file = open("./sample_1/" + self.game_number + "_"+type+"_solution.txt", "w")
        self.search_file = open("./sample_1/" + self.game_number + "_"+type+"_search.txt", "w+")

    '''
        Helper method to convert the list indices to matrix representation.
        '''

    def lin_to_matrix(self, i, size):
        row = int(i / size) + 65
        col = int(i % size)
        return chr(row) + str(col)

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
            # here is where you will input the f(n), g(n) or h(n)
            f = 0
            g = 0
            h = 0
            self.search_file.write(self.lin_to_matrix(i, board_1.size) + "  " + str(f) + "  " + str(g) + "  " + str(h) + "  " + str(board_1.current_state) + "\n")
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

    def generate_children_dfs(self, board):
        for i in range(board.size * board.size - 1, -1, -1):
            kid = self.flip_board(i, board)
            if str(kid.current_state) not in self.visits:
                self.stack.append(kid)
                # gets the parents depth and adds to that
                self.depth[str(kid.current_state)] = self.depth.get((self.parentMap.get(str(kid.current_state)))) + 1
        pass

    def generate_children_bfs(self, board):
        # create a temporary variable to store the "unsorted" children
        temp = []
        for i in range(board.size * board.size - 1, -1, -1):
            # add he generated children to the temp
            temp.append(self.flip_board(i, board))
        # here we rearrange the temp to have the correct order of the desired/favored children
        temp.sort(key=self.return_state_as_integer, reverse=True)
        for kid in temp:
            if str(kid.current_state) not in self.visits:
                self.stack.append(kid)
                # gets the parents depth and adds to that
                self.depth[str(kid.current_state)] = self.depth.get((self.parentMap.get(str(kid.current_state)))) + 1
        pass

    #  get the current board as an Integer which we use to sort the array
    def return_state_as_integer(self, board):
        number = int("".join(map(str, board.current_state)))
        return number

    '''
    This method is where all the action takes place.
    It start with checking if the stack is non empty; pop out the current state and check if it is final
    if final then return success; otherwise generate children and put them in stack; add the current_depth by 1 
    to keep track of the depth of tree.
    '''

    def play_game(self):
        self.parentMap[str(self.board.current_state)] = "root"
        self.depth[str(self.board.current_state)] = 0
        self.search_file.write("0  0  0  0  " + str(self.board.current_state) + "\n")
        while self.stack.__len__() != 0:
            new_board = self.stack.pop()
            if self.is_final_state(new_board):
                self.search_file.close()
                self.generate_report()
                return
            # if we still can go deeper into the tree
            if self.max_d > self.depth.get(str(new_board.current_state)):
                # have we reached the max node count.
                if (self.max_node > self.visits.__len__() and self.max_d > 0) or self.type == 'dfs':
                    # node hasnt been visited yet
                    if str(new_board.current_state) not in self.stack:
                        self.visits.append(str(new_board.current_state))
                        if self.type == 'dfs':
                            self.generate_children_dfs(new_board)
                        if self.type == 'bfs':
                            self.generate_children_bfs(new_board)
                else:
                    # generate_failed_report()
                    self.stack.clear()
        self.solution_file.write("no solution found")
        return

    def generate_report(self):

        self.search_file = open("./sample_1/" + self.game_number + "_"+self.type+"_search.txt", "r")
        count = 1
        elements = []
        while True:
            if count == 1:
                current = str([0 for i in range(self.board.size * self.board.size)])
                count -= 1
            else:
                current = self.parentMap.get(str(current))
            while current != "root":
                line = self.search_file.readline()
                move, f, g, h, board_info = line.split("  ")
                board_info = board_info.rstrip()
                if board_info == current:
                    elements.append(move + "  " + current + "\n")
                    self.search_file.seek(0)
                    break
                if move == "0" and current == board_info:
                    loop = False
                    self.search_file.close()
                    break
            if current == "root":
                break
        for line in elements:
            self.solution_file.write(line)
        self.solution_file.close()
