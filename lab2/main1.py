"""
String Int conversions
"""

import math
import json

DIGITS_ARRAY = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
DIGITS_MAP = json.loads('{"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, \
    "6": 6, "7": 7, "8": 8, "9": 9}')

INTEGER_INPUTS = [1, 30, 75, "test", 20, 56, "abc", "two", 25, 100]
STRING_INPUTS = ["234", "5", "26", 27, 300, "abcdef", "0", "1", "20", ""]


def int_to_str(value):
    """
    Converts an integer to its string representation
    """

    if isinstance(value, int):
        base = 10
        power = 1
        result = ""

        # The loop will iterate until the value divided by the decimal base is greater than 0.1
        while value / (base**power) >= 0.1:
            power_value = base**power
            modulo = value % power_value
            previous_power_value = (base**(power-1))
            unit = math.floor(modulo/previous_power_value)

            result = DIGITS_ARRAY[unit] + result
            power += 1

        return result

    raise ValueError("Not an integer value")


def str_to_int(value):
    """
    Convert a numeric string to its INT representation
    """

    base = 10

    if isinstance(value, str) and value.isdigit():
        # Split the string into individual characters
        #characters = [char for char in value]
        characters = list(value)
        string_length = len(characters)
        accumulator = 0

        for i in range(string_length):
            numeric_value = DIGITS_MAP[characters[i]]
            accumulator += numeric_value * (base**(string_length-i-1))

        return accumulator

    raise ValueError("Not a string value")


# Test the int_to_str conversion
print("***INT_TO_STR CONVERSION***")
for input_value in INTEGER_INPUTS:
    try:
        print(int_to_str(input_value))
    except ValueError as error:
        print(str(error))

# Test the str_to_int conversion
print()
print("***STR_TO_INT CONVERSION***")
for input_value in STRING_INPUTS:
    try:
        print(str_to_int(input_value))
    except ValueError as error:
        print(str(error))
