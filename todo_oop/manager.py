from task import *

class Manager:
    def __init__(self):
        self.tasks = {}
    
    def create_task(self, title,  description, id_, statuse, statrt_time, end_time = None):
        new_task = Task(title, description, id_, statuse, statrt_time, end_time)
        return new_task

    def add(self, task):
        if task.id_ not in self.tasks:
            self.tasks[task.id_] = task 
            print("Added")
        else:
            print("already exist!")

    def done(self, d_t, id):
        if id in self.tasks:
            task = self.tasks[id]
            task.statuse = True
            task.end_time = d_t

    def display(self):
        for task in self.tasks.values():
            print(task)
    
    def summary(self):
        c = 0
        n_c = 0
        for i in self.tasks.values():
            if i.statuse == True:
                c += 1
            elif i.statuse == False:
                n_c += 1
        print(f"{c}---> completed, {n_c}---> not completed")

        






