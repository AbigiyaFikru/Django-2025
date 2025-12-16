class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def annual_salary(self):
        return self.salary * 12

# Test the class
emp = Employee("John", 5000)
print(f"{emp.name}'s annual salary: ${emp.annual_salary():,}")