from board import Board
from play_game import PlayGame
import time


def main():
    '''
    Starting point of the application
    :return:
    '''
    # input_file_path = input("Enter input file path: ")
    input_file_path = 'sample_1/test_1.txt'
    args = open(input_file_path)
    count = 0
    for lines in args:
        size, max_d, max_nodes, initial = lines.split(" ")
        initial = initial.rstrip()
        board = Board(int(size))
        board.initialize_board(initial)
        time_start = time.perf_counter()
        game = PlayGame(board, max_d, max_nodes, count, 'dfs')
        game.play_game()
        print("time for dfs : "+str(time.perf_counter() - time_start))
        time_start = time.perf_counter()
        game = PlayGame(board, max_d, max_nodes, count, 'bfs')
        game.play_game()
        print("time for bfs : "+str(time.perf_counter() - time_start))
        time_start = time.perf_counter()
        game = PlayGame(board, max_d, max_nodes, count, 'a*')
        game.play_game()
        print("time for a* : " + str(time.perf_counter() - time_start))
        count += 1


if __name__ == '__main__':
    main()
