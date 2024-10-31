class MyString(str):

    def lower(self):
        return super().lower() + "!"

    def count_words(self):
        return len(self.split())
    
    def replace(self, old, new):
        return super().upper().replace(old.upper(), new.upper())

    def  __add__(self, other):
        return MyString(str(self) + ' ' + str(other))
    
    def  __mul__(self, n):
        return MyString(('-'.join([str(self)] * n)))
    
if __name__ == "__main__":
    my_str = MyString("hello mahshad")
    print(my_str.count_words())
    print(my_str.__add__("how are you"))
    print(my_str.replace("mahshad", "mehdi"))
    print(my_str.__mul__(5))
    str2 = MyString("HELLO THERE")
    print(str2.lower())

    





