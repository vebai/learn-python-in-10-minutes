# Additional examples from the book

These are verbatim formatted blocks from the book, preserved in reading order. They include code fragments, terminal commands and example outputs. Some depend on previous steps and are not complete standalone programs. Use the named `.py` files in this directory for running the full practical builds.

### Book example block 1622

```text
employees = [
    {"name": "Alice", "department": "IT", "salary": 42000},
    {"name": "Sam", "department": "Finance", "salary": 38000},
    {"name": "Priya", "department": "IT", "salary": 45000}
]
```

### Book example block 1628

```text
for employee in employees:
    if employee["name"] == "Alice":
        print(employee)
```

### Book example block 1649

```text
import sqlite3
```

### Book example block 1651

```text
connection = sqlite3.connect("employees.db")
```

### Book example block 1656

```text
connection.close()
```

### Book example block 1660

```text
import sqlite3

connection = sqlite3.connect("employees.db")

connection.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        salary INTEGER NOT NULL
    )
""")

connection.commit()
connection.close()
```

### Book example block 1684

```text
connection.execute(
    "INSERT OR IGNORE INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)",
    (1, "Alice", "IT", 42000)
)
connection.execute(
    "INSERT OR IGNORE INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)",
    (2, "Sam", "Finance", 38000)
)
connection.execute(
    "INSERT OR IGNORE INTO employees (id, name, department, salary) VALUES (?, ?, ?, ?)",
    (3, "Priya", "IT", 45000)
)

connection.commit()
connection.close()
```

### Book example block 1703

```text
import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.execute(
    "SELECT id, name, department, salary FROM employees ORDER BY id"
)

for row in cursor:
    print(row)

connection.close()
```

### Book example block 1716

```text
(1, 'Alice', 'IT', 42000)
(2, 'Sam', 'Finance', 38000)
(3, 'Priya', 'IT', 45000)
```

### Book example block 1722

```text
import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.execute(
    "SELECT name, department FROM employees WHERE id = ?",
    (1,)
)

row = cursor.fetchone()
print(row)

connection.close()
```

### Book example block 1736

```text
('Alice', 'IT')
```

### Book example block 1739

```text
import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.execute(
    "SELECT name, department FROM employees WHERE id = ?",
    (99,)
)

row = cursor.fetchone()

if row is None:
    print("Employee not found.")
else:
    print(row)

connection.close()
```

### Book example block 1757

```text
Employee not found.
```

### Book example block 1761

```text
import sqlite3

connection = sqlite3.connect("employees.db")

connection.execute(
    "UPDATE employees SET department = ? WHERE id = ?",
    ("Engineering", 1)
)

connection.commit()
connection.close()
```

### Book example block 1774

```text
import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.execute(
    "SELECT name, department FROM employees WHERE id = ?",
    (1,)
)
print(cursor.fetchone())

connection.close()
```

### Book example block 1786

```text
('Alice', 'Engineering')
```

### Book example block 1794

```text
connection = sqlite3.connect("employees.db")

# Execute your SQL statements here.

connection.commit()
connection.close()
```

### Book example block 1865

```text
All employees:
(1, 'Alice', 'IT', 42000)
(2, 'Sam', 'Finance', 38000)
(3, 'Priya', 'IT', 45000)

Employee with id 1:
('Alice', 'IT')

Employee with id 1 after update:
('Alice', 'Engineering')
```

### Book example block 1900

```text
Records after reopening:
(1, 'Alice', 'Engineering', 42000)
(2, 'Sam', 'Finance', 38000)
(3, 'Priya', 'IT', 45000)
```
