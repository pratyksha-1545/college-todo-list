"""Searching, set operations and simple reporting."""

from src.task_analysis import count_tasks, count_completed, count_pending, sum_title_lengths


def find_task(task_list, title):
    """Find a task by title using linear search."""
    index = 0

    while index < len(task_list):
        if task_list[index]["title"] == title:
            return index
        index = index + 1

    return -1


def unique_words(task_list):
    """Return the set of words used in task titles."""
    words = set()

    for task in task_list:
        title = task["title"]
        current_word = ""

        for character in title:
            if character == " ":
                if current_word != "":
                    words.add(current_word)
                    current_word = ""
            else:
                current_word = current_word + character

        if current_word != "":
            words.add(current_word)

    return words


def status_summary(task_list):
    """Return a dictionary containing task counts."""
    summary = {"Pending": 0, "Completed": 0}

    for task in task_list:
        if task["status"] == "Pending":
            summary["Pending"] = summary["Pending"] + 1
        elif task["status"] == "Completed":
            summary["Completed"] = summary["Completed"] + 1

    return summary


def make_report(task_list):
    """Create a tuple of report lines."""
    summary = status_summary(task_list)
    report = (
        "Total Tasks: " + str(count_tasks(task_list)),
        "Pending Tasks: " + str(count_pending(task_list)),
        "Completed Tasks: " + str(count_completed(task_list)),
        "Total Title Characters: " + str(sum_title_lengths(task_list)),
        "Unique Words in Titles: " + str(len(unique_words(task_list))),
    )

    return report
