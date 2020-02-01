from board import Board

'''
Starting point of the solver
'''
def main():
    # read a file and initialize values
    # input_file_path = input("Enter input file path: ")
    input_file_path = 'sample/test.txt'
    args = open(input_file_path)
    for lines in args:
        n, max_d, _, initial = lines.split(" ")
        initial = initial.rstrip()
        # print(type(n))
        # print(type(inital))
        board = Board(int(n))
        # board.print_board()
        board.initialize_board(initial)
        board.print_board()


if __name__ == '__main__':
    main()
