class Phone:
    def __init__(self, id_, name, price, brand):
        self.id = id_
        self.name = name 
        self.price = price 
        self.brand = brand

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Price : {self.price}, Brand : {self.brand}")

class Laptop:
    def __init__(self, id_, name, price, brand, memory, processor):
        self.id = id_
        self.name = name 
        self.price = price 
        self.brand = brand
        self.memory = memory
        self.processor = processor

    def display(self):
            print(f"ID: {self.id}, Name: {self.name}, Price : {self.price}, Brand : {self.brand}, Memory :{self.memory}, processor: {self.processor}")

class Store:
    def __init__(self):
        self.phones = []
        self.laptop = []

    def add(self, product):
        if isinstance(product, Phone):
            self.phones.append(product)
        elif isinstance(product, Laptop):
            self.laptop.append(product)

    def remove(self, id_):
        self.phones = [phone for phone in self.phones if phone.id_ != id_]
        self.laptop = [laptop for laptop in self.laptop if laptop.id_ != id_]

    def display(self, type):        
        if type == 'phone':
            print("phones in the store")
            for phone in self.phones:
                phone.display()

        elif type == 'laptop':
            print("phones in the store")
            for laptop in self.laptop:
                laptop.display()

