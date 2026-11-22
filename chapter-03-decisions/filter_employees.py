employees = [
    {"name": "Alice", "department": "IT", "salary": 42000},
    {"name": "Sam", "department": "Finance", "salary": 38000},
    {"name": "Priya", "department": "IT", "salary": 45000},
    {"name": "David", "department": "HR", "salary": 36000}
]

target_department = "IT"

print(f"Employees in {target_department}:")

for employee in employees:
    if employee["department"] == target_department:
        print(f"{employee['name']}: £{employee['salary']:,.2f}")
