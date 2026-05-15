#to add task, removetask , and mark tasks as complete

#add task to task manager

def add_task():
    task_name=input("Enter Your Task:")
    task={
        "name":task_name,
        "complete":False
    }
    tasks.append(task)
    add=str(tasks)
    with open("day7\\weekly milestone\\task_manager.txt","w") as file:
        file.write(add)
    print("Task Added to Your list")

#remove task from task manager
def remove_task():
    task_name=input("Enter Your Task:")
    for task in tasks:
        if task["name"]==task_name:
            tasks.remove(task)
            rem=str(tasks)
            print("Task Removed from Your List")
            with open("day7\\weekly milestone\\task_manager.txt","w") as file:
                file.write(rem)
            
            break
    else:
        print("Task not Found")

#mark task as completed in task manager
def task_complete():
    task_name=input("Enter Your Task:")
    for task in tasks:
        if task["name"]==task_name:
            task["complete"]=True
            com=str(tasks)
            print("Task marked as complete")
            with open("day7\\weekly milestone\\task_manager.txt","w") as file:
                file.write(com)
            break
    else:
        print("Task not Found")

tasks=[]
while True:
    print("\nTASK MANAGER\n")
    print("Select one from the below options:")
    print("1. Add Tasks to Task Manager")
    print("2. Remove Tasks From Task Manager")
    print("3. Mark Tasks as Complete in Task Manager")
    print("4. Exit Task Manager")
    choice=int(input("Enter your choice[1-4]:"))
    if choice==1:
        add_task()
    elif choice==2:
        remove_task()
    elif choice==3:
        task_complete()
    elif choice==4:
        print("Existing...")
        break
    else:
        print("Invalid Option!!!")
    