numbers = []

for i in range(10):
    numbers.append(int(input(f"Enter {i+1}-Number: ")))

new_number = int(input("Enter a new number: "))
if new_number in numbers:
    c = numbers.count(new_number)
    for c in range(c):
        numbers.remove(new_number)
    print(numbers)
else:
    numbers.insert(0, new_number)
    numbers.insert(1, new_number)
    print(numbers)