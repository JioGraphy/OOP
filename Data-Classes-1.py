from dataclasses import dataclass


# Get rids of boiler plate code __init__ 
# dataclass is a decorator 
# dataclass automatically create init and repr function based on the class attributes.
@dataclass
class Project:
    name: str
    payment: int
    client: str

    def notify_client(self):
        print(f"Notifying the client about the progress of the {self.name}..")
        

# class Project:

#     def __init__(self, name, payment, client):
#         self.name = name
#         self.payment = payment
#         self.client = client
        
#     def __repr__(self):
#         return f"Project(name={repr(self.name)}, payment={repr(self.payment)}, client={repr(self.client)})"
  


class Employee:

    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project

p = Project("Django App", 2000, "Cigna")
e = Employee("Ji Soo", 38, 1000, p)
print(e.project)