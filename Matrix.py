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
            if type(i) != "int" or type(i) != "float":
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
        pass
        """
            Loop through each row of the matrix and make a formatted string
            to print.

            For each row, add {:^1} to the string for each element in the row
        """
        
        # Within the loop, i is the current row, and j is the current column
        # Outer loop through all of the rows of the matrix
        for i in range(0, self.__height):

            # String that will be printed
            matrixString = ""

            # Add the first pipe character curly braces
            matrixString += "{pipe:^3}"

            # Inner loop through each column of the matrix
            for j in range(0, self.__width):

                # For every element in the row, add the curly braces
                matrixString += "{element :^3}"
                matrixString.format(element = self.__values[((i - 1) * self.__width) + (j - 1)], pipe = "|")
                
            # Add the curly braces for the last pipe character
            matrixString += "{pipe:^3}"

            # Print this row


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
    
