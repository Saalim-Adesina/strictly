import time
import tkinter as tk
from tkinter import ttk
import pyperclip as pyp

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

    # Setting the logo
    main.iconbitmap('icons\logo.ico')
    
    # Set the window title
    main.title('strictly | a minimalist timer & todo ')
    current_title = main.title()
    print(current_title)
    
    # Window Height, width and cordinates 
    # Set the window to be displayed in the center
    window_width = 950
    window_height = 600

    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    
    # minimum resizable width and height
    main.minsize(width=600, height=300)
    
    #? Newer Widgets
    label = ttk.Label(main, text=f'{main.geometry()}')
    label.pack()
    # tk.Label(main, text=f'{main.geometry()}').pack() #? Older widget

    #> Different ways to set the attributes of a widget
    # using config on the widget object and setting the attributes eg: label = ttk.Label(...) label.config(text='jeff')
    # doing it dictionairy style eg: Label = ttk.Label(...) Label[text] = 'jeff'

    #> Command binding
    
    # Call back function
    def button_clicked():
        print('Stop clicking me')
    
    def game_selection(option):
        print(option)

    ttk.Button(main, text='click Me', command=button_clicked).pack()
    
    #? We use lamda so we don't call the function just yet but only when clicked
    ttk.Button(main,text='Paper',command= lambda: game_selection('Paper')).pack()
    ttk.Button(main,text='Scissors',command= lambda: game_selection('Scissors')).pack()
    ttk.Button(main,text='Rock',command= lambda: game_selection('Rock')).pack()

    #TODO Continue from event binding...
    def copytext(event):
        print(f'Shift pressed')
    
    def log(event):
        print(f'window binded event: {event}')

    #> ALl TYPES OF EVENT BINDING

    #? For buttons only using command in initialisation
    # Button to copy window dimensions
    copy_btn = ttk.Button(main, text='Press to copy label text', command= lambda: pyp.copy(label['text']))
    copy_btn.pack()

    #? Binding it to a func that gets performed
    # Input box to paste it in
    past_box = ttk.Entry(main)
    past_box.bind('<Control-V>', pyp.paste)
    past_box.pack()

    #> Windows bind event
    # main.bind('<Return>', log)



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
    def __init__(self, text, duration):
        self.text = text
        self.status = 'complete' #Can either be ongoing or complete
        self.duration = duration

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

task1 = Task('Eat all day', half_hour)
print(task1.duration)