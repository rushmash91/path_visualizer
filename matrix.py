class Matrix:
    def __init__(self, n, start_point, end_point):
        self.matrix = [0 for i in range(n*n)]
        self.start = start_point
        self.end = end_point
        self.current_row = start_point[0]
        self.current_column = start_point[1]
        self.size = n
        self.reference = []
        for i in range(int(self.size)):
            row = []
            for j in range(int(self.size)):
                row.append(self.matrix[i])
            self.reference.append(row)
        self.reference[self.start[0]][self.start[1]] = "*"
        self.reference[self.end[0]][self.end[1]] = "+"

    def get_element(self, row, column):
        return self.reference[row][column]

    def get_matrix(self):
        return self.reference

    def set_value(self, row, column, value):
        self.reference[row][column] = value
        return self.reference[row][column]

    def up(self):
        try:
            if self.reference[self.current_row - 1][self.current_column] == 0:
                self.reference[self.current_row - 1][self.current_column] = 1
                self.current_row -= 1
                return self.current_row, self.current_column
            elif self.reference[self.current_row - 1][self.current_column] == "+":
                return print("End")
            elif self.reference[self.current_row - 1][self.current_column] == "*":
                return print("Back to Start")
        except IndexError:
            print("Out of Matrix")

    def down(self):
        try:
            if self.reference[self.current_row + 1][self.current_column] == 0:
                self.reference[self.current_row + 1][self.current_column] = 1
                self.current_row += 1
                return self.current_row, self.current_column
            elif self.reference[self.current_row + 1][self.current_column] == "+":
                return print("End")
            elif self.reference[self.current_row + 1][self.current_column] == "*":
                return print("Back to Start")
        except IndexError:
            print("Out of Matrix")

    def right(self):
        try:
            if self.reference[self.current_row][self.current_column + 1] == 0:
                self.reference[self.current_row][self.current_column + 1] = 1
                self.current_column += 1
                return self.current_row, self.current_column
            elif self.reference[self.current_row][self.current_column + 1] == "+":
                return print("End")
            elif self.reference[self.current_row][self.current_column + 1] == "*":
                return print("Back to Start")
        except IndexError:
            print("Out of Matrix")

    def left(self):
        try:
            if self.reference[self.current_row][self.current_column - 1] == 0:
                self.reference[self.current_row][self.current_column - 1] = 1
                self.current_column -= 1
                return self.current_row, self.current_column
            elif self.reference[self.current_row][self.current_column - 1] == "+":
                return print("End")
            elif self.reference[self.current_row][self.current_column - 1] == "*":
                return print("Back to Start")
        except IndexError:
            print("Out of Matrix")

    def print_matrix(self):
        for row in self.reference:
            for j in row:
                print(j, end=' ')
            print('\n')


mrx = Matrix(5, [2, 2], [4, 4])
mrx.print_matrix()
mrx.down()
mrx.down()
mrx.right()
mrx.print_matrix()
