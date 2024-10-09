class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price =price
    
    def __str__(self):
        return f"brand---> {self.brand}, model---> {self.model}, price---> {self.price}"
    
    def turn_on(self):
        return f"the device is powered on"
    
    def turn_off(self):
        return f"the device id powered off"
    
class Laptop(Device):
    def __init__(self, brand, model, price, Ram_size):
        super().__init__(brand, model, price)
        self.Ram_size = Ram_size

    def __str__(self):
        info = super().__str__()
        return f"{info}, Ramsize---> {self.Ram_size} GB"
    
    def open_laptop(self):
        return "the laptop is opened"
    
class Smartphone(Device):
    def __init__(self, brand, model, price, camera_resolution):
        super().__init__(brand, model, price)
        self.camera_resolution = camera_resolution

    def __str__(self):
        info = super().__str__()
        return f"{info}, camera resolution---> {self.camera_resolution} MP"

    def take_photo(self):
        return "a photo has been taken"
    

    

