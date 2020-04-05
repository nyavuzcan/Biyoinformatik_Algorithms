class Needleman:
    matrix = None
    scoreMatrixLine = None

    def __init__(self, matrix, scoreMatrixline):
        self.matrix = matrix
        self.scoreMatrixLine = scoreMatrixline
        self.calculateMatris()

    def calculateMatris(self):

        for i in range(2, 52):
            for j in range(2, 52):
                x = self.matrix[0][j]
                y = self.matrix[i][0]
                xyValue = self.scoreMatrixLine[x + y]
                temp = ''

                if (self.matrix[i][j - 1] != 'x' and
                        self.matrix[i][j - 1] is not None
                ):
                    temp = self.matrix[i][j - 1]
                if (self.matrix[i - 1][j - 1] != 'x' and
                        temp < self.matrix[i - 1][j - 1]

                ):
                    temp = self.matrix[i - 1][j - 1]
                if (self.matrix[i - 1][j] != 'x' and
                        temp < self.matrix[i - 1][j]

                ):
                    temp = self.matrix[i - 1][j]
                try:
                    if (self.matrix[i + 1][j - 1] != 'x' and
                            temp < self.matrix[i + 1][j - 1]

                    ):
                        temp = self.matrix[i + 1][j - 1]
                    if (self.matrix[i - 1][j + 1] != 'x' and
                            temp < self.matrix[i - 1][j + 1]

                    ):
                        temp = self.matrix[i - 1][j + 1]
                except IndexError or TypeError:
                    self.matrix[i][j] = temp + xyValue

                    pass
                self.matrix[i][j] = temp + xyValue

        return self.matrix
