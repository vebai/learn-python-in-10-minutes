# Additional examples

These examples accompany the chapter. Some are terminal commands or sample output rather than complete programs. Run the `.py` files in this folder for full exercises.

### Example 1

```text
employees = [
    {"name": "Alice", "department": "IT", "salary": 42000},
    {"name": "Sam", "department": "Finance", "salary": 38000},
    {"name": "Priya", "department": "IT", "salary": 45000}
]
```

### Example 2

```text
Hello from the Employee Directory
```

### Example 3

```text
with open("greeting.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

### Example 4

```text
file = open("greeting.txt", "r", encoding="utf-8")
content = file.read()
file.close()
```

### Example 5

```text
from pathlib import Path

path = Path("greeting.txt")
print(path.exists())
print(path.resolve())
```

### Example 6

```text
True
/path/to/your/project/greeting.txt
```

### Example 7

```text
print(employees)
```

### Example 8

```text
[{'name': 'Alice', 'department': 'IT', 'salary': 42000}, ...]
```

### Example 9

```text
[
  {"name": "Alice", "department": "IT", "salary": 42000},
  {"name": "Sam", "department": "Finance", "salary": 38000},
  {"name": "Priya", "department": "IT", "salary": 45000}
]
```

### Example 10

```text
Saved 3 employees to employees.json
```

### Example 11

```text
[
  {
    "name": "Alice",
    "department": "IT",
    "salary": 42000
  },
  {
    "name": "Sam",
    "department": "Finance",
    "salary": 38000
  },
  {
    "name": "Priya",
    "department": "IT",
    "salary": 45000
  }
]
```

### Example 12

```text
Loaded 3 employees
Alice: £42,000.00
Sam: £38,000.00
Priya: £45,000.00
```

### Example 13

```text
import json

try:
    with open("employees.json", "r", encoding="utf-8") as file:
        employees = json.load(file)
    print(f"Loaded {len(employees)} employees")
    for employee in employees:
        print(f"{employee['name']}: £{employee['salary']:,.2f}")
except FileNotFoundError:
    print("employees.json was not found.")
```
