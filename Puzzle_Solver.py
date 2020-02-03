from board import Board
from play_game import Play_Game


'''
Starting point of the solver
'''


def main():
    # input_file_path = input("Enter input file path: ")
    input_file_path = 'sample_1/test_1.txt'
    args = open(input_file_path)
    count = 0
    for lines in args:
        size, max_d, max_nodes, initial = lines.split(" ")
        initial = initial.rstrip()
        board = Board(int(size))
        board.initialize_board(initial)
        # board.print_board

        game = Play_Game(board, max_d, max_nodes, count)
        game.play_game()
        count += 1


if __name__ == '__main__':
    main()