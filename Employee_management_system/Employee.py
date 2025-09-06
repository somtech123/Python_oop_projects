

class Employee:
    def __init__(self,id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary


    def __str__(self):
        return f'Employee {self.name} is {self.age} age and earn salary {self.salary} and id is {self.id}'
    
    def __repr__(self):
        return F'Emploee name = {self.name}, age = {self.age} salary = {self.salary} id = {self.id}'