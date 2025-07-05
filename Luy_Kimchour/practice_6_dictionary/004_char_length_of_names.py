names = ["Anna", "Benjamin", "Cathy", "Dann", "Eleanor", "Frank"]

def get_char_length_dictionary(names):
    char_length_dictionary = {}

    for name in names:
        if len(name) not in char_length_dictionary:
            # if it isn't in the list, initialize the list
            char_length_dictionary[len(name)] = []

        char_length_dictionary[len(name)].append(name)

    return char_length_dictionary


if __name__ == "__main__":
    print(get_char_length_dictionary(names))
