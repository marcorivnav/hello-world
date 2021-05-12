"""
Guess number
"""

from random import randint

random_number = randint(1, 30)

USER_INPUT = None
USER_INTEGER = None
ATTEMPTS = 0

# First check (do-while does not exist)
try:
    USER_INPUT = input("Guess the number: ")
    USER_INTEGER = int(USER_INPUT)
    ATTEMPTS += 1

    if random_number == USER_INTEGER:
        print("Awesome! You guessed the number in the first try!")
except ValueError:
    if USER_INPUT != "exit":
        print("The input has to be a number")

# Loop for next attempts
while (random_number != USER_INTEGER and USER_INPUT != "exit"):
    if (USER_INTEGER is not None and random_number > USER_INTEGER):
        print("The target is greater than " + str(USER_INTEGER))
    elif (USER_INTEGER is not None and random_number < USER_INTEGER):
        print("The target is less than " + str(USER_INTEGER))

    try:
        USER_INPUT = input("Try again: ")
        ATTEMPTS += 1
        USER_INTEGER = int(USER_INPUT)
    except ValueError:
        if USER_INPUT != "exit":
            print("The input has to be a number")

if random_number == USER_INTEGER:
    print("Correct!!")

print("Number of attempts: " + str(ATTEMPTS))

# Flush the number of attempts to a file
f = open("GuessingSteps.txt", "w")
f.write("Numer of attempts: " + str(ATTEMPTS))
f.close()
