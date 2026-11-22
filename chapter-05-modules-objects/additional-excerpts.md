# Additional examples from the book

These are verbatim formatted blocks from the book, preserved in reading order. They include code fragments, terminal commands and example outputs. Some depend on previous steps and are not complete standalone programs. Use the named `.py` files in this directory for running the full practical builds.

### Book example block 1004

```text
def monthly_salary(annual_salary):
    return annual_salary / 12
```

### Book example block 1012

```text
import math

print(math.sqrt(144))
```

### Book example block 1016

```text
12.0
```

### Book example block 1019

```text
from math import sqrt

print(sqrt(144))
```

### Book example block 1023

```text
12.0
```

### Book example block 1029

```text
from datetime import date

today = date.today()
print(today)
```

### Book example block 1034

```text
2026-11-20
```

### Book example block 1048

```text
name = "  Alice  "
print(name.strip())
```

### Book example block 1051

```text
Alice
```

### Book example block 1054

```text
employee_names = ["Alice", "Sam"]
employee_names.append("Priya")
print(employee_names)
```

### Book example block 1059

```text
['Alice', 'Sam', 'Priya']
```

### Book example block 1066

```text
print(type("Alice"))
print(type(["Alice", "Sam"]))
```

### Book example block 1069

```text
<class 'str'>
<class 'list'>
```

### Book example block 1072

```text
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

alice = Employee("Alice", "IT")
print(alice.name)
print(alice.department)
```

### Book example block 1082

```text
IT
```

### Book example block 1092

```text
print(alice.name)
print(alice.department)
print("  Alice  ".strip())
```

### Book example block 1096

```text
Alice
IT
Alice
```

### Book example block 1101

```text
employee = {"name": "Alice", "department": "IT"}
print(employee["name"])
```

### Book example block 1127

```text
Directory as of 2026-11-20
Alice: IT
Sam: Finance
Priya: IT
```
