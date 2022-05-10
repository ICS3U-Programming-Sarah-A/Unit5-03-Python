#!/usr/bin/env python3

# Created by: Sarah
# Created on: May 6th, 2022.
# This program asks the user to enter a level. It then converts the level to a
# percentage, displaying it to the user.

# this function determines the middle percentage of what level
# the user entered.
def calc_mark(grade_average):
    if grade_average == "4+":
        return "98"
    elif grade_average == "4":
        return "91%"
    elif grade_average == "4-":
        return "83%"
    elif grade_average == "3+":
        return "78%."
    elif grade_average == "3":
        return "75%"
    elif grade_average == "3-":
        return "71%"
    elif grade_average == "2+":
        return "68%"
    elif grade_average == "2":
        return "65%"
    elif grade_average == "2-":
        return "61%"
    elif grade_average == "1+":
        return "58.%"
    elif grade_average == "1":
        return "55"
    elif grade_average == "1-":
        return "51%"
    elif grade_average == "R":
        return "25%"
    else:
        return "-1"


def main():
    # get user input from user
    user_level = input("Enter the level you want to convert to a percentage: ")
    print("")

    # assigns a variable to function call, giving it a returned value.
    percentage = calc_mark(user_level)

    # checks for any invalid inputs, as well as display them to user.
    if calc_mark(user_level) == "-1":
        print("Invalid entry, {} is not a valid level."
              .format(user_level))
    else:
        print("Level {} has a middle percentage of {}."
              .format(user_level, percentage))


if __name__ == "__main__":
    main()
