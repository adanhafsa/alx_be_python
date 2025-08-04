# Personal Daily Reminder

# prompt the user to input a task description and save it into a task variable
task = input("Enter your task: ")

while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break

while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break

# Process priority with match
match priority:
    case "high":
        base_msg = f"'{task}' is a high priority task"
    case "medium":
        base_msg = f"'{task}' is a medium priority task"
    case "low":
        base_msg = f"'{task}' is a low priority task"

# Adjust for time sensitivity
if time_bound == "yes":
    Reminder = f" Reminder: {base_msg} that requires immediate attention today!"
else:
    Reminder = f" Note: {base_msg}. Consider completing it when you have free time."

print(Reminder)