import time, re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

# Fixes blurry in windows os
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

str
tasks = {}
counter = 0
Pause = False
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        def window_config():
            self.iconbitmap('D:\Saalim\coding\Personal Projects\strictly\strictly\images\logo.ico') # small icon
            self.title('strictly | A miminalist todo and timer')
            window_width = 1005
            window_height = 600
            self.geometry(f'{window_width}x{window_height}+{500}+{30}')
            self.minsize(width=100, height=100)
            self.resizable(False, False)

        # Settinng the window settings
        window_config()

        #> Global Variables
        
        frame_padding = {'padding':(35, 20)}
        # Heading Frame
        header = ttk.Frame(self, **frame_padding) #left,top,right,bottom

        # Window padding
        header.grid(row=0, column=0, sticky='NW')

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
        min_input = tk.StringVar(value=15)
        sec_input = tk.StringVar(value=00)
        
        
        # Heading Text
        ttk.Label(header, text='To-Do List', **glob_font).grid(row=0,column=0,columnspan=2, sticky='W')

        # Opens the image using absolute path
        img = Image.open("D:\Saalim\coding\Personal Projects\strictly\strictly\images\copyright.png")
        img_widht, img_height = img.size
        # img = img.resize((img_widht//6, img_height//6))
        img = img.resize((img_widht//6, img_height//6))
        tkimg = ImageTk.PhotoImage(img)
        
        image_label = ttk.Label(header, image=tkimg)
        image_label.image = tkimg
        
        image_label.grid(row=0, column=2)

        #? User Inputs
        #> --- TIME GLOBAL --- 
        small_pad = {'padx':10, 'pady':10}
        med_pad = {'padx':15, 'pady':10}
        long_pad = {'padx':20, 'pady':10}
        size = {'width':3}
        
        #> --- Time input widgets ---
        taskframe = ttk.Frame(self)
        taskframe.grid(row=1, column=0, sticky='EW', padx=30)
        taskframe.columnconfigure(index=0, weight=4)
        taskframe.columnconfigure(index=0, weight=1)
        taskframe.columnconfigure(index=0, weight=1)
        taskframe.columnconfigure(index=0, weight=1)
        taskframe.columnconfigure(index=0, weight=1)
        taskframe.columnconfigure(index=0, weight=1)
        

        #! CONTROLS ALL THE BUTTONS
        def add_event(event_txt, hours, minutes, seconds):
            try:
                # Move cursor to entry box
                task_entry.focus()
                if event_txt != '':
                    event_txt = event_txt + ' ' * 100
                    event_txt = event_txt[0:20]
                    tasks[event_txt] = [int(hours), int(minutes), int(seconds)]

                    # Checkbox + item
                    global counter
                    
                    # Clears the entry
                    task_entry.delete(0, tk.END)
                    
                    # Task Check Box
                    task_lbl = ttk.Checkbutton(taskframe, text='{}'.format(event_txt), variable='')
                    task_lbl.grid(row=counter, rowspan=3,column=0, sticky='NW', padx=20, pady=3)

                    # Timer
                    timer = ttk.Label(taskframe, text='{:02d}:{:02d}:{:02d}'.format(int(hours), int(minutes), int(seconds)), font=('Helvetica 12 bold'), background='white', borderwidth=1, relief='solid', style='timer.TLabel', padding=(10, 0))
                    timer.grid(sticky='NW', row=counter, column=1, padx=15, ipadx=2, ipady=2, pady=2)
                    
                    # CRUD Buttons
                    button_settings = {'padx':5, 'pady':3, 'sticky':'NW'}

                    start_btn = ttk.Button(taskframe, text='Start', command= lambda: start(timer, task_lbl))

                    start_btn.grid(row=counter, column=2, **button_settings)

                    pause_btn = ttk.Button(taskframe, text='Pause', command= lambda: pause(timer))
                    pause_btn.grid(row=counter, column=3, **button_settings)

                    delete_btn = ttk.Button(taskframe, text='Delete', command= lambda: delete(task_lbl, timer, start_btn, pause_btn, delete_btn, time_btn))
                    delete_btn.grid(row=counter, column=4, **button_settings)

                    time_btn = ttk.Button(taskframe, text='Change Time', command= lambda: changetime(event_txt, timer) )
                    time_btn.grid(row=counter, column=5, **button_settings)
                    counter += 1
                else:
                    messagebox.showwarning('Blank Event', 'No event inputted in Event Field')
            except ValueError as error:
                messagebox.showwarning(message= f'{error}', title='Value Error')
            
        def start(timer, checkbutton):

            # sets pause back to False 
            global Pause
            Pause = False

            # selects the hrs, minutes and seconds from current time
            pattern = re.compile(r'(\d\d):(\d\d):(\d\d)')
            vals = pattern.findall(timer['text'])
            hrs = vals[0][0]
            mins = vals[0][1]
            secs = vals[0][2]

            temp = int(hrs)*3600 + int(mins)*60 + int(secs)

            while temp >-1 and Pause == False:

                # Sets label color as gray
                timer['foreground'] = 'green'

                mins,secs = divmod(temp,60)
                hours=0
                if mins >60:
                    hours, mins = divmod(mins, 60)
                
                timer['text'] = '{:02d}:{:02d}:{:02d}'.format(int(hours), int(mins), int(secs)) 
        
                # updating the GUI window after decrementing 
                timer.update()
                time.sleep(1)
        
                # Shows message when times up
                if (temp == 0):
                    
                    # Changes color to red
                    timer['foreground'] = 'red'
                    
                    # windows showing times up 
                    messagebox.showinfo("Time Countdown", "Time's up ")
                    break
                
                #? Temp value decrements
                temp -= 1
                
        def pause(timer):

            # sets pause back to True stopping the start() while loop
            global Pause
            Pause = True

            # selects the hrs, minutes and seconds from current time
            pattern = re.compile(r'(\d\d):(\d\d):(\d\d)')
            vals = pattern.findall(timer['text'])
            hrs = vals[0][0]
            mins = vals[0][1]
            secs = vals[0][2]
            timer['text'] = '{:02d}:{:02d}:{:02d}'.format(int(hrs), int(mins), int(secs))
            
            # Changes the color of the timer to yellow
            timer['foreground'] = '#d4c30b'
            taskframe.update()

        def delete(*buttons):
            for i in buttons:
                i.destroy()

        def changetime(event_text, timer):
            top = tk.Toplevel(self)

            #? Default window connfig
            top.iconbitmap('D:\Saalim\coding\Personal Projects\strictly\strictly\images\logo.ico') # small icon
            top.title('strictly | change time for task: {}'.format(event_text))
            window_width = 600
            window_height = 300
            screen_width = top.winfo_screenwidth()
            screen_height = top.winfo_screenheight()
            x = screen_width/2 - window_width/2
            y = screen_height/2 - window_height/2
            top.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')
            top.resizable(False, False)

            top.grid_columnconfigure(0, weight=1)

            #? Label Text
            header_frame = ttk.Frame(top)
            header_frame.grid(row=0, column=0)
            ttk.Label(header_frame, text='Current time:',).grid(row=0, column=0,)
            ttk.Label(header_frame, text='{}'.format(timer['text']), font='Montserrat 15 bold').grid(row=1, column=0)


            hrs_input = tk.StringVar(value=00)
            min_input = tk.StringVar(value=00)
            sec_input = tk.StringVar(value=00)


            time_frame = ttk.Frame(top, padding=(10, 0))
            time_frame.grid(row=1, column=0)
            ttk.Label(time_frame, text='Hrs').grid(row=2, column=1)
            ttk.Entry(time_frame, **size, textvariable=hrs_input).grid(row=2, column=2, **small_pad)

            ttk.Label(time_frame, text='Min').grid(row=2, column=3)
            ttk.Entry(time_frame, **size, textvariable=min_input).grid(row=2, column=4, **small_pad)

            ttk.Label(time_frame, text='Sec').grid(row=2, column=5)
            ttk.Entry(time_frame, **size, textvariable=sec_input).grid(row=2, column=6, **small_pad)

            button_frame = ttk.Frame(top, padding=5)
            button_frame.grid(row=2, column=0)
            ttk.Button(button_frame, text='Change Time', command= lambda: save_time(hrs_input, min_input, sec_input)).grid(row=3, column=0)
            
            def save_time(hrs, min, sec):

                hrs_val = hrs.get()
                min_val = min.get()
                sec_val = sec.get()

                try:
                    timer['text'] = '{:02d}:{:02d}:{:02d}'.format(int(hrs_val), int(min_val), int(sec_val))
                    messagebox.showinfo('Success', 'Time changed successfuly')
                    top.destroy()
                    taskframe.update()
                except:
                    messagebox.showwarning('Input Value', 'Please enter numbers')       

        # Add Event Button
        event_btn = ttk.Button(
            header, 
            text='Add Event',
            command= lambda: add_event(event_input.get(),hrs_input.get(),min_input.get(),sec_input.get()), style='Event.TButton'
        )
        event_btn.grid(row=1, column=0, )


        # Add Event Label
        task_entry = ttk.Entry(header, textvariable=event_input, width=30)
        task_entry.grid(row=1, column=1, **long_pad)
        task_entry.focus()
        
        # # Creating a scrollbar
        # scroll = ttk.Scrollbar(self, orient='vertical')
        # scroll.grid(sticky='NS')

        # Binding the window enter key to button
        self.bind('<Return>', lambda event: add_event(event_input.get(),hrs_input.get(),min_input.get(),sec_input.get()))
        
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


        # Styles
        btn = ttk.Style()
        btn.configure('TButton', font='Montserrat 8')
        btn.configure('Event.TButton', font='Montserrat 10', )
        btn.configure('TLabel', font='Montserrat 10')

if __name__ == "__main__":
    app = App()
    app.mainloop()