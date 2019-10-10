"""
    Class that represents a matrix in row major form and includes methods to do things
    to the matrix.

    Row Major: |0|1|2|3|4|5|6|7|8| 3x3 matrix Element Row: 2 Col: 3 Indice: 5
    Indice = ((Row - 1) * Width) + (Col - 1)

    P. Mathis
    Created 2/24/19
"""

# Math library
import math

# For random generator
import random

class Matrix:

    # Integer to represent the height
    height_ = 0

    # Integer to represent the width
    width_ = 0

    # List that stores all values of the matrix in row major form
    values_ = []

    # Constructor that initializes the matrix size but no values
    def __init__(self, height = None, width = None):

        # Default values given in member declaration
        if height == None:
            pass
        
        else:
            self.height_ = height
            
        if width == None:
            pass
        
        else:
            self.width_ = width

    # Method that takes a list to set the values of the matrix
    def initMatrix(self, values):

        # Check to make sure that the list entered is of correct size
        if (len(values) == (self.height_ * self.width_)):
            self.values_ = values

        else:
            raise "List argument given is of incorrect size"

    # Fills the matrix with random values ranging from start to end
    def randomFill(self, start, end):

        # Check that height and width have been set
        if self.height_ < 0 or self.width_ < 1:
            raise "Must initialize height and width greater than 1"
        
        # Iterates through the length of the list setting random values
        for i in range(0, self.height_ * self.width_):
            self.values_.append(random.randrange(start, end))
        

    # Method to return a value within the matrix. Takes a width and height arguments
    def getValue(self, row, col):

        # Check to make sure the values entered are of correct size for the matrix
        if (row > self.height_ or row < 1) or (col > self.width_ or col < 1):
            raise "Height or width argument of invalid size"

        else:

            # Find the value given the height and the width
            return self.values_[((row - 1) * self.width) + (col - 1)]

    # Method to set a value within the matrix.
    def setValue(self, row, col, value):

        # Check to make sure the values entered are of correct size for the matrix
        if (row > self.height_ or row < 1) or (col > self.width_ or col < 1):
            raise "Height or width argument of invalid size"

        else:

            # Set the element at the given height and width to the given value
            self.values_[((row - 1) * self.width_) + (col - 1)] = value

    # Prints the matrix in a formatted way to the console
    def printMatrix(self):
        
        """
            Loop through each row of the matrix and make a formatted string
            to print.

            For each row, add {:^1} to the string for each element in the row
        """
        
        # Within the loop, i is the current row, and j is the current column
        # Outer loop through all of the rows of the matrix
        for i in range(0, self.height_):

            # String that will be printed
            matrixString = ""

            # Add the first pipe character curly braces
            matrixString += "{pipe:^3}"

            # Inner loop through each column of the matrix
            for j in range(0, self.width_):

                # For every element in the row, add the curly braces
                matrixString += "{element :^3}"
                matrixString.format(element = self.values_[((i - 1) * self.width)) + (j - 1)], pipe = "|")
                
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
    
