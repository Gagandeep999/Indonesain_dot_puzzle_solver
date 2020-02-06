from board import Board
from play_game import PlayGame


def main():
    """
    Starting point of the application
    :return:
    """
    # input_file_path = input('Enter file path:')
    input_file_path = 'sample/test.txt'
    args = open(input_file_path)
    for i, lines in enumerate(args):
        solution = open('./sample/' + str(i) + '_my_dfs_solution.txt', 'w')
        search = open('./sample/' + str(i) + '_my_dfs_search.txt', 'w')
        n, max_d, _, initial = lines.split(' ')
        initial = initial.rstrip()
        # initialize the root node with name as 0; parent as None and level as 0.
        board = Board(size=int(n), my_name='0', parent_name=None, level=0)
        board.initialize_board(initial)
        game = PlayGame(max_d=int(max_d), solution=solution, search=search)
        game.DFS(board=board)


if __name__ == '__main__':
    main()
