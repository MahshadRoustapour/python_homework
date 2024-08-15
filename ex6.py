import datetime

names = []
statuses = []
durations = []

for i in range(200):
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
        name = input("Enter a to do to Add: ").lower
        if name not in names:
            names.append(name)
            statuses.append(False)
            durations.append(None)
            print("To Do Added")
        else:
            print("Already exist")
    elif answer == 2:
        for i , name in enumerate(names):
            print(i + 1, names[i], statuses[i], durations[i])
    elif answer == 3:
        name = input("Enter a to do to Remove: ").lower
        if name in names:
            i = names.index(name)
            names.pop(i)
            statuses.pop(i)
            durations.pop(i)
            print("To DO Removed")
        else:
            print("Does not exist")
    elif answer == 4:
        name = input("Enter a To Do to Edit: ").lower
        if name in names:
            new_name = input("Enter your new To Do: ").lower
            if new_name not in names:
                i = names.index(name)
                names[i] = new_name
                print("To Do Edited")
            else:
                print("Already exist")
        else:
            print("Does not exist") 
    elif answer == 5:
        name = input("Enter a To Do you are looking for: ").lower
        if name in names:
            i = names.index(name)
            print(f"{name} ----> statuse : {statuses[i]}, duration : {durations[i]}")
        else:
            print("Does not exist")
    elif answer == 6:
        name = input("Enter a To Do you have Done: ").lower
        time = input("Enter How long it took: ")
        if name in names:
                i = names.index(name)
                statuses[i] = "Done"
                durations[i] = time
                print("Done!")
        else:
                print("Does not exist")
    elif answer == 7:
        print("""Key Add will Add a new to do
                 Key DIsplay will show you what do you have in your to do list and is it done or not
                 Key Remove will Remove any to do you want
                 Key Edit will Edit a name of to do you want
                 Key Search will search any to do you want based on its name
                 Key Done will change the statuse of any to do you want to Done and change its time
                 Key Help will show you any information about any key
                 Key Display details will show you informations about you tasks how many of them have done ...
                 Key Exit will exit from this program""")
    elif answer == 8:
        number_of_todo = len(names)
        completed = statuses.count("Done")
        uncompleted = statuses.count(False)
        duration = []
        for i in durations:
            if i:
                duration.append(i)
        mysum = datetime.timedelta()
        for i in duration:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            mysum += d
        print(str(mysum))
        print(f"Number of all To Dos ----> {number_of_todo}")
        print(f"Number of Completed To Dos ----> {completed}")
        print(f"Number of Uncompleted To Dos ----> {uncompleted}")
        print(f"sum of time ----> {sum}")
    elif answer == 9:
        break
    else:
        print("command not found")





