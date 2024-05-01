import schedule
import queue
from datetime import timedelta

from tasks import *

# class that enables to decide when the tasks are to be executed
# stores the IDs of the next tasks in a queue 
# these IDs are retrieved in the threads, where the tasks are then executed
class Scheduler:
    def __init__(self, initTime):
        self.taskQueue = queue.Queue()
        self.initTime = initTime
        self.counterInit = 0 # counter to init all the tasks sequencially
        print("Time (sec) -> Tasks") 
        self.setupScheduler()

    # initialization of the various schedulers of the class
    def setupScheduler(self): 
        # schedules the display of the time elapsed every second
        schedule.every(1).seconds.do(self.displayTime) 

        # enables to start the schedulers for each tasks with 1 second of delay between them
        schedule.every(1).seconds.until(timedelta(seconds=len(tasksPeriods)+1)).do(self.setupTask)
        # important because for tasks with equal periods (e.g. B and C), if schedulers set up at the same time 
        # at every period they will be put in the queue together, blocking the threads for their execution and preventing
        # lower frequency tasks (e.g. A) from running

    def setupTask(self):
        taskId, period = tasksPeriods[self.counterInit] # get ID and period of next task to be initialized
        self.counterInit+=1 # increment the counter 
        self.addTask(taskId) # put an iteration of the task in the queue
        schedule.every(period).seconds.do(self.addTask, taskId)  # schedule the addition of the ID of the task to the queue every period
    
    def displayTime(self):
        elapsedTime = int(time.time()-self.initTime) # time since the beginning of the execution in seconds

        # line break
        if elapsedTime > 1:
            print()
        
        print(str(elapsedTime)+" ->", end=" ") # display without line break, so that the ID of the executed tasks can be shown on the same line 

    # add ID of the task to be executed into the queue
    def addTask(self, taskId):
        self.taskQueue.put(taskId)
    
    # run all the jobs that are scheduled to run
    def run():
        schedule.run_pending()

    