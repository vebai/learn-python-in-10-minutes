# Additional examples from the book

These are verbatim formatted blocks from the book, preserved in reading order. They include code fragments, terminal commands and example outputs. Some depend on previous steps and are not complete standalone programs. Use the named `.py` files in this directory for running the full practical builds.

### Book example block 1434

```text
employees = [
    {"name": "Alice", "department": "IT", "salary": 42000},
    {"name": "Sam", "department": "Finance", "salary": 38000},
    {"name": "Priya", "department": "IT", "salary": 45000}
]
```

### Book example block 1458

```text
Hello from the Employee Directory
```

### Book example block 1463

```text
with open("greeting.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

### Book example block 1467

```text
file = open("greeting.txt", "r", encoding="utf-8")
content = file.read()
file.close()
```

### Book example block 1478

```text
from pathlib import Path

path = Path("greeting.txt")
print(path.exists())
print(path.resolve())
```

### Book example block 1484

```text
True
/path/to/your/project/greeting.txt
```

### Book example block 1490

```text
print(employees)
```

### Book example block 1492

```text
[{'name': 'Alice', 'department': 'IT', 'salary': 42000}, ...]
```

### Book example block 1495

```text
[
  {"name": "Alice", "department": "IT", "salary": 42000},
  {"name": "Sam", "department": "Finance", "salary": 38000},
  {"name": "Priya", "department": "IT", "salary": 45000}
]
```

### Book example block 1523

```text
Saved 3 employees to employees.json
```

### Book example block 1526

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

### Book example block 1558

```text
Loaded 3 employees
Alice: £42,000.00
Sam: £38,000.00
Priya: £45,000.00
```

### Book example block 1591

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
