from matrix import Matrix
from queue import Queue

start_point = [1, 1]
end_point = [4, 4]
maze = Matrix(5, start_point, end_point)

maze.print_matrix()

q = Queue()
moves = ["R", "L", "U", "D"]
add = ""
q.put("")


def path_validity(maze, test_path):
    maze.start = start_point
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
    if val == "Out of Matrix":
        return False
    else:
        return True


while maze.path_found:
    pass

print(path_validity(maze, "LURDDDDDDD"))
