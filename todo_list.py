def print_menu():
    print('\nTodo List Menu:')
    print('1. View Tasks')
    print('2. Add a Task')
    print('3. Remove a Task')
    print('4. Exit')
def get_user_choice():
    while True:
        choice=int(input('Enter your choice: '))
        valid_choices=(1,2,3,4)

        if choice not in valid_choices:
            print('Invalid choice! Please enter number 1-4: ')
            continue
        else:
            return choice
def display_tasks(tasks):
    if not tasks:
        print('There are no tasks')
        return
    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')
def add_task(tasks):
    while True:
        task=input('Enter a new task: ').strip()
        if len(tasks)!=0:
            tasks.append(task)
            break
        else:
            print('Invalid task name')
def remove_task(tasks):
    display_tasks(tasks)
    while True:
        try:
            task_number=int(input('Enter the task number to remove: '))
            if 1<=task_number <=len(tasks):
                tasks.pop(task_number-1)
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid task number!')
def main():
    tasks=[]
    while True:
        print_menu()
        choice=get_user_choice()
        if choice==1:
            display_tasks(tasks)
        elif choice==2:
            add_task(tasks)
        elif choice==3:
            remove_task(tasks)
        else:
            break
if __name__=='__main__':
    main()