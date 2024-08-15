#Q1
#First Way
letter = input("Enter a letter :")

if letter == "o" or letter == "i" or letter == "u" or letter == "e" or letter == "a":
    print("Vowel")
else:
    print("consonant")

#Scond Way(ridiculous one)
letter = input("Enter a letter :")

if letter == "o":
    print("Vowel")
elif letter == "i":
    print("Vowel")
elif letter == "u":
    print("Vowel")
elif letter == "e":
    print("Vowel")
elif letter == "a":
    print("Vowel")
else:
    print("consonant")
    
#Q2

number = int(input("Enter a number :"))

if number > 10 and number < 20:
    print("in Range")
else:
    print("out of Range")

#Q3

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

if num1 + num2 > 20 :
    print("Greater")
else:
    print("Not Greater")

#Q4

color1 = input("Enter a color :")
color2 = input("Enter a color :")
color3 = input("Enter a color :")

if color1 == color2 == color3 :
    print("All colors match")
elif color1 == color2 != color3 or color1 != color2 == color3 or color1 == color3 != color2 :
    print("Two colors match")
else :
    print("No colors match")

