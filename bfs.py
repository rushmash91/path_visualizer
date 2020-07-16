from matrix import Matrix
from queue import Queue


def path_validity(maze, test_path, start_point):
    maze.current_row = start_point[0]
    maze.current_column = start_point[1]
    val = ""
    for step in test_path:
        if val == "Out of Matrix":
            break
        if step == "R":
            val = maze.right()
        elif step == "L":
            val = maze.left()
        elif step == "U":
            val = maze.up()
        elif step == "D":
            val = maze.down()
    if val == "Out of Matrix":
        return False
    else:
        return True


def final_path(maze, path):
    maze.clear_paths()
    for step in path:
        if step == "R":
            maze.right()
        elif step == "L":
            maze.left()
        elif step == "U":
            maze.up()
        elif step == "D":
            maze.down()


def find_end(maze, test_path, start_point):
    val = ""
    maze.current_row = start_point[0]
    maze.current_column = start_point[1]

    for step in test_path:
        if step == "R":
            val = maze.right()
        elif step == "L":
            val = maze.left()
        elif step == "U":
            val = maze.up()
        elif step == "D":
            val = maze.down()
        else:
            val = ""
    if val == "End":
        final_path(maze, test_path)
        return True
    else:
        return False


def bfs(maze, start_point):
    # Breath First Algorithm
    q = Queue()
    moves = ["R", "L", "U", "D"]
    add = ""
    q.put("")
    while not find_end(maze, add, start_point):
        add = q.get()
        for i in moves:
            put = add + i
            if path_validity(maze, put, start_point):
                q.put(put)


def main():
    start_point = [1, 3]
    end_point = [4, 4]
    maze = Matrix(5, start_point, end_point)
    maze.print_matrix()
    bfs(maze, start_point)
    maze.print_matrix()


if __name__ == '__main__':
    main()
