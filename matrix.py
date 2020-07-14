import math


class Matrix:
    def __init__(self, matrix):
        self.size = math.sqrt(len(matrix))
        self.matrix = matrix
        self.reference = []
        for i in range(int(self.size)):
            row = []
            for j in range(int(self.size)):
                row.append(self.matrix[i])
            self.reference.append(row)

    def index(self, row, column):
        return self.reference[row][column]

    def get_matrix(self):
        return self.reference

    def set_value(self, row, column, value):
        self.reference[row][column] = value
        return self.reference[row][column]

    def up(self, row, column):
        if self.reference[row - 1][column] == 0:
            self.reference[row - 1][column] = 1
        return self.reference[row - 1][column]

    def down(self, row, column):
        return self.reference[row + 1][column]

    def right(self, row, column):
        return self.reference[row][column + 1]

    def left(self, row, column):
        return self.reference[row][column - 1]

    def print_matrix(self):
        for row in self.reference:
            for j in row:
                print(j, end=' ')
            print('\n')


mrx = Matrix([0 for i in range(25)])
mrx.print_matrix()
mrx.up(2, 2)
mrx.print_matrix()
