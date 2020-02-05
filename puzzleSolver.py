from board import Board
from play_game import PlayGame


'''
Starting point of the solver
'''


def main():
    # input_file_path = input("Enter input file path: ")

    # b1 = Board(3, '0')
    # b2 = Board(3, '1')
    # b1.initialize_board('010111010')
    # b2.initialize_board('010111010')
    # b1.print_board()
    # b2.print_board()
    # print(b1.is_same_as(b2))

    input_file_path = 'sample/test.txt'
    args = open(input_file_path)
    for lines in args:
        n, max_d, _, initial = lines.split(" ")
        initial = initial.rstrip()
        board = Board(size=int(n), my_name='0', parent_name=None, level=0)
        board.initialize_board(initial)
        # board.print_board
        game = PlayGame(int(max_d))
        game.play_game(board)


if __name__ == '__main__':
    main()
