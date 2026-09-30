# College To-Do List

## Overview

**College To-Do List** is a menu-driven Python project for managing a small list of college tasks. It is intentionally designed around the first-semester syllabus supplied for the project.

The project demonstrates problem solving, top-down design, algorithms, flow of execution, functions, parameters and arguments, conditionals, iteration, lists, tuples, sets, dictionaries, searching, counting, summation, factorial, Fibonacci sequence, reverse, base conversion, character-to-number conversion, GCD, smallest divisor, prime generation and prime factorization.

The project does **not** use classes, external packages, databases, files for application data, web frameworks, dates, exception-handling frameworks, JSON, or other topics outside the supplied syllabus.

## Major Functional Modules

1. **Task Management**
   - Add a task
   - View tasks
   - Mark a task completed
   - Delete a task
   - Duplicate-title validation

2. **Task Search and Reporting**
   - Linear search for a task
   - Count pending/completed tasks
   - Generate a simple report
   - Use a set to count unique words in task titles

3. **Algorithm Lab**
   - Factorial
   - Fibonacci sequence
   - Reverse text
   - Decimal-to-binary conversion
   - GCD
   - Smallest divisor
   - Prime number generation
   - Prime factorization

## Technologies / Tools

- Python 3
- Git
- GitHub
- No external Python libraries

## Project Structure

```text
college-todo-list/
│
├── main.py
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── task_operations.py
│   ├── task_analysis.py
│   ├── number_algorithms.py
│   ├── search_and_report.py
│   ├── input_validation.py
│   └── menu.py
│
├── tests/
│   └── test_project.py
│
└── docs/
    ├── diagrams.md
    ├── design_decisions.md
    ├── testing.md
    └── project_report.md
```

## Requirements

Python 3 is required.

No `pip install` command is required because the project uses only the Python standard language features covered in the course.

## How to Run

Open a terminal in the project folder and run:

```bash
python main.py
```

The program displays a menu.

### Main menu

```text
1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Search task
6. Task report
7. Algorithm lab
8. Exit
```

## Testing

Run:

```bash
python -m tests.test_project
```

Expected result:

```text
All tests passed.
```

The tests use assertions and validate task operations and the fundamental algorithms.

## Syllabus Mapping

| Syllabus concept | Where it appears |
|---|---|
| Problem solving / top-down design | Project decomposition and `main.py` |
| Programs and algorithms | All `src` modules |
| Flowcharts / workflow | `docs/diagrams.md` |
| Analysis of algorithms | `docs/design_decisions.md` |
| Interpreter / interactive mode | Program is run with `python main.py` |
| Values and types | Integers, strings, lists, tuples, sets, dictionaries |
| Variables / expressions / statements | All Python files |
| Tuple assignment | `number_algorithms.py` uses multiple variables in algorithmic steps |
| Precedence of operators | Arithmetic and remainder expressions |
| Comments | Source files |
| Modules and functions | All files under `src/` |
| Parameters and arguments | Functions across `src/` |
| Conditionals | Menus and algorithm decisions |
| `while` / `for` | Task operations and algorithms |
| `break` / `continue` | Input validation and menu flow |
| Counting | `task_analysis.py` |
| Summation | `sum_title_lengths()` |
| Factorial | `factorial()` |
| Fibonacci | `fibonacci()` |
| Reverse | `reverse_text()` |
| Base conversion | `decimal_to_binary()` |
| Character to number | `character_to_digit()` |
| Lists | Tasks, prime numbers, factors |
| Tuples | Display and report results |
| Sets | Unique title words |
| Dictionaries | Task records and status summary |
| GCD | `gcd()` |
| Smallest divisor | `smallest_divisor()` |
| Generate prime numbers | `generate_primes()` |
| Prime factors | `prime_factors()` |
| Time tradeoff | Linear search/report choices are discussed in documentation |

## Academic Scope

This project is intentionally kept at a beginner first-semester level. Each function has a direct purpose and is used by the application or tests. There are no artificial classes or unnecessary helper layers.

## Future Enhancements

Possible future versions could add persistent storage, a graphical interface or a database, but those are intentionally outside the current implementation because they are not part of the supplied syllabus.
