import sys

# Verify at least 2 arguments are provided
arguments_count = len(sys.argv)

if (arguments_count < 3):
    print("You should provide at least 2 arguments (The filename, ...words to find)")
else:
    # Get the arguments
    argument1 = sys.argv[1]
    words_dictionary = dict()

    try:
        filename = str(argument1)
        # Get the rest of arguments
        for i in range(2, arguments_count):
            words_dictionary[sys.argv[i]] = 0

        # Read the file
        file1 = open(filename, "r")
        file_content = file1.read()
        file_items = file_content.split()

        # Count the ocurrences
        for item in file_items:
            try:
                words_dictionary[item] = words_dictionary[item] + 1
            except KeyError:
                pass

        print(words_dictionary)

    except ValueError:
        print("Incompatible arguments")