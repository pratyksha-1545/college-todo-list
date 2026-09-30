# Testing Approach

## Testing Method

The project uses simple assertion-based validation in `tests/test_project.py`.

This keeps testing within the Python concepts used in the course.

## Test Areas

### Task Management

- Add a valid task
- Reject duplicate task title
- Find an existing task
- Complete a task
- Delete a task

### Fundamental Algorithms

- Factorial
- Fibonacci
- Reverse
- Decimal to binary
- GCD
- Smallest divisor
- Prime generation
- Prime factors

## Running Tests

```bash
python -m tests.test_project
```

Expected output:

```text
All tests passed.
```

## Example Test Cases

| Input | Expected result |
|---|---|
| Add `Study Python` | Task added |
| Add `Study Python` again | Rejected as duplicate |
| Factorial of 5 | 120 |
| Fibonacci count 7 | `[0, 1, 1, 2, 3, 5, 8]` |
| Reverse `Python` | `nohtyP` |
| Decimal 10 | `1010` |
| GCD 48, 18 | 6 |
| Primes up to 10 | `[2, 3, 5, 7]` |
| Prime factors of 60 | `[2, 2, 3, 5]` |
| Smallest divisor of 91 | 7 |
