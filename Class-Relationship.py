# # object is super class of all classes
# class Employee(object):
#     pass


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

    # override method
    def __init__(self, name, age, salary, framework):
        # calling the init method of super class which is the Employee
        super().__init__(name, age, salary)
        # Extending instance attribute
        self.framework = framework

    # Method overriding
    # Redefining same method from the parent class inside of the child class
    def increase_salary(self, percent, bonus=0):
        # super is dynamic, using Method Resolution Order
        # DRY
        super().increase_salary(percent)
        # Employee.increase_salary(self, percent)
        self.salary += bonus


employee_1 = Tester("Julia", 30, 1000)
employee_2 = Developer("Laurance", 28, 5000, "Flask")


employee_2.increase_salary(20, 30)
print(employee_2.salary)
print(employee_2.name)
print(employee_2.framework)

# instance attributes values store in internal dictionary
print(employee_2.__dict__)




# e = Employee
# print(repr(e))

# class heirarcy: object class (Super Class) -> Employee class (Parent Class) -> Tester and Developer (Child Class)
# Polymorphism
# print(isinstance(employee_1, Tester))
# print(isinstance(employee_1, Employee))

# print(issubclass(Developer, Employee))
# print(issubclass(Employee, object))
# print(issubclass(Developer, object))

# try:
#     # something that raises the FloatingPointError or the ZeroDivisionError
#     raise FloatingPointError('Watch out for floating point error! ')
# except ArithmeticError as e:
#     print(e)
