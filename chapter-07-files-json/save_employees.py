import json

employees = [
    {"name": "Alice", "department": "IT", "salary": 42000},
    {"name": "Sam", "department": "Finance", "salary": 38000},
    {"name": "Priya", "department": "IT", "salary": 45000}
]

with open("employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=2)

print(f"Saved {len(employees)} employees to employees.json")
