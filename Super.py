class Phone:
    def __init__(self, price, brand, camera):
        print('inside Parent classs constructor')
        self.price = price
        self.brand = brand
        self.camera = camera
        
class SmartPhone(Phone):
    def __init__(self, price, brand, camera, OS, RAM):
        super().__init__(price, brand, camera)
        self.OS = OS
        self.RAM = RAM
        print('inside smartphone constructor')
        
s = SmartPhone(20000, 'Samsung', 20, 'Android', 4)
print(s.OS)
print(s.brand)


        