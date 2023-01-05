"""Module documentation goes here
# Created By  : name_of_the_creator   Line 3
# Created Date: 2022/12/26
# Description :
"""
import random


# Project Converter
# (L)bs or (K)g: not case sensitive
def lk_converter(weight):
    unit = input("(L)bs or (K)g:")

    if unit.upper() == 'K':
        # Kilo to pounds
        converted = weight / 0.453
        print(f'You are {converted} lbs')
    elif unit.upper() == 'L':
        # pounds to Kilo
        converted = weight * 0.453
        print(f'You are {converted} Kg')
    else:
        print("invalid unit!")

# weight = int(input("Enter Weight:"))
# lk_converter(weight)


# Guessing Number Game
def guessing_number():
    print("Guess the Number between 1-20")
    secret_no = 9  # secret number
    guess_count = 1
    guess_limit = 3

    while guess_count <= guess_limit:
        guess = int(input("Guess:"))
        if guess != secret_no:
            guess_count += 1
        else:
            print("You Win!")
            break
    else:
        print("Sorry you failed!")
# guessing_number()


# Engine Start Stop quit with Command
def engine_help():
    selection = """start - to start the car
stop  - to stop the car
quit  - to exit"""
    flag_start = 0

    while True:
        command = input("> ").lower()
        if command == "help":
            print(selection)
        elif command == "start":
            if flag_start != 1:
                print("Car started...Ready to go!!!")
                flag_start = 1
            else:
                print("Hey Car Already Started! broooom!!")
        elif command == "stop":
            if not flag_start:
                print("Hey Already Stopped!")
            else:
                print("Car stopped...")
                flag_start = 0
        elif command == "quit":
            break
        else:
            print("Sorry, I don't understand that...type help for commands.")
# engine_help()


# Find the large Number
# numbers = [2,4,5,7,1,2,10,23,27,8,3]
def find_largest_number(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    print(f"""The largest Number on the list 
{numbers} 
is = {max_num}""")
# find_largest_number(numbers=[2,127,80,6,4,5,7,1,2,10,23,27,8,3])


# Remove Duplicate on the List
def remove_duplicates(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    print(f"""Unique number are : {unique}
from {numbers}""")
# remove_duplicates(numbers=[2,2,4,6,3,4,6,1,8,2,4,5])


# fibonacci Function
def fibonacci(number):
    num1 = 0
    num2 = 1
    for num in range(number):
        print(num1)
        fn = num1 + num2
        num1 = num2
        num2 = fn
# fibonacci(20)


# Translate Number to Word
def number_to_word(phone):
    digit_map = {
        "+": "(Plus)",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero"
    }
    output = ""
    for number in phone:
        output += digit_map.get(number) + " "
    return output
# phone = input("Phone: ")
# number_to_word(phone)


# Emoji Converter
def emoji_converter(msg):
    words = msg.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😞"
    }
    output = ""

    for word in words:
        output += emojis.get(word, word) + " "

    return output

# message = input(">")
# print(emoji_converter(message))

# roll method tuple immutable value that cannot be change
# get tuple of two random values (0, 0)


class Dice:
    @staticmethod
    def roll():
        first_rand = random.randint(1, 6)
        second_rand = random.randint(1, 6)

        return first_rand, second_rand


dice = Dice()
print(dice.roll())
