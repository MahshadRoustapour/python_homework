#Q1

count_s = int(input("Enter number of students: "))
id_student = ()
name_student = ()
score_student = ()
for i in range(count_s):
    id = int(input("Enter id of student :"))
    if id not in id_student:
       name = input("Enter name of student :")
       score = int(input("Enter score of student :"))
       id_student = list(id_student)
       id_student.append(id)
       id_student = tuple(id_student)
       name_student = list(name_student)
       name_student.append(name)
       name_student = tuple(name_student)
       score_student = list(score_student)
       score_student.append(score)
       score_student = tuple(score_student)
    else:
        print("already exist")
result = list(zip(id_student, name_student, score_student))
print(result)
search_name = input("Enter a name you want to search: ")
for i in result:
    for j in i:
        if j == search_name:
            print(i)

#Q2

list1 = [1, 2, 3, 4, 5, 6, 6, 7]
list2 = [5, 6, 7, 8, 9]
final_list = list1 + list2
final_list = set(final_list)
print(final_list)

#Q3

set_per = set()
list = ["ex11.py", "lord of the rings.pdf", 90, 78, "post.py", 45, "book.pdf", "mahshad.jpg"]
for i in list:
    if isinstance(i, str):
        per = i.split(".")[-1]
        set_per.add(per)
print(set_per)

        
