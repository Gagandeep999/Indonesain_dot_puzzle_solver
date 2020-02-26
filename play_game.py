import copy


class play_game:

    def __init__(self, board, max_d, max_node, game_number):
        self.board = board
        self.game_number = str(game_number)
        self.stack = [self.board]
        self.parentMap = {}
        self.visits = []
        self.depth = {}
        self.max_d = int(max_d)
        self.max_node = int(max_node)
        self.solution_file = open("./sample/" + self.game_number + "_dfs_solution.txt", "w")
        self.search_file = open("./sample/" + self.game_number + "_dfs_search.txt", "w+")

    def _lin_to_matrix(self, i, size):
        '''
        Helper method to convert the list indices to matrix representation.
        :param i: the index on the board
        :param size: size of the board
        :return: the 2D representation of the linear number
        '''
        row = int(i / size) + 65
        col = int(i % size)
        return chr(row) + str(col)

    def _flip_board(self, i, board):
        '''
        Takes a position and the board and depending on the position flips surrounding position and returns new board
        :param i: position on the board
        :param board: object on which game is being played
        :return: the board object with flipped neighbouring indexes
        '''
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
            self.search_file.write(self._lin_to_matrix(i, board_1.size) + "  "+ str(f) + "  " + str(g) + "  " + str(h)+"  " + str(board_1.current_state) + "\n")
        return board_1

    def _is_final_state(self, board):
        '''
        Checks if the current board in final state or not
        :param board: object on which game is being played
        :return: true if the board is in final state otherwise false
        '''
        for i, letter in enumerate(board.current_state):
            if board.current_state[i] == 1:
                return False
        return True

    def _generate_children(self, board):
        '''
        Method used to generate the children of the current board. Adds a new board with different config to the stack.
        :param board: the parent board whose children we want to generate
        :return: nothing
        '''
        for i in range(board.size * board.size - 1, -1, -1):
            kid = self._flip_board(i, board)
            if str(kid.current_state) not in self.visits:
                self.stack.append(kid)
                # gets the parents depth and adds to that
                self.depth[str(kid.current_state)] = self.depth.get((self.parentMap.get(str(kid.current_state)))) + 1
        pass

    def _play_game(self):
        '''
        The heart of the application. Keeps looping until the stack is empty. Pops a board from the stack and checks
        for final state, if not final, then checks if maximum depth reached or not, then checks if maximum number of
        nodes reached or not; finally if boarn is not in stack then _generate_children() method is called which adds the
        children to the stack.
        If a child is found _generate_report() method is called otherwise "no solution found" is written to the file.
        :return: nothing
        '''
        self.parentMap[str(self.board.current_state)] = "root"
        self.depth[str(self.board.current_state)] = 0
        self.search_file.write("0  0  0  0  "+str(self.board.current_state)+"\n")
        while self.stack.__len__() != 0:
            new_board = self.stack.pop()
            if self._is_final_state(new_board):
                self.search_file.close()
                self._generate_report()
                return
            # if we still can go deeper into the tree
            if self.max_d > self.depth.get(str(new_board.current_state)):
                # have we reached the max node count.
                if self.max_node > self.visits.__len__() and self.max_d > 0:
                    # node hasnt been visited yet
                    if str(new_board.current_state) not in self.stack:
                        self.visits.append(str(new_board.current_state))
                        self._generate_children(new_board)
                else:
                    # generate_failed_report()
                    self.stack.clear()
        self.solution_file.write("no solution found")
        return

    def _generate_report(self):
        '''
        Once the solution is found this method is called which genrates the report.
        :return: nothing
        '''
        self.search_file = open("./sample/" + self.game_number + "_dfs_search.txt", "r")
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
                    elements.append(move + "  " + current+"\n")
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
