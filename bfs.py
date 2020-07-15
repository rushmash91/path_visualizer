from matrix import Matrix
from queue import Queue

start_point = [1, 1]
end_point = [5, 5]
maze = Matrix(7, start_point, end_point)

maze.print_matrix()

q = Queue()
moves = ["R", "L", "U", "D"]
add = ""
q.put("")


def path_validity(maze, test_path):
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
    maze.print_matrix()


def find_end(maze, test_path):
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


while not find_end(maze, add):
    add = q.get()
    for i in moves:
        put = add + i
        if path_validity(maze, put):
            q.put(put)
