#Q1

str1 = input("Enter a text :")
r = len(str1) % 2
n = len(str1) // 2

if r == 0 :    
    print(str1[:n])
else :
     print(str1[n:])

#Q2

str2 = """Python is a widely-used programming language known for its simplicity. Python supports various
programming paradigms. Python's code readability makes it a favorite among developers. Python is
ideal for rapidly prototyping applications."""
n = len(str2) % 2
m = len(str2) // 2
if n != 0:
    part1 = str2[:m + 1]
    c1_str2 = part1.count("Python")
    n_str2 = part1.replace("Python" , "Java")
    part2 = str2[m + 1:]
    c2_str2 = part2.count("Python")
    new_str2 = part2.replace("Python" , "C++")
    print(f"{c1_str2} tims python repeated at the first part")
    print(f"{c2_str2} tims python repeated at the second part")
    print(n_str2 + "" + new_str2)

#Q3

text = input("Enter a text :")
words = text.split(" ")
word = "".join(words)
print(word)

#Q4

str2 = input("Enter first text :")
str3 = input("Enter second text :")
if str3 in str2 :
    Text1 = str2.removeprefix(str3)
    if str3 in Text1 :
        Text1 = str2.removesuffix(str3)
    print(Text1)
else :
    Text2 = str3 + " " + str2 + " " + str3
    print(Text2)
     
#Q5

password = input("Enter your password: ")
if len(password) == 8:
    part1 = password[:4]
    part2 = password[4:9]
    if (part1.isalpha()):
            if (part2.isnumeric()):
                print("vaild")
    else:
        print("invaild")
else:
    print("invaild")





