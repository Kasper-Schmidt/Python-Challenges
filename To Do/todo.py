import json

TASKS = [
    {"id": 1, "task": "Rede seng", "done": False},
    {"id": 2, "task": "Træne", "done": False},
    {"id": 3, "task": "Læse", "done": False},
    {"id": 4, "task": "Backtest trading", "done": False}
]

FILE_NAME = "tasks.json"


def load_tasks(file_path=FILE_NAME):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        tasks = []
        for item in data:
            if not isinstance(item, dict):
                continue

            task_id = item.get("id")
            task_text = item.get("task")
            done = item.get("done", False)

            if not isinstance(task_id, int):
                continue
            if not isinstance(task_text, str) or not task_text.strip():
                continue
            if not isinstance(done, bool):
                done = False

            tasks.append({"id": task_id, "task": task_text, "done": done})

        return tasks

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks, file_path=FILE_NAME):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(tasks, file_path=FILE_NAME):
    task_text = input("What task do you want to add? ").strip()
    if not task_text:
        print("Task cannot be empty")
        return tasks

    next_id = 1
    if tasks:
        ids = [t.get("id", 0) for t in tasks if isinstance(t, dict)]
        next_id = (max(ids) + 1) if ids else 1

    new_task = {"id": next_id, "task": task_text, "done": False}
    tasks.append(new_task)

    save_tasks(tasks, file_path)
    print(f"Added task #{new_task['id']}: {new_task['task']}")
    return tasks


def delete_task(tasks, file_path=FILE_NAME):
    try:
        task_id = int(input("Enter id of the task you want to delete: ").strip())
    except ValueError:
        print("Invalid id. Please enter a number that exists")
        return tasks

    for i, task in enumerate(tasks):
        if isinstance(task, dict) and task.get("id") == task_id:
            deleted = tasks.pop(i)
            save_tasks(tasks, file_path)
            print(f"Deleted task #{deleted['id']}: {deleted['task']}")
            return tasks

    print(f"No task found with id {task_id}")
    return tasks


def main():
    tasks = load_tasks(FILE_NAME)

    # If no file yet, start with default TASKS and save them once
    if not tasks:
        tasks = TASKS.copy()
        save_tasks(tasks, FILE_NAME)

    while True:
        print("\n1) Add task")
        print("2) Reload tasks from file")
        print("3) Show all tasks")
        print("4) Delete task")
        print("5) Quit")

        choice = input("Choose: ").strip()

        if choice == "1":
            tasks = add_task(tasks, FILE_NAME)

        elif choice == "2":
            tasks = load_tasks(FILE_NAME)
            print("Reloaded tasks from file.")

        elif choice == "3":
            if not tasks:
                print("No tasks yet.")
            else:
                for t in tasks:
                    box = "[x]" if t.get("done") else "[ ]"
                    print(f"{box} {t.get('id')}: {t.get('task')}")

        elif choice == "4":
            tasks = delete_task(tasks, FILE_NAME)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
