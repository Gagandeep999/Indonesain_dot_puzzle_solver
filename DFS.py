import copy

stack = []
visited = []


def main():
    f = open("./sample/test.txt", "r")
    count = 0
    line = f.readline()
    # while line != "":
    count += 1
    parameters = line.split()
    size = parameters[0]
    max_d = parameters[1]
    max_search_path = parameters[2]
    board_info = parameters[3]
    board = populate_board(size, board_info)
    print("current board")
    for line in board:
        print(line)
    line = f.readline()
    final_state = [[0] * int(size)] * int(size)
    kids = get_kids(board, int(size))
    for x in kids:
        print("\n possibility")
        for line in x:
            print(line)
    # result_DFS(board, final_state, int(size));


# graph = {}
# visited = dfs(board, 'A', [])
# print(visited)

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


def populate_board(size, board_info):
    data = [[2 for x in range(int(size))] for y in range(int(size))]
    count = -1
    for i in range(int(size)):
        count += 1
        for j in range(int(size)):
            if board_info[i * int(size) + j] == "0":
                data[i][j] = int("-1")
            else:
                data[i][j] = int(board_info[i * int(size) + j])
    return data


def get_kids(current, SIZE):
    size = SIZE - 1
    kids = []
    for i in range(SIZE):
        for j in range(SIZE):
            kid = copy.deepcopy(current)
            if i == 0 and j == 0:
                kid[i][j] *= -1
                kid[i][j + 1] *= -1
                kid[i + 1][j] *= -1
            elif i == size and j == size:
                kid[i][j] *= -1
                kid[i][j - 1] *= -1
                kid[i - 1][j] *= -1
            elif i == 0 and j == size:
                kid[i][j] *= -1
                kid[i][j - 1] *= -1
                kid[i + 1][j] *= -1
            elif i == size and j == 0:
                kid[i][j] *= -1
                kid[i][j + 1] *= -1
                kid[i - 1][j] *= -1
            elif i == 0:
                kid[i][j] *= -1
                kid[i][j + 1] *= -1
                kid[i][j - 1] *= -1
                kid[i + 1][j] *= -1
            elif i == size:
                kid[i][j] *= -1
                kid[i][j + 1] *= -1
                kid[i][j - 1] *= -1
                kid[i - 1][j] *= -1
            elif j == 0:
                kid[i][j] *= -1
                kid[i][j + 1] *= -1
                kid[i + 1][j] *= -1
                kid[i - 1][j] *= -1
            elif j == size:
                kid[i][j] *= -1
                kid[i][j - 1] *= -1
                kid[i - 1][j] *= -1
                kid[i + 1][j] *= -1
            else:
                kid[i][j] *= -1
                kid[i][j - 1] *= -1
                kid[i][j + 1] *= -1
                kid[i - 1][j] *= -1
                kid[i + 1][j] *= -1
            kids.append(kid)
    return kids


def result_DFS(board, final_state, size):
    stack.append(board)
    while stack:
        current = stack.pop()
        kids = get_kids(current, size)
    return


if __name__ == "__main__":
    main()