#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Nov 2019
# This program calculates users percentage based on mark from 0- to 4+t


def calculate(mark):
    # This function calculates the users percentage based on mark from 0- to 4+

    # Process
    if mark == "4+":
        percentage = 97.5
    elif mark == "4":
        percentage = 90.5
    elif mark == "4-":
        percentage = 83
    elif mark == "3+":
        percentage = 78
    elif mark == "3":
        percentage = 74.5
    elif mark == "3-":
        percentage = 71
    elif mark == "2+":
        percentage = 68
    elif mark == "2":
        percentage = 64.5
    elif mark == "2-":
        percentage = 61
    elif mark == "1+":
        percentage = 58
    elif mark == "1":
        percentage = 54.5
    elif mark == "1-":
        percentage = 51
    elif mark == "0+":
        percentage = 44.5
    elif mark == "0":
        percentage = 34.5
    elif mark == "0-":
        percentage = 14.5
    else:
        percentage = -1
    return percentage


def main():
    # This function accepts inputted marks from 0- to 4+

    # Input
    mark = input("Input a mark from 0- to 4+: ")

    # Process
    user_percentage = calculate(mark)

    # Output
    if user_percentage == -1:
        print("Please enter only valid marks from 0- to 4+")
    else:
        print("The inputted mark is equivalent to "
              + str(user_percentage) + "%")


if __name__ == "__main__":
    main()
