from datetime import date

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

alice = Employee("Alice", "IT")
sam = Employee("Sam", "Finance")
priya = Employee("Priya", "IT")

employees = [alice, sam, priya]

today = date.today()

print(f"Directory as of {today}")
for employee in employees:
    print(f"{employee.name}: {employee.department}")
