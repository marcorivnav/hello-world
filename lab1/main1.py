from random import randint

random_number = randint(1, 30)

user_input = None
user_integer = None
attempts = 0

# First check (do-while does not exist)
try:
    user_input = input("Guess the number: ")
    user_integer = int(user_input)
    attempts += 1

    if (random_number == user_integer):
        print("Awesome! You guessed the number in the first try!")
except ValueError:
    if (user_input != "exit"):
        print("The input has to be a number")

# Loop for next attempts
while (random_number != user_integer and user_input != "exit"):
    if (user_integer is not None and random_number > user_integer):
        print("The target is greater than " + str(user_integer))
    elif (user_integer is not None and random_number < user_integer):
        print("The target is less than " + str(user_integer))

    try:
        user_input = input("Try again: ")
        attempts += 1
        user_integer = int(user_input)
    except ValueError:
        if (user_input != "exit"):
            print("The input has to be a number")

if (random_number == user_integer):
    print("Correct!!")

print("Number of attempts: " + str(attempts))

# Flush the number of attempts to a file
f = open("GuessingSteps.txt", "w")
f.write("Numer of attempts: " + str(attempts))
f.close()