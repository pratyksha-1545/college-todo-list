# Design Decisions and Rationale

## 1. Top-Down Design

The program starts from the overall `run()` function. The main problem is divided into smaller functions:

- Task operations
- Input validation
- Task analysis
- Searching/reporting
- Number algorithms
- Menu display

This follows the top-down problem-solving approach.

## 2. Data Representation

A task is represented by a dictionary:

```text
{"title": "Study Python", "status": "Pending"}
```

The complete task collection is a list of task dictionaries.

This uses the syllabus topics of lists and dictionaries without introducing classes.

## 3. Why No Database or File Storage?

The supplied syllabus does not include file handling or database programming. Therefore the application keeps the task list in memory while it is running.

## 4. Algorithms

### Counting

Task counts are calculated using a loop and an accumulator.

### Summation

`sum_title_lengths()` uses an accumulator to calculate the total number of characters in task titles.

### Factorial

`factorial()` uses iterative multiplication.

### Fibonacci

`fibonacci()` generates the requested number of values iteratively.

### Reverse

`reverse_text()` starts from the last character and moves toward the first character.

### Base Conversion

`decimal_to_binary()` repeatedly divides by 2 and builds the binary result.

### GCD

`gcd()` repeatedly uses the remainder operation until the second value becomes zero.

### Smallest Divisor

`smallest_divisor()` tests divisors starting at 2 and returns the first divisor.

### Prime Generation

`generate_primes()` checks each number using the prime test.

### Prime Factors

`prime_factors()` repeatedly divides by the current divisor when it is a factor.

### Linear Search

`find_task()` checks task titles one by one until the required title is found.

## 5. Time Tradeoff

The project intentionally keeps algorithms simple enough to trace manually. For example, task search uses linear search, which is straightforward but may inspect many tasks.

The project does not add a more advanced search or sorting algorithm because those are not required by the supplied syllabus.

## 6. Error Handling Strategy

The program validates empty task titles and positive integer input using conditionals and loops. Invalid menu choices are also handled by the menu conditions.

No exception-based framework is introduced because exception handling is not part of the supplied syllabus.

## 7. Resource Efficiency

The project uses simple lists, tuples, sets and dictionaries. No external services or libraries are required.

## 8. Maintainability

Each major responsibility is placed in a separate module. Functions have descriptive names and short comments.

## 9. Performance Discussion

Let `n` be the number of tasks.

- Viewing tasks: O(n)
- Counting tasks: O(n)
- Searching task titles: O(n) in the worst case
- Deleting by list position: O(n) in the worst case
- Finding unique words: proportional to the characters processed

These are intended as basic algorithm-analysis observations rather than advanced optimization.
