class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def total_salary(self):
        return float(self.base_salary)

class Manager(Employee):
    def __init__(self, name, base_salary, bonus_percent):
        super().__init__(name, base_salary)
        self.bonus_percent = bonus_percent

    def total_salary(self):
        return self.base_salary * (1 + self.bonus_percent / 100)

class Developer(Employee):
    def __init__(self, name, base_salary, completed_projects):
        super().__init__(name, base_salary)
        self.completed_projects = completed_projects

    def total_salary(self):
        return self.base_salary + (self.completed_projects * 500)

class Intern(Employee):
    def total_salary(self):
        return float(self.base_salary)

def main():
    data = input().split()
    if not data:
        return

    emp_type = data[0]
    name = data[1]
    base_salary = int(data[2])

    if emp_type == "Manager":
        bonus_percent = int(data[3])
        employee = Manager(name, base_salary, bonus_percent)
    elif emp_type == "Developer":
        completed_projects = int(data[3])
        employee = Developer(name, base_salary, completed_projects)
    elif emp_type == "Intern":
        employee = Intern(name, base_salary)
    
    print(f"Name: {employee.name}, Total: {employee.total_salary():.2f}")

if __name__ == "__main__":
    main()