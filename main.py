print(("1:View tasks " '|' " 2:Add task " '|' " 3:Delete task " '|' " 4:Exit app"))

list = []

while True:
    # this section views the tasks after you add them by clicking 1
    user = int(input(": "))
    if user == 1:
        for i in enumerate(list):
            print(i[0]+1,'-', i[1]) # adds increased numbers to each item added
        print("\n")
        print(("1:View tasks " '|' " 2:Add task " '|' " 3:Delete task " '|' " 4:Exit app"))

    # this section adds a new task to the list by clicking 2 and write your task
    elif user == 2:
        task = input("Task: ")
        list.append(task) # Adds the task to the [list]
        print("Task successfuly added.")
        print("\n")
        print(("1:View tasks " '|' " 2:Add task " '|' " 3:Delete task " '|' " 4:Exit app"))

    # this section deletes an item from the list by choosing the number of which item you want to delete 
    if user == 3:
        for i in enumerate(list):
            print(i[0]+1,'-', i[1])
        delete = int(input("Delete a task: "))
        del list[delete] # Removes the the choosen item from the variable (delete) "choose by number"
        print(f"Task {delete} successfuly removed")
        print(("1:View tasks " '|' " 2:Add task " '|' " 3:Delete task " '|' " 4:Exit app"))

        if user != 1 or 2 or 3 or 4:
            print("")

    # clicking 4 will exit the app
    elif user == 4:
        print("Exited the app")
        break

    # saves the file in a file named "saves.txt"
file = open("saves.txt", "a")
file.write('\n'.join(list))
file.close