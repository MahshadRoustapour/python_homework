#Q1

def scores():
    score=float(input("score"))
    if 0 < score < 20:
        return score
    else:
        return scores()
    
scores()

#Q2

def multiply(x, y):
    if abs(x - y) < 1:
        return 1
    elif x > y:
        return (y + 1) * multiply(x, y + 1)
    else:
        return (x + 1) * multiply(x + 1, y)
x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
multiply(x, y)

