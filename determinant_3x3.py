import numpy as np

class Matrix():
    matrix: np.array([])
    
    rows: int
    cols: int

    det: float

    @classmethod
    def __init__(self, array: np.array([])):
        
        self.matrix = array
        self.rows = self.matrix.shape[0]
        self.cols = self.matrix.shape[1]
        
        self.sum_of_parts = 0
        self.det = 0

    @classmethod
    def find_det(self):
        rows = self.rows
        cols = self.cols

        if (rows != cols):
            return

        print("\nadd the following groups of " + str(self.rows) + " multiplied")
        temp_sum = 1
        for x in range(rows):
            for y in range(cols):
                x_val = y % rows
                y_val = (y + x) % rows
                coord_val = self.matrix[x_val, y_val]
                temp_sum *= coord_val
                print("(" + str(x_val) + ", " + str(y_val) + "): " + str(coord_val))
            self.det += temp_sum
            print(str(temp_sum))
            print(str(self.det))
            temp_sum = 1
            print()

        print("\nsubtract the following groups of " + str(self.rows) + " multiplied")
        for x in range(rows):
            for y in range(cols):
                x_val = y
                y_val = (rows - 1 + x - y) % rows
                coord_val = self.matrix[x_val, y_val]
                temp_sum *= coord_val
                print("(" + str(x_val) + ", " + str(y_val) + "): " + str(coord_val))
            self.det -= temp_sum
            print(str(temp_sum * -1))
            print(str(self.det))
            temp_sum = 1
            print()

    @classmethod
    def is_square_matrix(self):
        return self.rows == self.cols

    @classmethod
    def __str__(self):
        return str(self.matrix)

def main():
    array = np.array([[2, 5, -6], [2, 7, 8], [6, -3, -2]])
    matrix = Matrix(array)
    print(matrix)
    print("rows: " + str(matrix.rows) + "\ncols: " + str(matrix.cols))
    print("square matrix: " + str(matrix.is_square_matrix()))
    matrix.find_det()
    print("determinant: " + str(matrix.det))

if __name__ == "__main__":
    main()
