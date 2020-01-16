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
            

    # Fills the matrix with random values ranging from start to end
    def randomFill(self, start, end):
        
        # Iterates through the length of the list setting random values
        for i in range(0, self.__height * self.__width):
            self.__values.append(random.randrange(start, end))

    """ Getters for each of the private variables """
    def getHeight(self):
        return self.__height
    
    def getWidth(self):
        return self.__width

    def getValues(self):
        return self.__values

    height = property(fget=getHeight)
    width = property(fget=getWidth)
    values = property(fget=getValues)

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

    # Takes a second matrix and multiplies the two. Creates and returns a product matrix object
    def multiplyMatrices(self, secondMatrix):
        pass

        # Check to make sure that the two matrices are multiplyable
        

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
    matrix.printMatrix()

if __name__ == "__main__":
    main()
