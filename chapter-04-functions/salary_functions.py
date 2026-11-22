def monthly_salary(annual_salary):
    return annual_salary / 12

def find_employee(employees, name):
    for employee in employees:
        if employee["name"] == name:
            return employee
    return None

employees = [
    {"name": "Alice", "department": "IT", "salary": 42000},
    {"name": "Sam", "department": "Finance", "salary": 38000},
    {"name": "Priya", "department": "IT", "salary": 45000}
]

alice = find_employee(employees, "Alice")
if alice is not None:
    print(f"Alice's monthly salary: £{monthly_salary(alice['salary']):,.2f}")

search_name = "David"
missing = find_employee(employees, search_name)
if missing is None:
    print(f"{search_name} is not in the directory")
