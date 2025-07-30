''' Matrix Class '''
class Matrix:
    def __init__(self, rows, cols, default=0):
        self.data = [[default for _ in range(cols)] for _ in range(rows)]

    def insert(self, row, col, value):
        self.data[row][col] = value

    def access(self, row, col):
        return self.data[row][col]

    def delete(self, row, col):
        self.data[row][col] = 0