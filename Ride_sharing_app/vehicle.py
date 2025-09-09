

class Vehicle:
    def __init__(self, model: str, plate: str):
        self.model = model
        self.plate = plate

    
    def __str__(self):
        return f'{self.model} ({self.plate})'
    
    def __repr__(self):
        return self.__str__()
    


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass

class Van(Vehicle):
    pass