import time
import tkinter as tk
from tkinter import ttk

# Fixes blurry in windows os
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

tasks = {}

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # main window configuration setting
        def window_config():
            self.iconbitmap('icons\logo.ico') # small icon
            self.title('strictly | A miminalist todo and timer')
            window_width = 850
            window_height = 400
            self.geometry(f'{window_width}x{window_height}+{1050}+{50}')
            self.minsize(width=500, height=200)
        window_config()

        self.rowconfigure(0, weight=3)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(0, weight=1)

        self.__create_widgets()


    def __create_widgets(self):
        headerframe = HeaderFrame(self)
        eventsFrame = EventsFrame(self)
        headerframe.grid(row=0, column=0, sticky='NW')
        eventsFrame.grid(row=1, column=0, sticky='NW')
             
class HeaderFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # set up grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(0, weight=2)
        self.__create_header_widgets()

    def __create_header_widgets(self):
        
        # Global Settings
        options={'padx':20, 'pady':10}
        glob_font={'font':('Segoue UI', 35)}
        
        # Time User Input
        hours = tk.IntVar()
        minutes = tk.IntVar()
        seconds = tk.IntVar()

        event = tk.StringVar()


        ttk.Label(self, text='To-Do List', **glob_font).grid(row=0,column=0,columnspan=2, **options, sticky='W')
        
        def add_to_lists(event_text, hrs_text, minutes_text, seconds_text):
            tasks[event_text] = [hrs_text, minutes_text, seconds_text]
            task_entry.delete(0, tk.END)
            print(tasks)

        ttk.Button(self,text='Add Event',width=13, command= lambda: add_to_lists(event.get(), hours.get(),minutes.get(), seconds.get())).grid(row=1, column=0, sticky='W', **options)
        
        
        # Event User Input
  
        task_entry = ttk.Entry(self, textvariable=event, width=30)
        task_entry.grid(row=1, column=1, **options)



        # Create time input frame
        time_input_frame = ttk.Frame(self)
        time_input_frame.grid(row=1, column=3, sticky='E')

        # global variables
        x_padding = {'padx':10}
        size = {'width':3}

        # time input widgets
        ttk.Label(time_input_frame, text='Hrs').grid(row=0, column=0)
        hrs_entry = ttk.Entry(time_input_frame, text='Hrs', textvariable=hours, **size)
        hrs_entry.grid(row=0, column=1, **x_padding)


        ttk.Label(time_input_frame, text='Min').grid(row=0, column=2)
        min_entry = ttk.Entry(time_input_frame, text='Min', textvariable=minutes, **size)
        min_entry.grid(row=0, column=3, **x_padding)

        ttk.Label(time_input_frame, text='Sec').grid(row=0, column=4)
        sec_entry = ttk.Entry(time_input_frame, text='Sec', textvariable=seconds, **size)
        sec_entry.grid(row=0, column=5, **x_padding)

        # Configuring Style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 10))
        self.style.configure('TButton', font=('Helvetica', 10))

class EventsFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        inc = 0     
        for task, dur in tasks.items():
            self.rowconfigure(0, weight=1)
            ttk.Label(self, text='{} {:02d}:{:02d}:{:02d}'.format(task, dur[0], dur[1], dur[2])).pack()
            

if __name__ == "__main__":
    app = App()
    app.mainloop()