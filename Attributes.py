class Employee:

    # Initializing attributes of new object / Constructor
    def __init__(self, name, age, role, salary):
        self.name = name
        self.age = age
        self.role = role
        self.salary = salary

    # Instance Function / functions inside of class is methods
    def increase_salary(self, percent):
        self.salary = self.salary * (percent/100)

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


try:

    minimum_salary = int(input("Input Salary: \n"))

    if minimum_salary < 1000:
        raise ValueError('Minimum Wage is less than 1000')
    else:
        employee_2.salary = minimum_salary

except ValueError as e:

    print(e, "Enter valid input")