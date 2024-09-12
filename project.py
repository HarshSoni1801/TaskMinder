import sys
import os
import csv
from tabulate import tabulate
from datetime import datetime
import emoji

#Status indicators using emojis
incomplete=emoji.emojize(':cross_mark: Incomplete', language='alias')
complete=emoji.emojize(':check_mark_button: complete', language='alias')
upcoming=emoji.emojize(':calendar: upcoming', language='alias')
eve_completed=emoji.emojize(':check_mark_button: completed',language='alias')

#Display input menu option
def input_menu():
        print('Choose any of the following:\n1.Add Task\n2.View Tasks\n3.Mark Task as Complete\n4.Add Event\n5.View Events\n6.Show Reminders for Upcoming Tasks and Events\n7.Exit')
        match(int(input())):
            case 1:
                add_task()
            case 2:
                view_task()
            case 3:
                mark_task()
            case 4:
                add_event()
            case 5:
                view_event()
            case 6:
                reminder()
            case 7:
                sys.exit('Exiting...')
            case _:
                raise(ValueError('Invalid Input!'))
            
#Function to add new task to the task list
def add_task():
    #Declaring the headers
    headers=['Task Name','Deadline','Priority','Description','Status']
    task_name=input('Task Name: ').strip()

    #Taking date input from user 
    while True:
        try:
            D=input('Deadline(YYYY-MM-DD HH:MM in 24 Hr Format): ')
            task_deadline=datetime.strptime(D,"%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M")
            break
        except ValueError:
            print('Invalid Date format! Enter again.')

    #Validating Priority
    while True:
        task_prio=int(input('Priority(0 to 10 where 0 is highest): '))
        if(task_prio in range(0,11)):
            break
        else:
            print('Out of Range!')

    task_des=input('Task Description(Optional): ').strip()
    file_name='list_of_tasks.csv'
    
    #Checking whether the file exists  and appending tasks
    file_exists=os.path.exists(file_name)
    with open(file_name,mode='a', newline='',encoding='utf-8') as file:
        writer=csv.DictWriter(file,fieldnames=headers)

        #checking the file exits but is empty
        if not file_exists or os.path.getsize(file_name)==0 :
            #Writing headser
            writer.writeheader()
        
        writer.writerow({'Task Name': task_name,'Deadline':task_deadline,'Priority':task_prio,'Description':task_des,'Status':incomplete})

#View tasks sorted by
def view_task():
    file_name='list_of_tasks.csv'
    
    #checking whether the file exists 
    try:
        with open(file_name,mode='r', newline='',encoding='utf-8') as file:
            reader=csv.reader(file)
            header=next(reader)
            tasks=list(reader)
            #sorting tasks based on Priority
            tasks.sort(key=lambda x:int(x[2]))
            table=[header]+tasks
            print(tabulate(table,headers='firstrow',tablefmt="grid"))
    except FileNotFoundError:
        print('File Not Found')

#Mark a task as complete
def mark_task(): 
    file_name='list_of_tasks.csv'
    _name=input('Enter the name of task: ')

    #checking whether the file exists 
    try:
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader=csv.DictReader(file)
            tasks=list(reader)
            header=reader.fieldnames
    except FileNotFoundError:
        print('File Not Found')
        return
    #Modifying the values
    found=0
    for task in tasks:
        if task['Task Name']==_name: 
            task['Status']=complete
            found=1
            break
    if not found:
        print(f"Task '{_name}' not found!")
        return
    
    #rewriting the value in the csv file
    with open(file_name, mode='w', newline='',encoding='utf-8') as file:
        writer=csv.DictWriter(file,fieldnames=header)
        writer.writeheader()
        writer.writerows(tasks)

