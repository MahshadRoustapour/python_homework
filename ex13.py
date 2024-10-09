#Q1

class Rectangle:
    def __init__(self,  length, width):
        self.length = length
        self.width = width 
    
    def area(self):
        area = self.length * self.width
        print(area)

    def perimeter(self):
        p = 2 * (self.length + self.width)
        print(p)
    
    def show(self):
        print(f"lenght---> {self.length}, width---> {self.width}")
    
r1 = Rectangle(3, 4)
r2 = Rectangle(4, 5)
r1.show()
r2.show()
r1.area()
r1.perimeter()
r2.area()
r2.perimeter()

#Q2

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        result = self.x + self.y
        print(result)

    def subtract(self):
        if self.x > self.y:
            result = self.x - self.y
        else:
            result = self.y - self.x
        print(result)
        
    def multiply(self):
        result = self.x * self.y
        print(result)
    
    def divide(self):
        if self.x > self.y:
            result = self.x / self.y
        else:
            result = self.y / self.x
        print(result)
    
c1 = Calculator(243, 32)
c1.add()
c1.subtract()
c1.multiply()
c1.divide()

#Q3

class Counter:
    def __init__(self, count = 0):
        self.count = count

    def increment(self):
        self.count += 1

    def decrement(self):
        if self.count > 0:
            self.count -= 1
        else:
            print("can not dcrement")

    def reset(self):
        self.count = 0
    
    def get_count(self):
        print(f"count---> {self.count}")

c1 = Counter()
c1.increment()
c1.get_count()