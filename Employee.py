class Employee:

    # # For debugging purposes
    # # Built-in class constructor of the class
    # def __init__(self):

    #     # data attributes stored inside of the object's internal dictionary
    #     # access internal dictionary with __dict__ attribute
    #     self.__dict__['name'] = "Ji-Soo"
    #     self.__dict__['age'] = 38
    #     self.__dict__['position'] = "Developer"
    #     self.__dict__['salary'] = 1200
    

    # Initializing attributes of new object / Constructor
    def __init__(self, name, age, role, salary):
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary
    
    # Instance Function / functions inside of class is methods
    def increase_salary(self, percent):
        self.salary = self.salary * (percent/100)

    # self - instance itself, self was referring to new instance of the class
    # instance itself is always the first parameter
    # def info(self):
    #     print(f"{self.name} is {self.age} years old. Employee is {self.role} with the salary of ${self.salary}")


    # Point of the __str__ method is to return a readable string representation of the object
    # Usually for the end user or for debugging or development 
    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is {self.role} with the salary of ${self.salary}"


    # represent an object, return official string representation of the object
    def __repr__(self):
        return (
            # Implied line continuation inside of the parenthesis
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)},"
            f"{repr(self.role)}, {repr(self.salary)})"
            )


# Employee instances: Instantiation - process of using class to create a new object
# The instance which call the function will be implicitly provided to the function of the class as first argguments know as self
employee_1 = Employee("Ji-Soo", 38, "Developer", 1200)
employee_2 = Employee("Lauren", 44, "Tester", 1000)

# e = Employee()

# print(e.__dict__)

# print(e.name)
# print(e.__class__) # Check objects class

print(employee_1.name)
print(employee_2.name)

# Calling directly the methods thru the class
Employee.increase_salary(employee_2, 20)
# Employee.info(employee_2)

employee_2.increase_salary(20)
# employee_2.info()

print(str(employee_2))
print(employee_1)
print(eval(repr(employee_1)))