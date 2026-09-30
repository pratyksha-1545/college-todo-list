"""College To-Do List
A first-semester Python project based only on the supplied syllabus.
"""

from src.task_operations import (
    create_task,
    show_tasks,
    complete_task,
    delete_task,
)
from src.task_analysis import (
    factorial,
    fibonacci,
    reverse_text,
)
from src.number_algorithms import (
    decimal_to_binary,
    gcd,
    generate_primes,
    prime_factors,
    smallest_divisor,
)
from src.search_and_report import (
    find_task,
    make_report,
)
from src.input_validation import (
    get_non_empty_title,
    get_positive_integer,
)
from src.menu import show_menu, algorithm_menu


def view_tasks(task_list):
    """Print all tasks."""
    lines = show_tasks(task_list)

    for line in lines:
        print(line)


def algorithm_lab():
    """Run the selected fundamental algorithm."""
    while True:
        algorithm_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            number = get_positive_integer("Enter a positive integer: ")
            print("Factorial:", factorial(number))

        elif choice == "2":
            number = get_positive_integer("How many Fibonacci values: ")
            print("Fibonacci:", fibonacci(number))

        elif choice == "3":
            text = input("Enter text: ")
            print("Reverse:", reverse_text(text))

        elif choice == "4":
            number = get_positive_integer("Enter a non-negative integer: ")
            print("Binary:", decimal_to_binary(number))

        elif choice == "5":
            first = get_positive_integer("Enter first positive integer: ")
            second = get_positive_integer("Enter second positive integer: ")
            print("GCD:", gcd(first, second))

        elif choice == "6":
            limit = get_positive_integer("Generate primes up to: ")
            print("Primes:", generate_primes(limit))

        elif choice == "7":
            number = get_positive_integer("Enter a positive integer: ")
            print("Prime factors:", prime_factors(number))

        elif choice == "8":
            number = get_positive_integer("Enter an integer >= 2: ")
            print("Smallest divisor:", smallest_divisor(number))

        elif choice == "9":
            break

        else:
            print("Invalid choice.")


def run():
    """Run the main To-Do List workflow."""
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = get_non_empty_title()

            if create_task(tasks, title):
                print("Task added.")
            else:
                print("Task already exists.")

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            view_tasks(tasks)
            number = get_positive_integer("Enter task number: ")

            if complete_task(tasks, number):
                print("Task completed.")
            else:
                print("Invalid task number.")

        elif choice == "4":
            view_tasks(tasks)
            number = get_positive_integer("Enter task number: ")

            if delete_task(tasks, number):
                print("Task deleted.")
            else:
                print("Invalid task number.")

        elif choice == "5":
            title = get_non_empty_title()
            position = find_task(tasks, title)

            if position == -1:
                print("Task not found.")
            else:
                print("Task found at position:", position + 1)

        elif choice == "6":
            report = make_report(tasks)

            for line in report:
                print(line)

        elif choice == "7":
            algorithm_lab()

        elif choice == "8":
            print("Thank you for using the College To-Do List.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    run()
