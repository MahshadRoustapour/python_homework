from manager import *
def main():
    manager1 = Manager()
    while True:
        task_ = input("Add, Done, Display, Details, Exit")
        if task_ == "Add":
            title = input("title: ")
            description = input("description :")
            id_ = input("id :")
            statrt_time = input("statrt time: ")
            task1 = Manager.create_task(title,description,id_,statrt_time)
            manager1.add(task1)

        elif task_ == "Done":
            id_ = input("Enter id of task: ")
            d_t = input("Enter End time: ")
            manager1.done(d_t, id_)
            print("Done!")

        elif task_ == "Display":
            manager1.display()

        elif task_ == "Details":
            manager1.summary()

        elif task_ == "Exit":
            break
        
        else:
            print("not found!")
       
main()
