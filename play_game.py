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
            # assuming we get the best leading 0s image.

            #  check if this entry already exists and must be modified
            if str(kid.current_state) in self.depth:
                # if we find that this board has already been visited but that this board now has a faster way/
                # less depth then replace old value of parent
                if self.depth[str(kid.current_state)] > self.depth[str(board.current_state)] + 1:  # old value vs new one
                    self.parentMap[str(kid.current_state)] = str(board.current_state)
                    self.depth[str(kid.current_state)] = self.depth.get((self.parentMap.get(str(kid.current_state)))) + 1
                    self.stack.append(kid)
                    # here is where you will input the f(n), g(n) or h(n)
                    g = 0
                    h = 0
                    f = 0
                    self.search_file.write("\n" + self.lin_to_matrix(i, board.size) + "  " + str(f) + "  " + str(g) + "  " + str(h) + "  " + str(kid.current_state))

                # else:
                # do nothing cause faster way to get to this node.
            else:
                self.parentMap[str(kid.current_state)] = str(board.current_state)
                self.depth[str(kid.current_state)] = self.depth.get((self.parentMap.get(str(kid.current_state)))) + 1
                self.stack.append(kid)
                # here is where you will input the f(n), g(n) or h(n)
                g = 0
                h = 0
                f = 0
                self.search_file.write("\n" + self.lin_to_matrix(i, board.size) + "  " + str(f) + "  " + str(g) + "  " + str(h) + "  " + str(kid.current_state))

        pass

    def generate_children_bfs(self, board):
        for i in range(board.size * board.size - 1, -1, -1):
            kid = self.flip_board(i, board)
            # assuming we get the best leading 0s image.

            #  check if this entry already exists and must be modified
            if str(kid.current_state) in self.depth:
                # if we find that this board has already been visited but that this board now has a faster way/
                # less depth then replace old value of parent
                if self.depth[str(kid.current_state)] > self.depth[str(board.current_state)] + 1:  # old value vs new one
                    self.parentMap[str(kid.current_state)] = str(board.current_state)
                    self.depth[str(kid.current_state)] = self.depth.get((self.parentMap.get(str(kid.current_state)))) + 1
                    self.stack.append(kid)
                    # here is where you will input the f(n), g(n) or h(n)
                    g = 0
                    h = self.return_state_as_integer(kid)
                    f = int(g) + int(h)
                    self.search_file.write("\n" + self.lin_to_matrix(i, board.size) + "  " + str(f) + "  " + str(g) + "  " + str(h) + "  " + str(kid.current_state))

                # else:
                # do nothing cause faster way to get to this node.
            else:
                self.parentMap[str(kid.current_state)] = str(board.current_state)
                self.depth[str(kid.current_state)] = self.depth.get((self.parentMap.get(str(kid.current_state)))) + 1
                self.stack.append(kid)
                # here is where you will input the f(n), g(n) or h(n)
                g = 0
                h = self.return_state_as_integer(kid)
                f = int(g) + int(h)
                self.search_file.write("\n" + self.lin_to_matrix(i, board.size) + "  " + str(f) + "  " + str(g) + "  " + str(h) + "  " + str(kid.current_state))

        pass

    def generate_children_a(self, board):
        for i in range(board.size * board.size - 1, -1, -1):
            kid = self.flip_board(i, board)
            # extra for performance would be assuming we get the best leading 0s image. future improvement

            #  check if this entry already exists and must be modified
            if str(kid.current_state) in self.depth:
                # if we find that this board has already been visited but that this board now has a faster way/
                # less depth then replace old value of parent
                if self.depth[str(kid.current_state)] > self.depth[str(board.current_state)] + 1:  # old value vs new one
                    self.parentMap[str(kid.current_state)] = str(board.current_state)
                    self.depth[str(kid.current_state)] = self.depth.get((self.parentMap.get(str(kid.current_state)))) + 1
                    #
                    kid.fn = self.return_state_as_integer(kid) + self.add_depth_cost(kid)
                    #
                    self.stack.append(kid)
                    g = self.depth[str(kid.current_state)]
                    h = self.add_depth_cost(kid)
                    f = int(g) + int(h)
                    self.search_file.write("\n"+self.lin_to_matrix(i, board.size) + "  " + str(f) + "  " + str(g) + "  " + str(h) + "  " + str(kid.current_state))

                # else:
                # do nothing cause faster way to get to this node.
            else:
                self.parentMap[str(kid.current_state)] = str(board.current_state)
                self.depth[str(kid.current_state)] = self.depth.get((self.parentMap.get(str(kid.current_state)))) + 1
                self.stack.append(kid)
                #
                kid.fn = self.return_state_as_integer(kid) + self.add_depth_cost(kid)
                #
                self.stack.append(kid)
                g = self.add_depth_cost(kid)
                h = self.return_state_as_integer(kid)
                f = int(g) + int(h)
                self.search_file.write("\n" + self.lin_to_matrix(i, board.size) + "  " + str(f) + "  " + str(g) + "  " + str(h) + "  " + str(kid.current_state))

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
        self.search_file.write("0  0  0  0  " + str(self.board.current_state))
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
                    # if str(new_board.current_state) not in self.stack:
                    self.visits.append(str(new_board.current_state))
                    if self.type == 'dfs':
                        self.generate_children_dfs(new_board)
                    if self.type == 'bfs':
                        self.generate_children_bfs(new_board)
                        # extra step to fix the stack so it becomes BFS
                        self.stack.sort(key=self.return_state_as_integer, reverse=True)
                    if self.type == "a*":
                        self.generate_children_a(new_board)
                        # sort based on f(n)
                        self.stack.sort(key=self.return_fn, reverse=True)
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

    def add_depth_cost(self, board):
        depth = [0 for i in range(board.size * board.size)]
        depth[0] = self.depth[str(board.current_state)]
        number = int("".join(map(str, depth)))
        return number

    def return_fn(self, board):
        return board.fn