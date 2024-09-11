import datetime
to_dos = {}

def Add(id):
    if id in to_dos:
       print("Already exist")
       return
    name = input("Enter name of to do: ")
    to_do = {
        "name" : name,
        "status" : False,
        "duration" : None
    }
    to_dos[id] = to_do
    print("To Do Added!")

def Display():
    for key, value in to_dos.items():
        print("*" * 10 + key + "*" * 10)
        for k, v in value.items():
            print(f"{k} : {v}")

def Remove(id):
    if id not in to_dos:
        print("Does not exist")
        return
    to_dos.pop(id)
    print("To Do Removed!")
    
def Edit(id):
    if id in to_dos:
        new_name = input("Enter new To Do: ")
        if new_name in to_dos[id]["name"]:
            print("Already exist")
        else:
            to_dos[id]["name"] = new_name
            print("To Do Edited!")
    else:
        print("not found")

def Search(name):
    for value in to_dos.values():
        if value["name"] == name:
            for k, v in value.items():
                print(f"{k} : {v}")
def Done(id):
    if id in to_dos:
        time = input("Enter time of To Do you have Done: ")
        to_dos[id]["duration"] = time
        to_dos[id]["status"] = "Done"
        print("Done!")
    else:
        print("not found!")
def Help():
    print("""Key Add will Add a new to do
                Key DIsplay will show you what do you have in your to do list and is it done or not
                Key Remove will Remove any to do you want
                Key Edit will Edit a name of to do you want
                Key Search will search any to do you want based on its name
                Key Done will change the statuse of any to do you want to Done and change its time
                Key Help will show you any information about any key
                Key Display details will show you informations about you tasks how many of them have done ...
                Key Exit will exit from this program""")
    
def Display_ditailes():
    completed = 0
    uncompleted = 0
    number_of_todo = len(to_dos)
    duration = []
    for k, v in to_dos.items():
        if v["status"] == "Done":
            completed = completed + 1
        else:
            uncompleted = uncompleted + 1
    print(number_of_todo)
    print(f"completed : {completed} uncompleted : {uncompleted}")
    for k, v in to_dos.items():
        if v["duration"] != False:
            duration.append(v["duration"])
    print(duration)
    mysum = datetime.timedelta()
    for i in duration:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        mysum += d
    print(str(mysum))

def main():
    while True:
        answer = int(input("""Menu ---->
                1 - Add
                2 - Display
                3 - Remove
                4 - Edit
                5 - Search
                6 - Done
                7 - Help
                8 - Display detailes
                9 - Exit
                    """))
        if answer == 1:
            id = input("Enter id to Add: ").strip()
            Add(id)            
        elif answer == 2:
            Display()
        elif answer == 3:
            id = input("Enter id to Remove: ").strip()
            Remove(id)
        elif answer == 4:
            id = input("Enter id to Edit: ").strip()
            Edit(id)
        elif answer == 5:
            name = input("Enter name of To Do to search: ")
            Search(name)
        elif answer == 6:
            id = input("Enter id of To Do you have Done: ")
            Done(id)
        elif answer == 7:
            Help()
        elif answer == 8:
            Display_ditailes()
        elif answer == 9:
            break
main()



        
