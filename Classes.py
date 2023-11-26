
# List
# employee_1 = ["Ji Soo", 38, "Developer", 1200]
# employee_2 = ["Lauren", 44, 'Tester', 1400]

# employees = [employee_1, employee_2]

# Dictionaries
employee_1 = {
    "Name": "Ji Soo",
    "Age": 38,
    "Role": "Developer",
    "Salary": 1200
}

employee_2 = {
    "Name": "Lauren",
    "Age": 44,
    "Role": "Tester",
    "Salary": 1400
}


def init_employee(name, age, role, salary):
    return {

        "Name": name,
        "Age": age,
        "Role": role,
        "Salary": salary

    }


def increase_salary(employee, percent):
    employee['Salary'] += employee['Salary'] * (percent/100)


def employee_info(employee):
    print(f"{employee['Name']} is {employee['Age']} years old. Employee is {employee['Role']} with the salary of ${employee['Salary']}")


employees = [employee_1, employee_2]
increase_salary(employee_2, 20)

for e in employees:
    employee_info(e)
