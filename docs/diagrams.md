# Design Diagrams

The diagrams below can be pasted into a Mermaid-compatible Markdown viewer or recreated in a diagram tool for the final report.

## System Architecture Diagram

```mermaid
flowchart TD
    U[Student / User] --> M[main.py]
    M --> I[input_validation.py]
    M --> O[task_operations.py]
    M --> A[task_analysis.py]
    M --> S[search_and_report.py]
    M --> N[number_algorithms.py]
    M --> Menu[menu.py]
    O --> T[(In-memory task list)]
    A --> T
    S --> T
```

## Workflow Diagram

```mermaid
flowchart TD
    A[Start] --> B[Show Main Menu]
    B --> C{Choose Option}
    C -->|Add| D[Validate Title]
    D --> E[Create Task]
    C -->|View| F[Display Tasks]
    C -->|Complete| G[Validate Task Number]
    G --> H[Mark Completed]
    C -->|Delete| I[Validate Task Number]
    I --> J[Delete Task]
    C -->|Search| K[Linear Search]
    C -->|Report| L[Generate Report]
    C -->|Algorithm Lab| M[Run Selected Algorithm]
    C -->|Exit| N[Stop]
    E --> B
    F --> B
    H --> B
    J --> B
    K --> B
    L --> B
    M --> B
```

## Use Case Diagram

```mermaid
flowchart LR
    User((Student))
    Add[Add Task]
    View[View Tasks]
    Complete[Complete Task]
    Delete[Delete Task]
    Search[Search Task]
    Report[View Report]
    Lab[Run Algorithm Lab]

    User --> Add
    User --> View
    User --> Complete
    User --> Delete
    User --> Search
    User --> Report
    User --> Lab
```

## Component Diagram

```mermaid
flowchart TD
    Main[main.py]
    Main --> Task[task_operations]
    Main --> Analysis[task_analysis]
    Main --> Algorithms[number_algorithms]
    Main --> Search[search_and_report]
    Main --> Input[input_validation]
    Main --> Menu[menu]
```

## Sequence Diagram: Add Task

```mermaid
sequenceDiagram
    actor Student
    participant Main
    participant Input
    participant Task

    Student->>Main: Choose Add Task
    Main->>Input: Request title
    Input-->>Main: Valid title
    Main->>Task: create_task(tasks, title)
    Task-->>Main: True / False
    Main-->>Student: Display result
```

## Storage Design

There is no database in the current project.

The in-memory representation is:

```text
tasks = [
    {"title": "Study Python", "status": "Pending"},
    {"title": "Complete assignment", "status": "Completed"}
]
```

An ER diagram is therefore not applicable to the current implementation.
