#!/usr/bin/env python3

# Created by: Mr. Matthew Meech
# Created on: Sep 2021
# month namer


def main():

    # input
    integer = int(input("Enter number a the number of a month:"))
    print("")

    # if ... then ... elseif
    if integer == 1:
        print("your month is Jan")
    elif integer == 2:
        print("your month is Feb")
    elif integer == 3:
        print("your month is Mar")
    elif integer == 4:
        print("your month is Apr")
    elif integer == 5:
        print("your month is May")
    elif integer == 6:
        print("your month is Jun")
    elif integer == 7:
        print("your month is Jul")
    elif integer == 8:
        print("your month is Aug")
    elif integer == 9:
        print("your month is Sep")
    elif integer == 10:
        print("your month is Oct")
    elif integer == 11:
        print("your month is Nov")
    elif integer == 12:
        print("your month is Dec")
    elif integer > 12:
        print("not a month number ")
    elif integer < 1:
        print("not a month number ")

    print("\nDone.")


if __name__ == "__main__":
    main()
