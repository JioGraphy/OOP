# Parent Class
class Employee:

    # Initializing attributes of new object / Constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # Instance Function / functions inside of class is methods
    def increase_salary(self, percent):
        self.salary =+ self.salary * (percent/100)


# Subclass
class Tester(Employee):
    
    def run_tester(self):
        print(f"Testing is started by {self.name}..")
        print("Test are done")


class Developer(Employee):

    # Method overriding
    # Redefining same method from the parent class inside of the child class
    def increase_salary(self, percent, bonus=0):
        self.salary += self.salary * (percent/100)
        self.salary += bonus


employee_1 = Tester("Julia", 30, 1000)
employee_2 = Developer("Laurance", 28, 5000)

employee_1.increase_salary(20)
employee_2.increase_salary(20, 30)
print(employee_1.salary)
print(employee_2.salary)





# employee_1.increase_salary(20)
# print(employee_1.age)
# print(employee_1.salary)
# employee_1.run_tester()