#Function to add new event
def add_event():
    #Declaring the headers
    headers=['Event Name','Date','Location','Description','Status']
    event_name=input('event Name: ').strip()

    #Taking date input from user 
    while True:
        try:
            D=input('date(YYYY-MM-DD HH:MM in 24 Hr Format): ')
            event_date=datetime.strptime(D,"%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M")
            break
        except ValueError:
            print('Invalid Date format! Enter again.')

    event_loc=input('Location: ')
    event_des=input('event Description(Optional): ').strip()
    file_name='list_of_events.csv'
    
    #checking whether the file exists and appending values 
    file_exists=os.path.exists(file_name)
    with open(file_name,mode='a', newline='',encoding='utf-8') as file:
        writer=csv.DictWriter(file,fieldnames=headers)

        #checking the file exits but is empty
        if not file_exists or os.path.getsize(file_name)==0 :
            #Writing header
            writer.writeheader()
        
        writer.writerow({'Event Name': event_name,'Date':event_date,'Location':event_loc,'Description':event_des,'Status':upcoming})

#Function to view events sorted by date
def view_event():
    file_name='list_of_events.csv'
    #checking whether the file exists 
    try:
        with open(file_name,mode='r', newline='',encoding='utf-8') as file:
            reader=csv.DictReader(file)
            header=reader.fieldnames
            events=list(reader)
            #sorting events based on date
            for event in events:
                event['Date']=datetime.strptime(event['Date'],"%Y-%m-%d %H:%M")
            events.sort(key=lambda x:x['Date'])

            #Converting back to strings
            for event in events:
                event['Date']=event['Date'].strftime("%Y-%m-%d %H:%M")
            table=[header]+[list(event.values()) for event in events]
            print(tabulate(table,headers='firstrow',tablefmt="grid"))
    except FileNotFoundError:
        print('File Not Found')

#Function to calculate time left for a task/event
def time_left(date):
    curr_time=datetime.now().replace(second=0, microsecond=0)
    deadline=datetime.strptime(date,"%Y-%m-%d %H:%M")

    #calculating time left from the present day to the deadline of task/Event
    total_secs=(deadline-curr_time).total_seconds()
    if(total_secs<0):
        return 'Event/Task passed'
    days_left=int(total_secs//86400)
    hours_left=int((total_secs%86400)//3600)
    mins_left=int((total_secs%3600)//60)

    #returning remaining time in readable format
    if(days_left>0):
        if(days_left==1):
            return (f'{days_left} day and {hours_left} hours left')
        return (f'{days_left} days and {hours_left} hours are left')
    elif(hours_left>0):
        if(hours_left==1):
            return (f'{hours_left} hour and {mins_left} mins are left')
        return (f'{hours_left} hours and {mins_left} mins are left')
    elif mins_left > 0:
        if mins_left == 1:
            return f'{mins_left} minute left'
        return f'{mins_left} minutes left'
    else:
        return 'Due now'

#converting date itmes so that they can be compared
def convert_comparable(str):
    if 'day' in str:
        return int(str.split()[0])*24
    elif 'hour' in str:
        return int(str.split()[0])
    else:
        return 0

#Function to display combined table of upcoming tasks and events
def reminder():
    task_file='list_of_tasks.csv'
    event_file='list_of_events.csv'
    rem_tasks=[]
    rem_events=[]
    with open(task_file, mode='r', newline='',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row['Status']==incomplete:
                rem_tasks.append({
                    'Name':row['Task Name'],'Time Left':time_left(row['Deadline'])
                    })

    with open(event_file, mode='r', newline='',encoding='utf-8') as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row['Status']==upcoming:
                rem_events.append({
                    'Name':row['Event Name'],'Time Left':time_left(row['Date'])
                })
    combined=rem_tasks+rem_events
    combined.sort(key=lambda x:convert_comparable(x['Time Left']))
    headers=['Name','Time Left']
    table=[headers]+[list(item.values()) for item in combined]
    print(tabulate(table,headers='firstrow',tablefmt='grid'))

#Main function.
def main():
    print('*********** TaskMinder ***********')
    input_menu()

if __name__=="__main__":
    main()