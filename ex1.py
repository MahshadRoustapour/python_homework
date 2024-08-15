#Q1

num1 = 12.45
num1 = int(num1)
print(num1)

num2 = "12.45"
num2 = int(float(num2))
print(num2)

flag1 = True
flag1 = int(flag1)
print(flag1)

#impossible : has an error because there is a character on it 
#code = "a123"
#code = int(code)
#print(code)

num3 = "0123"
num3 = int(num3)
print(num3)

num4 = 10
num4 = float(num4)
print(num4)

#it is already a float number
num5 = 4.
print(type(num5))

num6 = "4.7"
num6 = float(num6)
print(num6)

num7 = "51"
num7 = float(num7)
print(num7)

#impossible
#name = "python"
#name = float(name)
#print(name)

#it is already bool
flag3 = False
print(type(flag3))

flag4 = "False"
flag4 = bool(flag4)
print(flag4)

name1 = ""
name1 = bool(name1)
print(name1)

name2 = " "
name2 = bool(name2)
print(name2)

num8 = 0 
num8 = bool(num8)
print(num8)

flag = False
flag = str(flag)
print(type(flag))

num = 0.000
num = str(num)
print(type(num))

#Q2

x = "300" #assign 300 as a string value to variable x
y = int(x) #convert x into an int variable and assign to variable y(type casting)
z = y + 200 #add 200 to variable y and assign to variable z
a = float(z) #convert 500 as an int variable into a float variable(type casting)
#b = a + x #this line has error because x is a string but a is a float
#c = int(b) + 100 #this line does not execute because in line 79 there is an error

#fixed bug
b = a + float(x)
c = int(b) + 100
print(c)


x = "250" #assign 250 as a string value to variable x
y = int(x) #convert x into an int variable and assign to variable y(type casting)
z = y // 3 #exact divide by 3 and assign it into z variable
a = str(z) #convert variable z into a string variable and assign to variable a(type casting)
b = a + x #add a with x as two string and assign it to variable b
c = int(b) // 2 #convert b into an int number and exact divide by 2 and assign to c(type casting)  
print(c)



#Q3

text = str(input("Enter a text: "))
print(text == "yes" or text == "no")

#Q4

Text = input("Enter a text :")
print(Text != "")

#Q5

c = float(input("Enter the temperature :"))
f = c * 1.8 + 32.
print(f)

#Q6

num1, num2, num3 = 17, 1.8, 28 #this line assign values to variables
#num4, num5 = 45, 12, 19 this line has an error there is no variable for 19
#num6, num7, num8 = 200, 300 this line has error there is no value for variable num8
name, score, passed = "sara", 19, True #this line assign different types of value to variable
var1 = var2 = var3 = 500 #this line assign value 500 to 3 different variables

num1 = 20 #this line assign value 20 to variable num1
num2 = 30 #this line assign value 30 to variable num2
num1, num2 = num2, num1 #exchange vlues
print(num1, num2) 


