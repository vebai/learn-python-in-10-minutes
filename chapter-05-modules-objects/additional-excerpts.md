# Additional examples

These examples accompany the chapter. Some are terminal commands or sample output rather than complete programs. Run the `.py` files in this folder for full exercises.

### Example 1

```text
def monthly_salary(annual_salary):
    return annual_salary / 12
```

### Example 2

```text
import math

print(math.sqrt(144))
```

### Example 3

```text
12.0
```

### Example 4

```text
from math import sqrt

print(sqrt(144))
```

### Example 5

```text
12.0
```

### Example 6

```text
from datetime import date

today = date.today()
print(today)
```

### Example 7

```text
2026-11-20
```

### Example 8

```text
name = "  Alice  "
print(name.strip())
```

### Example 9

```text
Alice
```

### Example 10

```text
employee_names = ["Alice", "Sam"]
employee_names.append("Priya")
print(employee_names)
```

### Example 11

```text
['Alice', 'Sam', 'Priya']
```

### Example 12

```text
print(type("Alice"))
print(type(["Alice", "Sam"]))
```

### Example 13

```text
<class 'str'>
<class 'list'>
```

### Example 14

```text
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

alice = Employee("Alice", "IT")
print(alice.name)
print(alice.department)
```

### Example 15

```text
IT
```

### Example 16

```text
print(alice.name)
print(alice.department)
print("  Alice  ".strip())
```

### Example 17

```text
Alice
IT
Alice
```

### Example 18

```text
employee = {"name": "Alice", "department": "IT"}
print(employee["name"])
```

### Example 19

```text
Directory as of 2026-11-20
Alice: IT
Sam: Finance
Priya: IT
```
