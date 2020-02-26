import copy

stack = []
visited = []
parentMap = {}


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
    parentMap[str(board)] = "root"
    # print("current board")
    # for line in board:
    #     print(line)
    line = f.readline()
    final_state = [[-1] * int(size)] * int(size)
    #kids = get_kids(board, int(size))
    # for x in kids:
    #     print("\n possibility")
    #     for line in x:
    #         print(line)
    # result_DFS(board, final_state, int(size));
    done = dfs(board, int(size), visited, final_state)
    state = str(final_state)
    # print(parentMap)
    if done:
        print(state)
        while parentMap.get(state) != "root":
            print(parentMap.get(state))
            state = parentMap.get(state)


#   for child in children:
#         stack.push(child[0])
#         parentMap[child] = parent #this line was added
# Later on, when you found your target, you can get the path from the source to the target (pseudo code):
#
# curr = target
# while (curr != None):
#   print curr
#   curr = parentMap[curr]

def dfs(board, size, visits, final):
    stack.append(board)
    while stack:
        current = stack.pop()
        kids = get_kids(current, size)
        visits.append(current)
        for kid in kids:
            if kid == final:
                return True
            if kid not in visited:
                stack.append(kid)
    return False


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


# return list of kids
def get_kids(current, SIZE):
    size = SIZE - 1
    kids = []
    for i in range(size, -1, -1):
        for j in range(size, -1, -1):
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
            if str(kid) not in parentMap:
                parentMap[str(kid)] = str(current)

    return kids


if __name__ == "__main__":
    main()

# def dfs(board, size, visits):
#     if node not in visited:
#         visited.append(node)
#         for n in graph[node]:
#             dfs(graph, n, visited)
#     return visited
