"""
This program adds two numbers
It first ask for a user input for both numbers.
The numbers and then converted into integers to allow the correct calculation
The total is then converted into text to display the result
"""


# The main function is the entry point of the program
def main():
    print("This program adds two numbers")
    num1 = input("Enter first number: ")
    num1 = int(num1)
    num2 = input("Enter second number: ")
    num2 = int(num2)
    total = num1 + num2
    print("The total of the first and second numbers is " + str(total) + ".")


# This allow the main function to run when this file is executed
if __name__ == '__main__':
    main()
