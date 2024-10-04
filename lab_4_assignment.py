# Romain Tranchant
# CIS103
# Instructor: MD Ali
# CIS 103: Fundamentals of Programming
# Lab 4: Python Practice – Group Assignment
# Due Date: 10/05/2024 @ 11:59pm
# Presentation Date: 09/28/2024 @ 10:00am


# Part 1: Short Practice – Individual
# • Write a program that checks if a number is positive, negative, or zero
# • Write a for loop that prints every second number between 0 and 10
# • Create a while loop that prints numbers from 1 to 100
# • Loop through rows and columns of a matrix that you created
# • Write a function that takes two numbers as arguments and returns their sums
# • Write a function that calculate that area of a rectangle, with a default length and width
# • Use a try-except mentioned in last lecture to handle user input errors in the calculator
# program from lab 1

##################################################################################

# • Write a program that checks if a number is positive, negative, or zero

# Define the number_check function with num as a parameter
def number_check(num):
# Print a message as an f-string if the number is either positive or negative
    if num < 0:
        print(f"{num} is a negative")
    elif num > 0:
        print((f"{num} is a positive"))
# If the number isn't positive or negative, print the message "The number is zero"
    else:
        print("The number is zero")

##################################################################################

# • Write a for loop that prints every second number between 0 and 10

# Start a for loop going from 0 to 10, 11 is excluded, with a step of 2
# The step of 2 skips every second number within the range, and print the output
for second_number in range(0, 11, 2):
    print(second_number)

##################################################################################

# • Create a while loop that prints numbers from 1 to 100

# create a variable number with the value of 1
number = 1
# start a while loop going from 0 to 100 and print the current value of number
while number <= 100:
    print(number)
# Increase the variable number by 1, after printing the current value, number gets a new value
    number += 1

##################################################################################

# • Loop through rows and columns of a matrix that you created

# Create a matrix with 3 rows and 3 columns
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Start a for loop through all the rows of the matrix, len(matrix) the number of rows in the matrix
for row_index in range(len(matrix)):
# Start another for loop through the columns in the current row
    for col_index in range(len(matrix[row_index])):
# Because the outputs need the row number and column number, and our indexes start at 0,
# for more clarity to the user, we need to increase the index by 1 for the row number
# and the column number
        row_number = row_index + 1
        column_number = col_index +1
# Print the element along with its position using and f-string
        print(f"The element at row {row_number}, column {column_number} is {matrix[row_index][col_index]}")


##################################################################################


# • Write a function that takes two numbers as arguments and returns their sums

# Define the sum_function with 2 numbers by returning the sum of these 2 numbers
def sum_function(num1, num2):
    return num1 + num2
# Assign values to num1 and num2
num1 = 10
num2 = 15
# Create a result variable containing the result of the sum_function using num1 and num2 as arguments
# Print the result using an f-string
result = sum_function(num1, num2)
print(f"The sum of {num1} and {num2} is {result}")


##################################################################################

# • Write a function that calculate that area of a rectangle, with a default length and width

# Define the rectangle_area function with 2 numbers by returning the product of these two numbers
def rectangle_area(length, width):
    return length * width
# Assign values to length and width
length = 6
width = 3
# Create a result variable containing the result of the rectangle_area function using length and
# width as arguments
# Print the result using an f-string
result = (rectangle_area(length, width))
print(f"The area of the rectangle is {result}")


##################################################################################

# • Use a try-except mentioned in last lecture to handle user input errors in the calculator
# program from lab 1

# Define the addition function with 2 numbers by returning
# the sum of these 2 numbers
def addition(num1, num2):
    return num1 + num2

# Define the subtraction function with 2 numbers by returning
# the difference of these 2 numbers
def subtraction(num1, num2):
    return num1 - num2

# Define the multiplication function with 2 numbers by returning
# the product of these 2 numbers
def multiplication(num1, num2):
    return num1 * num2

# Define the division function with 2 numbers by returning
# the quotient of these 2 numbers, except if the second number
# is equal to 0 because a division by 0 is impossible. It would
# return an error message
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error, division by zero impossible"

# Define the exponentiation function with 2 numbers by returning
# num1 to the power of num2
def exponentiation(num1, num2):
    return num1 ** num2

# Define the modulus function with 2 number by returning the
# remainder of num1 divided by num2
def modulus(num1, num2):
    return num1 % num2

# Define the squareroot function by returning the square root
# of num3, except if num3 is a negative number, an error message
# would be returned
def squareroot(num3):
    if num3 >= 0:
        return num3 ** 0.5
    else:
        return "Error, square root of a negative number is not defined in real numbers."

# Define the calculator function
def calculator():

# Start a while loop, to allow the calculator to reset itself until
# the user decides to exit
    while True:

# Prints the choices to the user
        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("6. Modulus (%)")
        print("7. Square root (√)")
        print("8. Exit")

 # Define the variable choice as being the user's input choice
        choice = input("Enter your choice 1, 2, 3, 4, 5, 6, 7 or 8:")

# If the user's choice is not between 1 and 8, print an "Invalid choice"
# message. The continue statement allows the program to process errors and
# invalid inputs, by skipping the rest of the program and resetting the
# calculator
        if choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("Invalid choice! Please enter a valid choice.")
            continue

# The try statement is used to check any errors that might occur during
# the user's inputs of num3
# Call the squareroot function and print the square root of num3, print the
# result,and the continue statement skips the rest of the program to reset
# the calculator7
        try:
            if choice == "7":
                num3 = float(input("Enter your number: "))
                print(f"The result is: {squareroot(num3)}")
                continue

# The valueError handles any format error that the user may input, if the
# user input is not a float number, an "Invalid input! Please enter a number."
# message is shown and the calculator restarts through the continue statement
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

# If the user wants to exit the calculator, print a "Goodbye" message
# and exit the calculator through the break statement
        if choice == "8":
            print("Goodbye!")
            break

# The try statement is used to check any errors that might occur during
# the user's inputs of num1 and num2
        try:

# Ask the user to enter the first number, converts the input from a
# string to a float number, and assigns it to the variable num1
            num1 = float(input("Enter your first number:"))

# Ask the user to enter the second number, converts the input from a
# string to a float number, and assigns it to the variable num2
            num2 = float(input("Enter your second number:"))

# The valueError handles any format error that the user may input, if the
# user input is not a float number, an "Invalid input! Please enter a number."
# message is shown and the calculator restarts through the continue statement
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

# Perform the chosen operation based on user's choice

# Call the addition function and print the sum of num1 and num2
        if choice == "1":
            print(f"The result is: {addition(num1, num2)}")

## Call the subtraction function and print the difference of num1 and num2
        if choice == "2":
            print(f"The result is: {subtraction(num1, num2)}")

# Call the multiplication function and print the product of num1 and num2
        if choice == "3":
            print(f"The result is: {multiplication(num1, num2)}")

# Call the division function and print the quotient of num1 and num2
        if choice == "4":
            print(f"The result is: {division(num1, num2)}")

# Call the division function and print the result of num1 to the power of num2
        if choice == "5":
            print(f"The result is: {exponentiation(num1, num2)}")

# Call the division function and print the remainder of num1 divided num2
        if choice == "6":
            print(f"The result is: {modulus(num1, num2)}")

# This construct ensures that certain code is only executed when the script is run
# directly, and not when it is imported as a module in another script.
if __name__ == "__main__":
    calculator()