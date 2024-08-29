#Q1

str_list = ["16", "12", "4"]
f_list = [20., 14.6, 18.75]
new_list = list(map(lambda a, b: int(a) + int(b), str_list, f_list))
print(new_list)

#Q2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter one of the operation(+, -, *, /, **): ")
if operation == "+":
    add = lambda a, b: a + b
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif operation == "*":
    multi = lambda a, b: a * b
    result = multi(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif operation == "-":
    minus = lambda a, b: a - b
    if num1 > num2:
        result = minus(num1, num2)
        print(f"{num1} - {num2} = {result}")
    else:
        result = minus(num2, num1)
        print(f"{num2} - {num1} = {result}")
elif operation == "/":
    if num2:
        division = lambda a, b: a / b
        result = division(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        num2 = 1
        print("your second number was 0 so we change it to 1")
        print(f"{num1} / 1 = {num1}")
elif operation == "**":
    power = lambda a, b: a ** b
    result = power(num1, num2)
    print(f"{num1} ** {num2} = {result}")
else:
    print("The operation you entered is invaild, try again:)")

#Q3

list1 = [672, -83, 73, -23, 12]
result1 = list(filter(lambda a: a < 0, list1))
print(result1)

count_ave = lambda a: sum(a)/len(a)
ave = count_ave(list1) 
result2 = list(filter(lambda a: a < ave, list1))
print(result2)

result3 = list(filter(lambda a: a % 2 == 0, list1))
print(result3)

#Q4

email_list = ["mahshadroustapour1@gmail.com", "python", "alainmesdach@yahoo.com", "pizza.", "pierecuri@gmail"]
real_emails = list(filter(lambda a: ("@") in a, email_list))
real_emails1 = list(filter(lambda b: (".") in b, real_emails))
print(real_emails1)

#Q5

list4 = [384, 6438, -43, 123, 234, 137, 839, -373, 128, 154, 849, -130]
result4 = any(map(lambda a: a > 100 and a < 200, list4))
print(result4)

#Q6

def count(s):
    words = sentence.split(" ")
    print(f"{len(words)} words in your sentence")

sentence = input("Enter a sentence: ")
count(sentence)



