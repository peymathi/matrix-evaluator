from Matrix import Matrix

"""
    Takes in a matrix from the user and
    reduces it to reduced row echelon form
"""

# Main function
def main():

    keepGoing = True
    
    # While loop that runs until the user asks to stop
    while keepGoing:
    
        # Ask the user the size of the matrix they would like to create
        width = int(input("Enter the width of your matrix: "))
        height = int(input("Enter the height of your matrix: "))

        # List to store the matrix values if the user wants to enter them
        values = []

        # Create the matrix object
        currentMatrix = Matrix(width, height)


        # Runs until the user enters correct input
        while True:
            
            # Ask the user if they would like random values or to set values
            userInput = input("Enter 'R' for random values or 'C' for custom values: ")

            if userInput == "C":

                # Ask the user for each value of the matrix
                for i in range(0, width * height):
                    values.append(float(input("Enter the next value for the matrix: ")))

                # Initialize the values of the matrix with the custom values
                currentMatrix.initMatrix(values)

                # Break the loop
                break;

            elif userInput == "R":

                # Ask the user for the range of random values
                start = int(input("Enter the lowest random value you would like: "))
                end = int(input("Enter the highest random value you woulld like: "))

                # Initialize the matrix with random values within this range
                currentMatrix.randomFill(start, end + 1)

                # Break the loop
                break;
                
        # Print the initial matrix
        currentMatrix.printMatrix()

        # Ask the user if they would like to keep going
        userInput = input("Would you like to do it again? (Y/N) ")

        if userInput.upper() == "N":
            keepGoing = False

# Runs if this module is being ran
if(__name__ == "__main__"):
    main()
