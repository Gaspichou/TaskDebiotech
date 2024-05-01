import time 

# IDs and periods of the tasks to be scheduled
tasksPeriods = [("A", 1), ("B", 5), ("C", 5), ("D", 10), ("E", 10)]

# definition of the tasks
# here they all use the same function, but individual functions could be defined for each
def task(taskId):
    time.sleep(0.8) # simulate the execution time of the task
    print(taskId, end = " ") # print the name of the task when the execution is over

# function that is executed in both threads
# infinite loop while checking for new tasks added to the queue
# if a task is found, it is executed and removed from the queue
def taskManager(taskQueue):
    while True:
        if not taskQueue.empty(): # checks if tasks are to be done 
            taskId = taskQueue.get() # retrieve ID of the first task in queue
            task(taskId) # execute the task 
            taskQueue.task_done() # mark task as done 
