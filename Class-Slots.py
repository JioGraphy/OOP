
# Parent Class
class Employee:
    
    __slots__ = ("name", "age", "salary")
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

    # you should definitely use slots if you plan to create a lot of instances
    __slots__ = "Framework"

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




