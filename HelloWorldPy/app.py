"""Module documentation goes here
# Created By  : Kean Duque
# Created Date: 2022/12/26
# Description : main app
"""
import openpyxl as xl
from openpyxl.chart import BarChart, Reference

import utils
from utils import Dice


# Project Converter
# weight = int(input("Enter Weight:"))
# utils.lk_converter(weight)

# Guessing Number Game
# utils.guessing_number()

# utils.engine_help()

# Find the large Number
# utils.find_largest_number(numbers=[2,127,80,6,4,5,7,1,2,10,23,27,8,3])

# Remove Duplicate on the List
# utils.remove_duplicates(numbers=[2,2,4,6,3,4,6,1,8,2,4,5])

# Fibonacci Function
# utils.fibonacci(20)

# phone = input("Phone: ")
# utils.number_to_word(phone)

# message = input(">")
# print(utils.emoji_converter(message))

# Dice Roll tuple of two random values (0, 0)
# dice = Dice()
# print(dice.roll())


# Project_1 Automation Excel File
# update 4th column for corrected_price
def process_workbook(filename):

    wb = xl.load_workbook(filename)
    sheet = wb['Sheet1']

    cell4_header = sheet.cell(1, 4)
    cell4_header.value = "corrected_price"

    for row in range(2, sheet.max_row + 1):
        cell = sheet.cell(row, 3)
        corrected_price = cell.value * 0.9

        corrected_price_cell = sheet.cell(row, 4)
        corrected_price_cell.value = corrected_price

    values = Reference(sheet,
                       min_row=2,                # start at Row 2
                       max_row=sheet.max_row,    # max row is 4
                       min_col=4,                # column D2
                       max_col=4)                # column D4

    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart, 'e2')

    wb.save(filename)

# process_workbook('transactions.xlsx')


# FizzBuzz
# utils.fizz_buzz(50)


# Checking speed of Driver
# 0speed: The car Stop
# 1 - 70speed : OK
# >= 75speed - every 5km speed limit Demerit Points + 1
# 130 speed which is 12 demerit : License Suspended

# utils.print(check_speed(130))


# Print Odd and Even beside numbers until limit reached
# utils.show_numbers(10)


# print Stars based on row input
# utils.print(show_stars(5))


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
"""

# Get all Prime Numbers
# utils.prime_numbers(100)
