from manager import *
def main():
    manager1 = Manager()
    while True:
        task_ = input("Add, Done, Display, Ditailes, Exit")
        if task_ == "Add":
            title,description,id_,statrt_time = input("title,description,id_,statrt_time").split(",")
            task1 = Manager.create_task(title,description,id_,statrt_time)
            manager1.add(task1)

        elif task_ == "Done":
            id_ = input("Enter id of task: ")
            d_t = input("Enter End time: ")
            manager1.done(d_t, id_)
            print("Done!")

        elif task_ == "Display":
            manager1.display()

        elif task_ == "Ditailes":
            manager1.summary()

        elif task_ == "Exit":
            break
        
        else:
            print("not found!")
       
main()
