from utility import *
from Employee import *
import uuid

class EmployeesManager:
    def __init__(self):
        self.__employee = []

    
    def add_new_employee(self):
        print('Enter Employee Detail')
        name = input('Enter your name: ')
        age = input_is_valid('Enter Employee age: ')
        salary = input_is_valid('Enter Employee salary')

        id = uuid.uuid4()

        self.__employee.append(Employee(id, name, age, salary))


    def list_all_emploee(self):
        print('List all company Employees \n')

        if len(self.__employee) == 0 :
          print('\n Employee list is empty')
          return
        else: 
            for emp in self.__employee:
                print(emp)

    
    def delete_employee_with_age(self, start_age, end_age):

        for emp in self.__employee:
            if start_age <= emp.age <= end_age:
                print(f'\tDeleting Employee {emp.age}')
                self.__employee.remove(emp)

    
    def find_employee_by_name(self, name):
        for emp in self.__employee:
            if emp.name == name:
                return emp
        return None
    

    def update_salary_by_name(self,name, salary):
        emp = self.find_employee_by_name(name)
        if emp is None: print('Error: No Employee found')
        else: emp.salary += int(salary)






    