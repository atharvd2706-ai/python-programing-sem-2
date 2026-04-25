class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_salary(self):
        return self.salary + self.bonus


# Usage
emp = Employee("Rahul", 30000, 5000)
print("Total Salary:", emp.calculate_total_salary())