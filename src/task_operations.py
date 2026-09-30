"""Basic To-Do task operations.

Uses only syllabus-level concepts:
lists, dictionaries, tuples, sets, functions, conditionals and loops.
"""

def create_task(task_list, title):
    """Add one task if the title is not empty and not already present."""
    if title == "":
        return False

    for task in task_list:
        if task["title"] == title:
            return False

    task = {"title": title, "status": "Pending"}
    task_list.append(task)
    return True


def show_tasks(task_list):
    """Return a tuple containing the task list in display-ready form."""
    display = []

    if len(task_list) == 0:
        return ("No tasks available.",)

    number = 1
    for task in task_list:
        display.append(str(number) + ". " + task["title"] + " - " + task["status"])
        number = number + 1

    return tuple(display)


def complete_task(task_list, task_number):
    """Mark a selected task as completed."""
    if task_number >= 1 and task_number <= len(task_list):
        task_list[task_number - 1]["status"] = "Completed"
        return True

    return False


def delete_task(task_list, task_number):
    """Delete a selected task."""
    if task_number >= 1 and task_number <= len(task_list):
        task_list.pop(task_number - 1)
        return True

    return False

