class Car:
    
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def fullname(self):
        return f"my car is {self.brand} {self.model}."    

my_car = Car("BMW","M3")
print(my_car.brand,my_car.model)
print(my_car.fullname())