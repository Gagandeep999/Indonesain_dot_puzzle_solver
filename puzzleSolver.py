from board import Board
from play_game import PlayGame
import time

def main():
    """
    Starting point of the application
    :return:
    """
    # input_file_path = input('Enter file path:')
    input_file_path = 'sample/test1.txt'
    args = open(input_file_path)
    for i, lines in enumerate(args):
        solution = open('./sample/' + str(i) + '_my_dfs_solution.txt', 'w')
        search = open('./sample/' + str(i) + '_my_dfs_search.txt', 'w')
        n, max_d, _, initial = lines.split(' ')
        initial = initial.rstrip()
        # initialize the root node with name as 0; parent as None and level as 0.
        board = Board(size=int(n), my_name='0', board=None, level=0)
        board.initialize_board(initial)
        time_start = time.perf_counter()
        game = PlayGame(max_d=int(max_d), solution=solution, search=search)
        game.DFS(board=board)
        print(time.perf_counter() - time_start)


if __name__ == '__main__':
    main()
