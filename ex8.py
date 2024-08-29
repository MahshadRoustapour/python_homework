#Q1
import datetime

names = []
statuses = []
durations = []

def Add(name):
    if name not in names:
        names.append(name)
        statuses.append(False)
        durations.append(None)
        print("To Do Added")
    else:
        print("Already exist")
def Display():
    for i , name in enumerate(names):
        print(i + 1, names[i], statuses[i], durations[i])
def Remove(name):
    if name in names:
        i = names.index(name)
        names.pop(i)
        statuses.pop(i)
        durations.pop(i)
        print("To DO Removed")
    else:
        print("Does not exist")
def Edit(name):
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
def Search(name):
    if name in names:
        i = names.index(name)
        print(f"{name} ----> statuse : {statuses[i]}, duration : {durations[i]}")
    else:
        print("Does not exist")
def Done(name, time):
    if name in names:
        i = names.index(name)
        statuses[i] = "Done"
        durations[i] = time
        print("Done!")
    else:
        print("Does not exist")
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
        name = input("Enter a to do to Add: ").lower
        Add(name)
    elif answer == 2:
        Display()
    elif answer == 3:
        name = input("Enter a to do to Remove: ").lower
        Remove(name)
    elif answer == 4:
        name = input("Enter a To Do to Edit: ").lower
        Edit(name)
    elif answer == 5:
        name = input("Enter a To Do you are looking for: ").lower
        Search(name)
    elif answer == 6:
        name = input("Enter a To Do you have Done: ").lower
        time = input("Enter How long it took: ")
        Done(name, time)
    elif answer == 7:
        Help()
    elif answer == 8:
        Display_ditailes()
    elif answer == 9:
        break
    else:
        print("command not found")

#Q2

id_product = ["name", "price", "color", "released"]
product = ["Apple iPhone", 999.99, "Gray", "July 2021"]
dic_product = dict(zip(id_product, product))

print(dic_product["name"])
print(dic_product["price"])
print(dic_product["color"])
print(dic_product["released"])

dic_product["color"] = "silver"
print(dic_product)

products = []
for i in range(4):
    product1 = {}
    product1["name"] = input("Enter name of product: ")
    product1["price"] = int(input("Enter price of product: "))
    product1["color"] = input("Enter color of product: ")
    product1["released"] = input("Enter date of released: ")
    products.append(product1)
print(products)

#Q3

student_grades = {
    "Mahshad Roustapour" : 17,
    "Jane Wers" : 18,
    "John wers" : 9
}

student_grades.update({"Peter Parker" : 15})
student_grades.update({"Merry Jane" : 7})
print(student_grades)

student_list = list(student_grades.items())
for k, v in student_list:
    if v < 10:
        del student_grades[k]
print(student_grades)

name = input("Enter a name: ")
if name in list(student_grades.keys()):
    new_grade = int(input("Enter new grade: "))
    student_grades[name] = new_grade
    print(student_grades)

sum = sum(list(student_grades.values()))
ave = sum/len(list(student_grades.values()))
print(ave)

#Q4

print("""This method returns the value for the given key, if it exists in the dictionary.
If the key does not exist, it returns a default value.
The default value is None if not specified, but if you
use direct key access you should expect key error 
""")

#Q5

employee_data = {}

for i in range(3):
    employee_id = {}
    employee_number = int(input("Enter the number of employee: "))
    employee_id["name"] = input("Enter name of employee: ")
    employee_id["age"] = int(input("Enter the age of employee: "))
    employee_id["salary"] = int(input("Enter the salary of employee: "))
    employee_data[employee_number] = employee_id
print(employee_data)

for k, v in employee_data.items():
    if employee_data[k]["age"] > 50:
        employee_data[k]["salary"] = employee_data[k]["salary"] + employee_data[k]["salary"] * 0.1 
print(employee_data)

d = []
for k, v in employee_data.items():
    if employee_data[k]["salary"] < 3000:
        d.append(k)
for i in d:
    del employee_data[i]
print(employee_data)

while 1:
    employee_n = int(input("Enter number of employee: "))
    for k in employee_data.keys():
        if employee_n == k:
            name_e = input("Enter new name of employee: ")
            employee_data[k]["name"] = name_e
            age_e = int(input("Enter new age of employee: "))
            employee_data[k]["age"] = age_e
            break
        else:
            continue
    break 
print(employee_data)

salary_dic = {}
for k in employee_data.keys():
    m_dic = {}
    m_dic["salary"] = employee_data[k]["salary"]
    salary_dic[k] = m_dic
print(salary_dic)


