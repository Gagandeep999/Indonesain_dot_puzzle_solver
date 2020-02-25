from board import Board
from play_game import play_game
import time


'''
Starting point of the solver
'''


def main():
    input_file_path = input("Enter input file path: ")
    args = open(input_file_path)
    count = 0
    for lines in args:
        size, max_d, max_nodes, initial = lines.split(" ")
        initial = initial.rstrip()
        board = Board(int(size))
        board.initialize_board(initial)
        time_start = time.perf_counter()
        game = play_game(board, max_d, max_nodes, count)
        game._play_game()
        print(time.perf_counter() - time_start)
        count += 1


if __name__ == '__main__':
    main()
