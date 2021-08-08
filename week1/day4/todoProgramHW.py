

taskList = []
mainMenuResponse = ''
mainMenu = '''\nWelcome to the To Do List program.\n
                 How would you like to manage your tasks?\n
    Press 1 to add task
    Press 2 to delete task
    Press 3 to review current list of tasks
    Press q to quit program
    \n\n'''


while mainMenuResponse != 'q':
    mainMenuResponse = input(mainMenu)

    if mainMenuResponse == '1':
        print('Current Task List:')
        print(taskList)
        addTask = input(
            "Please enter the new task you would like to add.\n    Example entry: wash dog\n\n")
        addPrio = input(
            "Please enter the priority of the task you would like to add (high, medium, low).\n    Example entry: high\n\n")
        newTask = (addTask + ' ' + addPrio)
        taskList.append(newTask)

    if mainMenuResponse == '2':
        print('Current Task List:')
        print(taskList)
        taskToDelete = int(
            input('\nWhich task would you like to delete?\n')) - 1
        del taskList[taskToDelete]
        print('Your task has been deleted ')
        print(taskList)

    if mainMenuResponse == '3':
        print('Current Task List:')
        print(taskList)
