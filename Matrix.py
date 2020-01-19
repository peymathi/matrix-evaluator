"""
    Class that represents a matrix in row major form and includes methods to do things
    to the matrix. Matrices are of fixed size. 

    Row Major - 
    Array: |0|1|2|3|4|5|6|7|8| 
    Representing Matrix: 

        |0|1|2|
        |3|4|5|
        |6|7|8|       
    
    Ex. 3x3 matrix 
    Element Row: 2 Col: 3 Indice: 5
    Indice = ((Row - 1) * Width) + (Col - 1)

    2D Array -

    array[row][col]

    All methods return lists in row major form

    P. Mathis
    Created 2/24/19
"""

# Math library
import math
import random
import numbers

class Matrix:

    # Constructor that initializes the matrix size with default values of 1
    def __init__(self, height = 1, width = 1):

        if height < 1 or width < 1:
            raise "Height and width must be equal to or greater than 1"

        self.__height = height
        self.__width = width

        # List that stores all values of the matrix in row major form
        self.__values = []

        # List that stores all values of the matrix in 2d array form
        self.__values_2d = []

    # Method that takes a list to set the values of the matrix
    def initMatrix(self, values):

        # Check to make sure that the list entered is of correct size
        if (len(values) != (self.__height * self.__width)):
            raise "List argument given is of incorrect size"

        # Check to make sure that all values entered are numeric
        for i in values:
            if not isinstance(i, numbers.Number):
                raise "Arguments in list are not all numeric"

        self.__values = values

        # Set up 2d array
        row = []
        for i in range(len(self.__values)):

            row.append(self.__values[i])
            if (i + 1) % self.__width == 0:
                self.__values_2d.append(row)
                row = []

    # Fills the matrix with random values ranging from start to end
    def randomFill(self, start, end):
        
        # Iterates through the length of the list setting random values
        for i in range(0, self.__height * self.__width):
            self.__values.append(random.randrange(start, end))

        self.initMatrix(self.__values)

    """ Getters for each of the private variables """
    def getHeight(self):
        return self.__height
    
    def getWidth(self):
        return self.__width

    def getValues(self):
        return self.__values

    def getValues2d(self):
        return self.__values_2d

    height = property(fget=getHeight)
    width = property(fget=getWidth)
    values = property(fget=getValues)
    values2d = property(fget=getValues)

    # Method to return a value within the matrix. Takes a width and height arguments
    def getValue(self, row, col):

        # Check to make sure the values entered are of correct size for the matrix
        if (row > self.__height or row < 1) or (col > self.__width or col < 1):
            raise "Height or width argument of invalid size"

        else:
            # Find the value given the height and the width
            return self.__values[((row - 1) * self.__width) + (col - 1)]

    # Method to set a value within the matrix.
    def setValue(self, row, col, value):

        # Check to make sure the values entered are of correct size for the matrix
        if (row > self.__height or row < 1) or (col > self.__width or col < 1):
            raise "Height or width argument of invalid size"

        else:

            # Set the element at the given height and width to the given value
            self.__values[((row - 1) * self.__width) + (col - 1)] = value

    # Prints the matrix in a formatted way to the console
    def printMatrix(self):
        
        if self.__values == []:
            print("Empty matrix. Nothing to print.")
            return

        # format string to print at the end
        formatted = ""

        # Each row
        for i in range(self.__height):

            # Each column
            for j in range(self.__width):

                # Check if we are at the end of the row
                if j == self.__width - 1:
                    formatted += "|{}|\n".format(self.__values[j + (self.__width * i)])

                else:
                    formatted += "|{}".format(self.__values[j + (self.__width * i)])
                
        print(formatted)


    # Reduces the matrix to row-echelon form
    def reduceMatrix(self):
        pass

    # Takes the second matrix and subtracts the two
    def __sub__(self, secondMatrix):

        # Check that the matrix sizes are correct
        if self.__width != secondMatrix.__width or self.__height != secondMatrix.__height:
            raise "Bad matrix dimensions"

        newMatrix = []
        for i in range(len(self.__values)):
            newMatrix.append(self.__values[i] - secondMatrix.__values[i])

        return newMatrix

    # Takes the second matrix and adds the two
    def __add__(self, secondMatrix):

        # Check that the matrix sizes are correct
        if self.__width != secondMatrix.__width or self.__height != secondMatrix.__height:
            raise "Bad matrix dimensions"

        newMatrix = []
        for i in range(len(self.__values)):
            newMatrix.append(self.__values[i] + secondMatrix.__values[i])

        return newMatrix

    # Takes a second matrix and multiplies the two. Creates and returns a product matrix object
    def __mul__(self, secondMatrix):
        
        # Check to make sure that the two matrices are multiplyable
        if self.__width != secondMatrix.__height:
            raise "Bad matrix dimensions"

        newMatrix = []
        # Loop through each row of the first matrix
        for row in range(self.__height):

            # Loop through each column of the second matrix
            for col in range(secondMatrix.__width):

                # Multiply each value in the current row with each value in the current column
                nextSum = 0
                # Loop through the row
                for i in range(self.__width):
                    nextSum += self.__values_2d[row][i] * secondMatrix.__values_2d[i][col]

                newMatrix.append(nextSum)

        return newMatrix

    # Finds the determinant of the matrix
    def getDeterminant(self):
        pass
    
def main():
    matrix = Matrix(3, 3)
    values = [
        30, 4, 3,
        5, 300, 2, 
        -17.5, 9, 10]

    matrix.initMatrix(values)
    nextMatrix = Matrix(3,6)
    nextMatrix.randomFill(1, 4)
    matrix.printMatrix()
    nextMatrix.printMatrix()
    m2d = matrix.getValues2d()
    n2d = nextMatrix.getValues2d()

    result = matrix * nextMatrix
    


if __name__ == "__main__":
    main()
