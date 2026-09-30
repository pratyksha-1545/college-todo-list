# College To-Do List — Project Report

> This document is a report-ready draft. Add the student's name, registration details, screenshots and final observations before submission.

## 1. Cover Page

**Project Title:** College To-Do List  
**Subject:** Problem Solving / Python  
**Student Name:** ____________________  
**Registration Number:** ____________________  
**Section:** ____________________  
**Faculty:** ____________________  
**Academic Year:** ____________________

## 2. Introduction

The College To-Do List is a menu-driven Python application designed for a college student. It provides basic task management while demonstrating the problem-solving and algorithmic concepts covered in the semester syllabus.

The project follows a top-down design. The complete application is divided into small functions and modules so that each part has a clear responsibility.

## 3. Problem Statement

College students manage multiple academic activities. A simple task list can provide a clear way to record and track these activities.

The project solves this problem with a command-line application that allows the user to add, view, search, complete and delete tasks.

## 4. Objectives

1. Apply top-down problem solving.
2. Implement functions with parameters and arguments.
3. Use conditionals and iteration.
4. Use lists, tuples, sets and dictionaries.
5. Implement fundamental algorithms from the syllabus.
6. Practice basic algorithm analysis.
7. Build a modular GitHub project.

## 5. Functional Requirements

1. The user can add a task.
2. The user can view tasks.
3. The user can complete a task.
4. The user can delete a task.
5. The user can search for a task.
6. The user can view a task report.
7. The user can run the Algorithm Lab.

## 6. Non-Functional Requirements

### Usability
The program uses a simple numbered menu and clear messages.

### Performance
The project uses simple algorithms suitable for a small college task list.

### Maintainability
The code is divided into modules with focused functions.

### Reliability
Input validation prevents empty task titles and invalid positive-integer input.

### Resource Efficiency
The application uses only in-memory Python data structures and requires no external package.

## 7. System Architecture

The application contains a main control module and supporting modules for task operations, analysis, algorithms, searching/reporting, validation and menu display.

See `diagrams.md` for the architecture and workflow diagrams.

## 8. Design Diagrams

The repository contains:

- System Architecture Diagram
- Workflow Diagram
- Use Case Diagram
- Component Diagram
- Sequence Diagram

An ER diagram is not applicable because the project does not use database storage.

## 9. Design Decisions and Rationale

The project intentionally uses only concepts available in the supplied syllabus. Tasks are represented with dictionaries and stored in a list. Functions are used instead of classes.

The application does not use persistent files or a database because those concepts are outside the supplied syllabus.

The Algorithm Lab demonstrates the fundamental algorithms directly rather than adding unrelated functionality.

## 10. Implementation Details

### Task Management

The task list is a list of dictionaries. Each dictionary stores a title and status.

### Search

Linear search checks task titles one by one.

### Analysis

Counting and summation are implemented with loops and accumulators.

### Fundamental Algorithms

The project implements factorial, Fibonacci, reverse, decimal-to-binary conversion, GCD, smallest divisor, prime generation and prime factorization.

### Data Structures

Lists, tuples, sets and dictionaries are used where their behavior directly supports the project.

## 11. Screenshots / Results

Add screenshots here after running the application:

1. Main menu
2. Adding a task
3. Viewing tasks
4. Completing a task
5. Task report
6. Algorithm Lab
7. Test output

## 12. Testing Approach

The project contains assertion-based tests in `tests/test_project.py`.

Run:

```bash
python -m tests.test_project
```

Expected result:

```text
All tests passed.
```

## 13. Challenges Faced

- Breaking the problem into small functions.
- Representing tasks using basic data structures.
- Validating user input without using advanced libraries.
- Implementing fundamental algorithms manually.
- Keeping the project within the semester syllabus.

## 14. Learnings and Key Takeaways

The project provided practice in:

- Top-down design
- Algorithm development
- Flow of execution
- Functions
- Parameters and arguments
- Conditionals
- Loops
- Lists
- Tuples
- Sets
- Dictionaries
- Basic algorithm analysis
- GitHub project organization

## 15. Future Enhancements

Possible future enhancements include persistent storage or a graphical interface. These are intentionally not implemented in this version because they are outside the current course scope.

## 16. References

1. Supplied VITyarthi Build Your Own Project guidelines.
2. Course syllabus supplied for the semester.
