class Developer():

    # instance attributes: iterables
    # Instructing the class to utilize slots to store attributes in a new instance
    # global scope
    # this are now static, slots tuple
    __slots__ = ("name", "age", "salary", "framework")

    def __init__(self, name, age, salary, framework):
        self.name = name
        self.age = age
        self.salary = salary
        self.framework = framework

employee_1 = Developer("Ji-Soo", 20, 1200, "Django")

print(employee_1.__slots__)
        

