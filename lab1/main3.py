import sys

# Verify at least 2 arguments are provided
argumentsCount = len(sys.argv)

if (argumentsCount < 3):
    print("You should provide at least 2 arguments (The filename, ...words to find)")
else:
    # Get the arguments
    argument1 = sys.argv[1]
    wordsDictionary = dict()

    try:
        filename = str(argument1)
        # Get the rest of arguments
        for i in range(2, argumentsCount):
            wordsDictionary[sys.argv[i]] = 0

        # Read the file
        file1 = open(filename, "r")
        fileContent = file1.read()
        fileItems = fileContent.split()

        # Count the ocurrences
        for item in fileItems:
            try:
                wordsDictionary[item] = wordsDictionary[item] + 1
            except KeyError:
                pass

        print(wordsDictionary)

    except ValueError:
        print("Incompatible arguments")