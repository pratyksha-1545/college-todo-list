"""Simple validation tests using only Python assertions."""

from src.task_operations import (
    create_task,
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
    status_summary,
)


def run_tests():
    tasks = []

    assert create_task(tasks, "Study Python") is True
    assert create_task(tasks, "Complete assignment") is True
    assert create_task(tasks, "Study Python") is False

    assert find_task(tasks, "Study Python") == 0

    assert complete_task(tasks, 1) is True
    assert status_summary(tasks) == {"Pending": 1, "Completed": 1}

    assert delete_task(tasks, 2) is True
    assert len(tasks) == 1

    assert factorial(5) == 120
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    assert reverse_text("Python") == "nohtyP"

    assert decimal_to_binary(10) == "1010"
    assert gcd(48, 18) == 6
    assert smallest_divisor(91) == 7
    assert generate_primes(10) == [2, 3, 5, 7]
    assert prime_factors(60) == [2, 2, 3, 5]

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
