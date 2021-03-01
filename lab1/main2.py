import sys
import json

# Verify at least 1 argument is provided
argumentsCount = len(sys.argv)

if (argumentsCount < 2):
    print("You should provide an integer number as an argument")
else:
    # Get the argument
    argument = sys.argv[1]

    # Assert it is an integer number
    try:
        userNumber = int(argument)

        # Binary conversion
        if (userNumber == 0):
            print("Binary: 0")
        else:
            base = 2
            accumulator = userNumber
            result = ""

            while (accumulator > 0):
                modulo = accumulator % base
                result = str(modulo) + result
                accumulator = int(accumulator/base)

            print("Binary: %s" % result)

        # Hexa conversion
        if (userNumber == 0):
            print("Hexadecimal: 0")
        else:
            HEXA_VALUES = json.loads('{"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}')
            base = 16
            accumulator = userNumber
            result = ""

            while (accumulator > 0):
                modulo = accumulator % base            

                if (modulo < 10):
                    result = str(modulo) + result
                else:
                    result = HEXA_VALUES[str(modulo)] + result               

                accumulator = int(accumulator/base)

            print("Hexadecimal: %s" % result)
    except ValueError:
        print("The argument has to be an integer number")