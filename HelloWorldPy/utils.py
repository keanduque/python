"""Module documentation goes here
# Created By  : Kean Duque
# Created Date: 2023/01/05
# Description : utility reusable functions
"""
import random


# roll method tuple immutable value that cannot be change
# get tuple of two random values (0, 0)
class Dice:
    @staticmethod
    def roll():
        first_rand = random.randint(1, 6)
        second_rand = random.randint(1, 6)

        return first_rand, second_rand


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
                print("Hey Car Already Started! broom!!")
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


# Remove Duplicate on the List
def remove_duplicates(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    print(f"""Unique number are : {unique}
from {numbers}""")


# fibonacci Function
def fibonacci(number):
    num1 = 0
    num2 = 1
    for num in range(number):
        print(num1)
        fn = num1 + num2
        num1 = num2
        num2 = fn


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


# FizzBuzz
# divisible by 3 = fizz - divided by 3 or in 3x multiplication table no remainder
# divisible by 5 = buzz - ends in a 5 or 0  or no remainder
# divisible by 3 and 5 = fizz_buzz
#
def fizz_buzz(num):
    for number in range(num + 1):
        if (number % 3 == 0) and number % 5 == 0:
            output = "FizzBuzz"
            print(f"{number} = {output}")
        elif number % 3 == 0:
            output = "Fizz"
            print(f"{number} = {output}")
        elif number % 5 == 0:
            output = "Buzz"
            print(f"{number} = {output}")
        else:
            print(number)


# Checking speed of Driver
# 0speed: The car Stop
# 1 - 70speed : OK
# >= 75speed - every 5km speed limit Demerit Points + 1
# 130 speed which is 12 demerit : License Suspended
def check_speed(speed):
    speed_limit = 70
    output = ""
    if speed == 0:
        output = "The car is stop"
    else:
        for num in range(speed):
            if speed <= speed_limit:
                output = "OK"
            elif speed > speed_limit:
                exceed_speed = speed - speed_limit
                per_speed_limit = exceed_speed / 5
                points = int(per_speed_limit)
                if points != 0 and points < 12:
                    output = f"Speed:{speed} Demerit Points:{points}"
                elif points >= 12:
                    output = f"License Suspended!!"
                else:
                    output = "OK"
    return output


# Print Odd and Even beside numbers until limit reached
def show_numbers(limit):
    for num in range(limit + 1):
        if num % 2 == 0:
            print(f"{num} EVEN")
        else:
            print(f"{num} ODD")


# print Stars based on row input
def show_stars(rows):
    output = ""
    for rows in range(1, rows + 1):
        for cols in range(rows):
            output += "*"
        output += "\n"

    return output


"""
Prime number is divisible by 2 natural numbers ONLY
- divide by 1 and itself
- greater than 1
- not more than 2 factors
- 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97
factor : a number that divides another number exactly or evenly with no remainder
smallest prime is 2 
smallest composite number is 4

1 - not prime numbers because not > 1 not 2 factors
samples : 
                                no remainder
2 - 1,2             prime        2/1, 2/2
3 - 1,3             prime        3/1, 3/3
4 - 1,2,4           composite    4/1, 4/2, 4/4
5 - 1,5             prime        5/1, 5/5
6 - 1,2,3,6         composite    6/1, 6/2, 6/3, 6/6
7 - 1,7             prime        7/1, 7/7
8 - 1,2,4,8         composite    8/1, 8/2, 8/4, 8/8
9 - 1,3,9           composite    9/1, 9/3, 9/9
10 - 1,2,5          composite    10/1, 10/2, 10,5
11 - 1,11           prime        11/1, 11/11
12 - 1,2,3,4,6,12   composite    12/1, 12/2, 12/3, 12/4, 12/6, 12/12
13 - 1,13           prime        13/1, 13/13
14 - 1,2,7,14       composite
15 - 1,3,5,15       composite
18 - 1,2,3,6,9,18   composite
23 - 1,23           prime
29 - 1,29           prime

"""


# Get all Prime Numbers
def prime_numbers(num):
    count = 0
    prime = []
    for n in range(2, num+1):
        for in_n in range(1, num):
            if n % in_n == 0:
                count += 1
                if count == 2 and n == in_n:
                    prime.append(n)
        count = 0
    print(f'Prime Numbers : {prime}')
