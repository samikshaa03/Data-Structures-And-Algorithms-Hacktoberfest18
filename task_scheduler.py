import heapq

class TaskScheduler:
    def __init__(self):
        self.tasks = []
        self.task_counter = 0

    def add_task(self, description, priority):
        task = (priority, self.task_counter, description)
        heapq.heappush(self.tasks, task)
        self.task_counter += 1

    def complete_task(self):
        if self.tasks:
            _, _, task_description = heapq.heappop(self.tasks)
            print(f"Completed task: {task_description}")
        else:
            print("No tasks to complete.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for _, _, task_description in self.tasks:
                print(task_description)
        else:
            print("No tasks to display.")

# Create a task scheduler
scheduler = TaskScheduler()

while True:
    print("\nTask Scheduler Menu:")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. View Tasks")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        description = input("Enter task description: ")
        priority = int(input("Enter task priority (1 - high, 2 - medium, 3 - low): "))
        scheduler.add_task(description, priority)
    elif choice == '2':
        scheduler.complete_task()
    elif choice == '3':
        scheduler.view_tasks()
    elif choice == '4':
        print("Exiting Task Scheduler.")
        break
    else:
        print("Invalid choice. Please try again.")
