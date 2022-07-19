import time

#TODO
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