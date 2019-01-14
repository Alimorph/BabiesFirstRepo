class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = []
        for row_string in matrix_string.split("\n"):
            row_list = []
            for num_string in row_string.split(" "):
                row_list.append(int(num_string))
            self.matrix.append(row_list)

    def row(self, index):
        return self.matrix[index]

    def column(self, index):
        column = []
        for row in self.matrix:
            column.append(row[index])
        return column
