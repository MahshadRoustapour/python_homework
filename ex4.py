 #Q1

str4 = input("Enter a text: ")
c1 = 0
c2 = 0
for i in str4:
    if (i.isalpha()):
        c1 = c1 + 1
    if (i.isnumeric()):
        c2 = c2 + 1
   
print(f"number of alphabet character ----> {c1} number of numeric character ----> {c2}")

#Q2

for i in range(5):
    str5 = input("Enter a Text: ")
    if len(str5) > 6:
        print(str5)

#Q3

name1 = input("Enter the name of student")
score1 = float(input(f"Enter score of {name1}"))
if score1 > 20 :
    print("out of range")
elif score1 > 17:
    level = "A+"
elif score1 > 15:
    level= "A"
elif score1 > 10:
    level = "B"
else:
    level = "C"
print(f"name : {name1} ----> score : {score1} ----> level : {level}")
sum = score1
max = score1
max_n = name1
min = score1
min_n = name1
for i in range(9):
    name = input("Enter the name of student")
    score = float(input(f"Enter score of {name}"))
    sum += score
    if score > 20 :
        print("out of range")
    elif score >= 17:
        level = "A+"
    elif score >= 15:
        level= "A"
    elif score >= 10:
        level = "B"
    else:
        level = "C"
    if score > max:
        max = score
        max_n = name
    elif score < min:
        min = score
        min_n = name
    print(f"name : {name} ----> score : {score} ----> level : {level}")
print(f"maximum ----> name : {max_n} score : {max}")
print(f"minimum ----> name : {min_n} score : {min}")
print(f"average ----> {sum / 10}")

#Q4

sum = 0
for i in range(1, 11):
    r = i % 2
    if r == 0:
        new_i = i
        i = i + 5
        print(f"{new_i} + 5 = {i}")
        sum = i + sum
    else:
        new_i = i
        i = i * 5
        print(f"{new_i} * 5 = {i}")
        sum = i + sum
print(f"sum of obtained numbers = {sum}")




