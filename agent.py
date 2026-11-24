def build_plan(tasks, minutes_left):
    """Choose tasks by priority and skip any that do not fit."""
    plan = []
    skipped = []
    for task in sorted(tasks, key=lambda task: task[1]):
        name, _, duration = task
        if duration <= minutes_left:
            plan.append((name, duration))
            minutes_left -= duration
        else:
            skipped.append(name)
    return plan, skipped, minutes_left


def main():
    tasks = [
        ("Practice SQL joins", 1, 25),
        ("Review Python basics", 2, 20),
        ("Review Git commands", 3, 10),
    ]
    try:
        minutes = int(input("How many minutes can you study today? "))
        if minutes < 1:
            raise ValueError
    except ValueError:
        print("Enter a positive whole number of minutes.")
        return

    plan, skipped, spare_minutes = build_plan(tasks, minutes)
    print("\nYour study plan")
    if not plan:
        print("No tasks fit in the available time.")
    for name, duration in plan:
        print(f"- {name} ({duration} minutes)")
    if skipped:
        print("Save for later: " + ", ".join(skipped))
    print(f"Time left: {spare_minutes} minutes")


if __name__ == "__main__":
    main()
