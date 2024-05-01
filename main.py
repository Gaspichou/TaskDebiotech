import threading
import time

from tasks import taskManager
from scheduler import Scheduler


limitTime = 21 # sets the time limit for testing, can be removed and the condition for the while below converted to True for infinite loop
initTime = time.time() # execution start time

taskScheduler = Scheduler(initTime = initTime) # instance of the Scheduler class responsible for the timing of execution of the tasks

# creation of two threads for executing two tasks simultaneously in parallel 
threading.Thread(target=lambda: taskManager(taskScheduler.taskQueue), daemon=True).start()
threading.Thread(target=lambda: taskManager(taskScheduler.taskQueue), daemon=True).start()

# main loop 
while time.time()-initTime < limitTime:
        Scheduler.run()




    