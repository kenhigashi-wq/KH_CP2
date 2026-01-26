# KH 2nd Password Generator
"""A main function that runs the code
Functions for the different password requirements
A function that assembles that password once it is the correct length
Users should be able to specify length and if they want to include
uppercase letters
lowercase letters
numbers
special characters"""

import random
#Make a list of special characters

def main():
    print("Welcome to the Password Generator!")
    print("1. Generate Passwords")
    print("2. Exit")
    operation = input("Type the number for the action you would like to perform: ")
    if operation == "1":
        length = int(input("Enter the length of the password: "))
        uppercase = input("Include uppercase letters? (y/n): ").lower()
        lowercase = input("Include lowercase letters? (y/n): ").lower()
        numbers = input("Include numbers? (y/n): ").lower()
        special = input("Include special characters? (y/n): ").lower()
        print("Possible Passwords:")
        print(f"1.")
        print(f"2.")
        print(f"3.")
        print(f"4.")
        return
    elif operation == "2":
        print("Goodbye")

main()

