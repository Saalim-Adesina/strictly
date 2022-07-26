import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Fixes blurry in windows os
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

str
tasks = {}
counter = 0

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        def window_config():
            self.iconbitmap('icons\logo.ico') # small icon
            self.title('strictly | A miminalist todo and timer')
            window_width = 900
            window_height = 600
            self.geometry(f'{window_width}x{window_height}+{500}+{30}')
            self.minsize(width=100, height=100)

        # Settinng the window settings
        window_config()
        
        #> Global Variables
        frame_pad = {'padx':35, 'pady':20}
        
        # Heading Frame
        header = ttk.LabelFrame(self)
        # Window padding
        header.grid(**frame_pad, sticky='NW')

        # Global Style settings 
        glob_font={'font':('Segoue UI', 35)}

        # Grid Settings
        header.columnconfigure(0, weight=1)
        header.columnconfigure(0, weight=2)
        header.columnconfigure(0, weight=2)

        # Event User
        event_input = tk.StringVar()        
        
        # Time User Input

        hrs_input = tk.StringVar(value=00)
        min_input = tk.StringVar(value=00)
        sec_input = tk.StringVar(value=00)
        
        
        # Heading Text
        ttk.Label(header, text='To-Do List', **glob_font).grid(row=0,column=0,columnspan=2, sticky='W')
        
        #? User Inputs
        #> --- TIME GLOBAL --- 
        small_pad = {'padx':10, 'pady':10}
        med_pad = {'padx':15, 'pady':10}
        long_pad = {'padx':20, 'pady':10}
        size = {'width':3}
        
        #> --- Time input widgets ---
        taskframe = ttk.LabelFrame(self)
        taskframe.grid(row=1, column=0, sticky='EW', padx=30)
        taskframe.columnconfigure(index=0, weight=3)
        taskframe.columnconfigure(index=0, weight=2)
        taskframe.columnconfigure(index=0, weight=1)
        taskframe.columnconfigure(index=0, weight=1)
        taskframe.columnconfigure(index=0, weight=1)
        taskframe.columnconfigure(index=0, weight=1)

        def show_tasks(event_txt, hours, minutes, seconds):
            try:
                # Store the tasks
                tasks[event_txt] = [int(hours), int(minutes), int(seconds)]

                # Clears the entry
                task_entry.delete(0, tk.END)

                # Checkbox + item
                global counter
                ttk.Checkbutton(taskframe, text='{}'.format(event_txt)).grid(row=counter, rowspan=3,column=0, sticky='NW', padx=20, pady=3)

                # Timer
                timer = ttk.Label(taskframe, text='{:02d}:{:02d}:{:02d}'.format(int(hours), int(minutes), int(seconds)))
                timer.grid(row=counter, column=1, padx=15)
                
                # CRUD Buttons
                button_settings = {'padx':5, 'pady':3, 'sticky':'E'}
                ttk.Button(taskframe, text='Start', command= lambda: start(timer, int(hours), int(minutes), int(seconds)) ).grid(row=counter, column=2, **button_settings)
                ttk.Button(taskframe, text='Pause', command= lambda: pause(timer, int(hours), int(minutes), int(seconds)) ).grid(row=counter, column=3, **button_settings)
                ttk.Button(taskframe, text='Delete').grid(row=counter, column=4, **button_settings)
                ttk.Button(taskframe, text='Change Time').grid(row=counter, column=5, **button_settings)
                counter += 1

            except ValueError as error:
                messagebox.showwarning(message= f'{error}', title='Value Error')
            
        def start(timer, hrs, min, sec):
            temp = int(hrs)*3600 + int(min)*60 + int(sec)
            print(temp)
            while temp >-1:
                # divmod(firstvalue = temp//60, secondvalue = temp%60)
                mins,secs = divmod(temp,60)
        
                # Converting the input entered in mins or secs to hours,
                # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
                # 50min: 0sec)
                hours=0
                if mins >60:
                    # divmod(firstvalue = temp//60, secondvalue
                    # = temp%60)
                    hours, mins = divmod(mins, 60)
                
                # using format () method to store the value up to
                # two decimal places
                timer['text'] = '{:02d}:{:02d}:{:02d}'.format(int(hours), int(mins), int(secs)) 
        
                # updating the GUI window after decrementing the
                # temp value every time
                taskframe.update()
                time.sleep(1)
        
                # when temp value = 0; then a messagebox pop's up
                # with a message:"Time's up"
                if (temp == 0):
                    messagebox.showinfo("Time Countdown", "Time's up ")
                    break
                
                # after every one sec the value of temp will be decremented
                # by one
                temp -= 1

        def pause(timer, hrs, min, sec):
            temp = int(hrs)*3600 + int(min)*60 + int(sec)
            if temp > 0:
                timer['text'] = '{:02d}:{:02d}:{:02d}'.format(int(hrs), int(min), int(sec))
                taskframe.update()
    

        # Add Event Button
        ttk.Button(
            header, 
            text='Add Event',
            command= lambda: show_tasks(event_input.get(),hrs_input.get(),min_input.get(),sec_input.get())
        ).grid(row=1, column=0, )
        
        # Add Event Label
        task_entry = ttk.Entry(header, textvariable=event_input, width=30)
        task_entry.grid(row=1, column=1, **long_pad)

        # Create a time input sub-frame
        time_input_frame = ttk.Frame(header)
        time_input_frame.grid(row=1, column=2, sticky='E')
        
        ttk.Label(time_input_frame, text='Hrs').grid(row=0, column=0)
        hrs_entry = ttk.Entry(time_input_frame, text='Hrs', textvariable=hrs_input, **size)
        hrs_entry.grid(row=0, column=1, **small_pad)

        ttk.Label(time_input_frame, text='Min').grid(row=0, column=2)
        min_entry = ttk.Entry(time_input_frame, text='Min', textvariable=min_input, **size)
        min_entry.grid(row=0, column=3, **small_pad)

        ttk.Label(time_input_frame, text='Sec').grid(row=0, column=4)
        sec_entry = ttk.Entry(time_input_frame, text='Sec', textvariable=sec_input, **size)
        sec_entry.grid(row=0, column=5, **small_pad)        

class HeaderFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # set up grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(0, weight=2)

        # font size
        glob_font={'font':('Segoue UI', 35)}
        
        # Time User Input
        hours = tk.IntVar()
        minutes = tk.IntVar()
        seconds = tk.IntVar()

        # Event User
        event = tk.StringVar()

        # Header
        ttk.Label(self, text='To-Do List', **glob_font).grid(row=0,column=0,columnspan=2, sticky='W')
        
        def add_to_lists(event_text, hrs_text, minutes_text, seconds_text):
            global counter


            # Adds tasks into list
            ttk.Checkbutton(self, text='{} {:02d}:{:02d}:{:02d}'.format(event_text, hrs_text, minutes_text, seconds_text)).grid(row=counter, column=0, sticky='W', padx=20)

            # Buttons
            ttk.Button(self, text='Start').grid(row=counter, column=1, sticky='W')
            ttk.Button(self, text='Pause').grid(row=counter, column=2, sticky='W')
            ttk.Button(self, text='Delete').grid(row=counter, column=3, sticky='W')
            ttk.Button(self, text='Change Time').grid(row=counter, column=4, sticky='W')
            counter += 1

            tasks[event_text] = [hrs_text, minutes_text, seconds_text]
            task_entry.delete(0, tk.END)
            print(tasks)

        ttk.Button(self,text='Add Event',width=13, command= lambda: add_to_lists(
            event.get(), 
            hours.get(),
            minutes.get(), 
            seconds.get()
            )).grid(row=1, column=0, sticky='W')
        
        
        # Event User Input
  
        task_entry = ttk.Entry(self, textvariable=event, width=30)
        task_entry.grid(row=1, column=1)


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
    ...

if __name__ == "__main__":
    app = App()
    app.mainloop()