"""Input validation using basic conditionals and loops."""


def get_non_empty_title():
    """Read a non-empty task title."""
    while True:
        title = input("Enter task title: ").strip()

        if title != "":
            return title

        print("Task title cannot be empty.")


def get_positive_integer(message):
    """Read a positive integer."""
    while True:
        value = input(message)

        if value == "":
            print("Enter a number.")
            continue

        number = 0
        valid = True

        for character in value:
            digit = character_to_digit(character)

            if digit == -1:
                valid = False
                break

            number = number * 10 + digit

        if valid and number > 0:
            return number

        print("Enter a positive integer.")


def character_to_digit(character):
    """Convert one digit character to an integer."""
    if character == "0":
        return 0
    elif character == "1":
        return 1
    elif character == "2":
        return 2
    elif character == "3":
        return 3
    elif character == "4":
        return 4
    elif character == "5":
        return 5
    elif character == "6":
        return 6
    elif character == "7":
        return 7
    elif character == "8":
        return 8
    elif character == "9":
        return 9

    return -1
