#Q2

#syntaxerror
#example1:
num1 = 12
num2 = 0
try:
    result = num1 / num2
except Exception as e:
    print(e)
else:
    print(result

#Q3

sum = 8
numbers = [10, 12, 13]
try:
    res = sum(numbers)
except Exception as e:
    print(e.__class__.__name__, ":", e)
else:
    print(res)

numbers = [2, 3, 10, 23]
try:
    numbers.remove(300)
except ValueError as e:
    print(e.__class__.__name__, ":", e)
try:
    print(numbers[8])
except IndexError as e:
     print(e.__class__.__name__, ":", e)

