from random import randint

randomNumber = randint(1, 30)

userInput = None
userInteger = None
attempts = 0

# First check (do-while does not exist)
try:
    userInput = input("Guess the number: ")
    userInteger = int(userInput)
    attempts += 1

    if (randomNumber == userInteger):
        print("Awesome! You guessed the number in the first try!")
except ValueError as e:
    if (userInput != "exit"):
        print("The input has to be a number")

# Loop for next attempts
while (randomNumber != userInteger and userInput != "exit"):
    if (userInteger != None and randomNumber > userInteger):
        print("The target is greater than " + str(userInteger))
    elif (userInteger != None and randomNumber < userInteger):
        print("The target is less than " + str(userInteger))

    try:
        userInput = input("Try again: ")
        attempts += 1
        userInteger = int(userInput)
    except ValueError as e:
        if (userInput != "exit"):
            print("The input has to be a number")

if (randomNumber == userInteger):
    print("Correct!!")

print("Number of attempts: " + str(attempts))

# Flush the number of attempts to a file
f = open("GuessingSteps.txt", "w")
f.write("Numer of attempts: " + str(attempts))
f.close()