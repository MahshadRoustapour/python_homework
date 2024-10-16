#Single inheritance

class Book:
    def __init__(self, name, author):
        self.name = name 
        self.author = author

    def __str__(self):
        return f"Book name: {self.name}, author: {self.author}"
    
class Novel(Book):
    def __init__(self, name, author, country):
        super().__init__(name, author)
        self.country = country

    def __str__(self):
        return f"{super().__str__()}, country: {self.country}"
    
n1 = Novel("Jane Eyre", "Charlotte Brontë", "England")
print(n1)

#Hierarchical inheritance

class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"name: {self.name}, price: {self.price}"
    
class Benz(Car):
    def __init__(self, name, price, model):
        super().__init__(name, price)
        self.model = model

    def __str__(self):
        return f"{super().__str__()}, model: {self.model}"
    
    def discount(self):
        self.price = self.price * 0.8
    
class BMW(Car):
    def __init__(self, name, price, model):
        super().__init__(name, price)
        self.model = model

    def __str__(self):
        return f"{super().__str__()}, model: {self.model}"
    
    def discount(self):
        self.price = self.price * 0.85

c1 = Benz("Benz1", 3000, "2020")
c2 = BMW("BMW1", 4000, 2022)
print(c1)
c1.discount()
print(c1)

#Multilevel inheritance

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"name: {self.name}, price: {self.price}"

class Elproduct(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def __str__(self):
        return f"{super().__str__()}, brand: {self.brand}"
    
class Mobile(Elproduct):
    def __init__(self, name, price, brand, model, camera):
        super().__init__(name, price, brand)
        self.model = model
        self.camera = camera

    def __str__(self):
        return f"{super().__str__()}, model: {self.model}, camera: {self.camera}MGpx"
    
m1 = Mobile("m1", 3000, "samsung", "s24", 50)
print(m1)

#Multiple inheritance

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"name: {self.name}, price: {self.price}"

class Elproduct:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"brand: {self.brand}"
    
class Mobile(Elproduct, Product):
    def __init__(self, name, price, brand, model, camera):
        super().__init__(brand)
        Product.__init__(self, name, price)
        self.model = model
        self.camera = camera

    def __str__(self):
        return f"{super().__str__()}, model: {self.model}, camera: {self.camera}MGpx"

m2 = Mobile("m2", 3000, "samsung", "s23 fe", 50)
print(m2)