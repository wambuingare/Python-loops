class Vehicle:
    color = "White"
    def __init__(self,name,max_speed,mileage,color,capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color
        self.capacity = capacity
        
    def greet(self): 
        return f"Hello Nancy,Congratulations for buying this {self.name}, colour {self.color},with an average speed of {self.max_speed}, at {self.mileage} with a capacity of {self.capacity} people"

    def calculate(self):
        return f"A {self.name}, with capacity of {self.capacity}"
         
            

