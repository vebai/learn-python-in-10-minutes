employees = [
    {"name": "Alice", "department": "IT", "salary": 42000},
    {"name": "Sam", "department": "Finance", "salary": 38000},
    {"name": "Priya", "department": "IT", "salary": 45000}
]

print(f"Employee count: {len(employees)}")

employees[0]["department"] = "Engineering"

employees.append({"name": "David", "department": "HR", "salary": 36000})

print(f"Employee count: {len(employees)}")

for employee in employees:
    print(f"{employee['name']}: {employee['department']}")
