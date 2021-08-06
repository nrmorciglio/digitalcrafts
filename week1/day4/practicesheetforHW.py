# loop = True

# todoList = {}

# while loop:
#     ans = input(
#         'Press 1 to add task \nPress 2 to delete tasks \nPress 3 to view all tasks \nPress q to quit the program\n')
#     if ans == 1:
#         addTask = input('which task would you like to delete?\n')
#         addPriority = input(
#             'what is the priority of this task? Please enter low / medium / high\n')

# todoList[addTask] = addPriority
# print('Here is your revised to do list' + str(todoList))

# elif ans == '2'
#     for key, value)
#     delTask =

index = 0

taskList = {'wash the car', 'post office', 'vacuum', 'buy gift',
            'make dinner', 'call mom', 'community bike ride'}

indexList = {len(taskList)}

mainMenu = str(input('Welcome to the To Do List program.\n\n'
                     '''How would you like to manage your tasks?\n
    Press 1 to add task
    Press 2 to delete task
    Press 3 to review current list of tasks
    Press q to quit program
    \n'''))


if mainMenu == '1':
    addTask = str(input('please enter the task you would like to add\n'))
    taskList.append(addTask)
    print(taskList)
    count = 1
    for addTask in taskList:
        print(count, taskList)
        count += 1

if mainMenu == '2':
    subTask = int(input(
        'please enter the corresponding index number to the task you would like to delete'))
    print(taskList)
    del taskList[subTask]
    print(taskList)
    while index < len(taskList):
        mainMenu = taskList[index]
    print(taskList)
    index = index + 1
    mainMenu = str(input(
        '''How would you like to manage your tasks?\n
            Press 1 to add task
            Press 2 to delete task
            Press 3 to review current list of tasks
            Press q to quit program
            \n'''))

if mainMenu == '3':
    while index < len(taskList):
        mainMenu = taskList
        print(taskList)
        index = index + 1
        mainMenu = str(input(
            '''How would you like to manage your tasks?\n
            Press 1 to add task
            Press 2 to delete task
            Press 3 to review current list of tasks
            Press q to quit program
            \n'''))

else:
    print('You have quit the program, please run it and try again')
# else:
#     print('invalid input')
#     mainMenu = str(input(
#         '''How would you like to manage your tasks?\n
#             Press 1 to add task
#             Press 2 to delete task
#             Press 3 to review current list of tasks
#             Press q to quit program
#             \n'''))
