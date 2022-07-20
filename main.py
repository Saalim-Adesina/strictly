import time
import tkinter as tk

try:
    # Fixes the blurry text problem
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
    
    #Creates the window
    main = tk.Tk()
    
    # # Initialises a text label makes it under the 'main' window  
    # message = tk.Label(main, text='Hellow, World! UwU')
    # # Displays the text
    # message.pack()

    # Set the window title
    main.title('strictly | a minimalist timer & todo ')
    current_title = main.title()
    print(current_title)
    
    # Set the width, height, x and y
    # width x height + x + y
    main.geometry('1000x500+500-0')

    # Setting the logo
    main.iconbitmap('icons\logo.ico')
    
finally:
    main.mainloop()



# Create a class called Timer

# Main class todo: contains a list of all the tasks
class ToDo:
    tasks = []
    def __init__(self, current_task:list):
        self.task = current_task

    def addTask(self):
        '''
        Adds a task into the tasks list
        '''
        self.tasks.append(self.task)
        
# The task class contains all the main functions of the tasks
class Task:
    def __init__(self, text, timer):
        self.text = text
        self.status = 'complete' #Can either be ongoing or complete
        self.timer = timer

class Timer:
    '''
    A class that takes one argument, time in seconds
    '''
    def __init__(self, time):
        self.time = time

    def __repr__(self):
        minutes, seconds = divmod(self.time, 60)
        hours, minutes = divmod(minutes, 60)
        return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

half_hour = Timer(1800)
hour = Timer(3600)


def count_down(sec):
    minutes, seconds = divmod(sec, 60)
    hours, minutes = divmod(minutes, 60)

    print(f'{hours} hours {minutes} minutes {seconds} seconds') 
# count_down(14674)

