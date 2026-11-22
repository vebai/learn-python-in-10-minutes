import json

with open("employees.json", "r", encoding="utf-8") as file:
    employees = json.load(file)

print(f"Loaded {len(employees)} employees")

for employee in employees:
    print(f"{employee['name']}: £{employee['salary']:,.2f}")
