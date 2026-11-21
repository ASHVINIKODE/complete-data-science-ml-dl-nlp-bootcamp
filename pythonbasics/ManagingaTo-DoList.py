to_do_list = [
    "Buy groceries",
    "Clean the house",
    "Pay bills"
]

# Add new tasks
to_do_list.append("Schedule meeting")
to_do_list.append("Go for a run")

# Remove a completed task
to_do_list.remove("Clean the house")

# Check whether a task exists
if "Pay bills" in to_do_list:
    print("Don't forget to pay the utility bills!")

# Display remaining tasks
print("Remaining tasks:")
for task in to_do_list:
    print(task)