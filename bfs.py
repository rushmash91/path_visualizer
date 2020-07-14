import queue
from matrix import Matrix


def print_maze(maze, path=""):
    i = maze.start[0]
    j = maze.start[1]
    pos = set()
    for move in path:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1
        pos.add((i, j))

    for i, row in enumerate(maze.get_matrix()):
        for j, col in enumerate(row):
            if (i, j) in pos:
                maze.set_value(i, j, "+")

    maze.print_matrix()


def validity(maze, moves):
    i = maze.start[0]
    j = maze.start[1]
    for move in moves:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1

        if not (0 <= j < len(maze.get_matrix()[0]) and 0 <= i < len(maze.get_matrix())):
            return False

        elif maze.get_matrix()[i][j] == "#":
            return False

    return True


def find_end(maze, moves):
    i = maze.start[0]
    j = maze.start[1]
    for move in moves:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1

    if maze.get_matrix()[i][j] == "#":
        print("Found: " + moves)
        print_maze(maze, moves)
        return True

    return False


q = queue.Queue()
q.put("")
path = ""
maze = Matrix(3, [0, 0], [2, 2])

while not find_end(maze, path):
    add = q.get()
    # print(add)
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if validity(maze, put):
            q.put(put)
