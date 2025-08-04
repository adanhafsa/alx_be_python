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
        Reminder = f"'{task}' is a high priority task"
    case "medium":
        Reminder = f"'{task}' is a medium priority task"
    case "low":
        Reminder = f"'{task}' is a low priority task"

# Adjust for time sensitivity
if time_bound == "yes":
    Reminder += " that requires immediate attention today!"
else:
    Reminder +=  " .Consider completing it when you have free time."

print(f"Reminder: {Reminder}")