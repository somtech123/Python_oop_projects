from EmployeesManager import *

class FrontendManager:
    def __init__(self):
        self.__EmployeesManager = EmployeesManager()

    def _print_menu(self):
        print('\nprogram options: ')

        messages = [
            '1) Add a new employee ',
            '2) List all employees ',
            '3) Delete by age range ',
            '4) Update salary given ',
            '5) End the program '
        ]

        print('\n'.join(messages))
        msg = f'Enter your choice (from 1 to {len(messages)})'

        return input_is_valid(msg, 1, len(messages))
    

    def run(self):
        while True:
            choice = self._print_menu()

            if choice == 1:
                self.__EmployeesManager.add_new_employee()

            elif choice == 2:
                self.__EmployeesManager.list_all_emploee()

            elif choice == 3:
                age_from = int(input("Enter age from: \n"))
                age_to = int(input("Enter age to: \n"))

                self.__EmployeesManager.delete_employee_with_age(age_from, age_to)

            elif choice == 4:
                 name = input("Enter employee name: \n")
                 salary = input("Enter employee salary \n")

                 self.__EmployeesManager.update_salary_by_name(name, salary)

            else: break
