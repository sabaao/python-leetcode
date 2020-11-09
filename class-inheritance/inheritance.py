class Transportation:
    def __init__(self):
        self.color = "white"
    def drive(self):
        print("Transportation deive methos is called")

class Car(Transportation):
    def accelerate(self):
        print("accelerate is method called.")

class Airplane(Transportation):
    def fly(self):
        print("fly method is called")
    def drive(self):
        print("Airplane deive methos is called")
car = Car()
print(car.color) # white
car.drive() # Transportation deive methos is called

airplane = Airplane()
print(airplane.color) # white
print(airplane.drive()) # Airplane deive methos is called