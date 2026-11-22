# Additional examples from the book

These are verbatim formatted blocks from the book, preserved in reading order. They include code fragments, terminal commands and example outputs. Some depend on previous steps and are not complete standalone programs. Use the named `.py` files in this directory for running the full practical builds.

### Book example block 403

```text
employee_name = "Alice"
department = "IT"
annual_salary = 42000
```

### Book example block 412

```text
employee_names = ["Alice", "Sam", "Priya"]
```

### Book example block 415

```text
employee_names = ["Alice", "Sam", "Priya"]
#                   0       1       2
```

### Book example block 418

```text
print(employee_names[0])
print(employee_names[2])
```

### Book example block 421

```text
Alice
Priya
```

### Book example block 424

```text
employee_names[1] = "Samuel"
print(employee_names)
```

### Book example block 427

```text
['Alice', 'Samuel', 'Priya']
```

### Book example block 429

```text
employee_names.append("David")
print(employee_names)
```

### Book example block 432

```text
['Alice', 'Samuel', 'Priya', 'David']
```

### Book example block 434

```text
print(len(employee_names))
```

### Book example block 436

```text
4
```

### Book example block 441

```text
    "name": "Alice",
    "department": "IT",
    "salary": 42000
}
```

### Book example block 448

```text
print(employee["department"])
```

### Book example block 451

```text
IT
```

### Book example block 454

```text
print(employee["department"])
```

### Book example block 459

```text
print(employee)
```

### Book example block 467

```text
    {"name": "Alice", "department": "IT", "salary": 42000},
    {"name": "Sam", "department": "Finance", "salary": 38000},
    {"name": "Priya", "department": "IT", "salary": 45000}
]
```

### Book example block 477

```text
print(employees[0])
```

### Book example block 479

```text
{'name': 'Alice', 'department': 'IT', 'salary': 42000}
```

### Book example block 482

```text
print(employees[0]["name"])
```

### Book example block 484

```text
Alice
```

### Book example block 487

```text
print(employees[2]["department"])
```

### Book example block 489

```text
IT
```

### Book example block 491

```text
employees.append({"name": "David", "department": "HR", "salary": 36000})
print(len(employees))
```

### Book example block 494

```text
4
```

### Book example block 501

```text
print(office_coordinates[1])
```

### Book example block 504

```text
-0.1
```

### Book example block 506

```text
office_coordinates[0] = 52.0
```

### Book example block 511

```text
departments = {"IT", "Finance", "HR", "IT"}
print(departments)
```

### Book example block 514

```text
{'IT', 'Finance', 'HR'}
```

### Book example block 517

```text
departments.add("Marketing")
print(departments)
```

### Book example block 520

```text
{'IT', 'Finance', 'HR', 'Marketing'}
```

### Book example block 528

```text
team_a = ["Alice", "Sam"]
team_b = team_a
```

### Book example block 531

```text
team_b.append("Priya")
print(team_a)
```

### Book example block 534

```text
['Alice', 'Sam', 'Priya']
```

### Book example block 537

```text
team_c = team_a.copy()
team_c.append("David")
print(team_a)
print(team_c)
```

### Book example block 542

```text
['Alice', 'Sam', 'Priya']
['Alice', 'Sam', 'Priya', 'David']
```

### Book example block 566

```text
Employee count: 3
Employee count: 4
Alice: Engineering
Sam: Finance
Priya: IT
David: HR
```
