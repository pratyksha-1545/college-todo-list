"""Fundamental and control-flow algorithms used by the project."""


def smallest_divisor(number):
    """Find the smallest divisor greater than 1."""
    if number < 2:
        return 0

    divisor = 2

    while divisor <= number:
        if number % divisor == 0:
            return divisor
        divisor = divisor + 1

    return number


def gcd(first, second):
    """Compute GCD by repeated remainder."""
    if first < 0:
        first = -first

    if second < 0:
        second = -second

    while second != 0:
        remainder = first % second
        first = second
        second = remainder

    return first


def is_prime(number):
    """Check primality using the smallest-divisor idea."""
    if number < 2:
        return False

    divisor = smallest_divisor(number)

    if divisor == number:
        return True

    return False


def generate_primes(limit):
    """Generate prime numbers from 2 through limit."""
    primes = []

    if limit < 2:
        return primes

    number = 2

    while number <= limit:
        if is_prime(number):
            primes.append(number)
        number = number + 1

    return primes


def prime_factors(number):
    """Generate the prime factors of a positive integer."""
    factors = []

    if number < 2:
        return factors

    divisor = 2

    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor = divisor + 1

    return factors


def decimal_to_binary(number):
    """Convert a non-negative decimal integer to binary."""
    if number == 0:
        return "0"

    binary = ""

    while number > 0:
        remainder = number % 2

        if remainder == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary

        number = number // 2

    return binary
