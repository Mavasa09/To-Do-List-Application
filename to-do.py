import os
todo_list_file='tasks.txt'

def load_tasks():
 if not os.path.exists(todo_list_file):
    with open (todo_list_file,'w')as file:
     pass
    with open (todo_list_file,'r')as file:
     return[line.strip()for line in file.readlines()]

def save_tasks(tasks):
    #saves the current list of tasks to the file#
    with open(todo_list_file,'w') as file:
        for task in tasks:
            file.write(task+'\n')
            
def display_tasks(tasks):
    #Displays the current list of available tasks
    
    if not tasks:
        
        print('\n Oop! Your TO-DO LIST IS EMPTY!')
    else:
     print('\n Your TO-DO List:')    
     for idx,task in enumerate(tasks,start=1):
         print(f'{idx}.{task}')
         
def add_tasks(tasks):
    #Adding New Tasks To The List#
    task=input('Enter the new task:')
    tasks.append(tasks)
    save_tasks(tasks)
    print(f'This Task"{task}" Is Successfully Added!.')   
    
def delete_task(tasks):
     #This deletes the tasks by its number
     display_tasks(tasks)
     try:
         task_num=int(input('Please Enter the task number to delete'))   
         if 1 <= task_num <=len(tasks):
             removed_task=tasks.pop(task_num-1)
             save_tasks(tasks)
             print(f'Task"{removed_task}"been  deleted!')
         else:
             print('Invalid Task Number!') 
     except ValueError: 
         print('Please enter a valid number!')   

def main():
    tasks=load_tasks() 
    while True:
        print('\nTo-Do-List Men:')
        print('1.View Tasks') 
        print('2.Add Task')
        print('3.Delete Task')
        print('4.EXIT')   
        
        choice=input('Please Enter Your Choice(1/2/3/4)')  
        
        if choice=='1':
            display_tasks(tasks)
        elif choice=='2':
            add_tasks(tasks)
        elif choice=='3':
            delete_task(tasks)
        elif choice=='4':
            print('Bye!')
        break
        
    else:
        print('Invalid Choice.please choose the right Choices 1,2,3,4')


main()    