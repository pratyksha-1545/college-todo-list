"""Simple analysis of the To-Do list.

The calculations deliberately use fundamental algorithms from the syllabus.
"""

def count_tasks(task_list):
    """Count tasks using the counting algorithm."""
    count = 0

    for task in task_list:
        count = count + 1

    return count


def count_completed(task_list):
    """Count completed tasks."""
    count = 0

    for task in task_list:
        if task["status"] == "Completed":
            count = count + 1

    return count


def count_pending(task_list):
    """Count pending tasks."""
    count = 0

    for task in task_list:
        if task["status"] == "Pending":
            count = count + 1

    return count


def task_title_lengths(task_list):
    """Return a list containing the length of every task title."""
    lengths = []

    for task in task_list:
        length = 0
        for character in task["title"]:
            length = length + 1
        lengths.append(length)

    return lengths


def sum_title_lengths(task_list):
    """Calculate the total number of characters in task titles."""
    lengths = task_title_lengths(task_list)
    total = 0

    for length in lengths:
        total = total + length

    return total


def factorial(number):
    """Compute factorial using iteration."""
    result = 1

    if number < 0:
        return 0

    for value in range(1, number + 1):
        result = result * value

    return result


def fibonacci(number):
    """Return the first number Fibonacci values as a list."""
    sequence = []

    if number <= 0:
        return sequence

    first = 0
    second = 1

    for position in range(number):
        sequence.append(first)
        next_value = first + second
        first, second = second, next_value

    return sequence


def reverse_text(text):
    """Reverse text using indexing and a loop."""
    result = ""
    index = len(text) - 1

    while index >= 0:
        result = result + text[index]
        index = index - 1

    return result

