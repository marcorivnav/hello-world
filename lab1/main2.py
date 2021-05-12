"""
Conversions
"""

import sys
import json

# Verify at least 1 argument is provided
ARGUMENTS_COUNT = len(sys.argv)

if ARGUMENTS_COUNT < 2:
    print("You should provide an integer number as an argument")
else:
    # Get the argument
    argument = sys.argv[1]

    # Assert it is an integer number
    try:
        user_number = int(argument)

        # Binary conversion
        if user_number == 0:
            print("Binary: 0")
        else:
            BASE = 2
            accumulator = user_number
            RESULT = ""

            while accumulator > 0:
                modulo = accumulator % BASE
                RESULT = str(modulo) + RESULT
                accumulator = int(accumulator/BASE)

            print("Binary: %s" % RESULT)

        # Hexa conversion
        if user_number == 0:
            print("Hexadecimal: 0")
        else:
            HEXA = json.loads('{"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}')
            BASE = 16
            accumulator = user_number
            RESULT = ""

            while accumulator > 0:
                modulo = accumulator % BASE

                if modulo < 10:
                    RESULT = str(modulo) + RESULT
                else:
                    RESULT = HEXA[str(modulo)] + RESULT

                accumulator = int(accumulator/BASE)

            print("Hexadecimal: %s" % RESULT)
    except ValueError:
        print("The argument has to be an integer number")
