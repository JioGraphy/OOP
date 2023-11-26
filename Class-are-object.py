from datetime import date

# Method in a class is nothing but an attribute which points to a function object
# Instance method vs class method
class Employee:

    # Class attribute
    minimum_wage = 1000

    @classmethod # use case for class method is factory functions
    def change_minimum_wage(cls, new_wage): # cls stands for class as the first parameter
        if new_wage > 3000:
            raise ValueError("Company is Bankrupt!")
        cls.minimum_wage = new_wage
    
    @classmethod # factory function or as alternative contructors
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage) # will create and return new instance

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary =+ self.salary * (percent/100)

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError('Minimum Wage is ${Employee.minimum_wage}')
        else:
            self._salary = salary

e = Employee("Ji-Soo", 38, 12000)
# Employee.__dict__["increase_salary"](e, 20)
# print(e.salary)

# # Employee instance has access to the class attributes
# print(e.minimum_wage)
# # Directly accessing attributes in the class
# print(Employee.minimum_wage)

# print(Employee.minimum_wage)
# Employee.change_minimum_wage(200)
# print(Employee.minimum_wage)

a = Employee.new_employee("Violet", date(1991, 8, 12))
print(a.name)
print(a.age)
print(a.salary)