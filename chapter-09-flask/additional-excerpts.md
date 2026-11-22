# Additional examples from the book

These are verbatim formatted blocks from the book, preserved in reading order. They include code fragments, terminal commands and example outputs. Some depend on previous steps and are not complete standalone programs. Use the named `.py` files in this directory for running the full practical builds.

### Book example block 1938

```text
cursor = connection.execute(
    "SELECT id, name, department, salary FROM employees ORDER BY id"
)
```

### Book example block 1975

```text
python3 -m venv venv
```

### Book example block 1977

```text
python -m venv venv
```

### Book example block 1982

```text
venv/bin/python -m pip install flask
```

### Book example block 1984

```text
.\venv\Scripts\python.exe -m pip install flask
```

### Book example block 2002

```text
venv/bin/python app.py
```

### Book example block 2004

```text
.\venv\Scripts\python.exe app.py
```

### Book example block 2006

```text
 * Running on http://127.0.0.1:5000
```

### Book example block 2008

```text
http://127.0.0.1:5000/
```

### Book example block 2010

```text
Employee Directory API
```

### Book example block 2052

```text
venv/bin/python init_db.py
```

### Book example block 2054

```text
.\venv\Scripts\python.exe init_db.py
```

### Book example block 2056

```text
Database initialised
```

### Book example block 2099

```text
venv/bin/python app.py
```

### Book example block 2101

```text
.\venv\Scripts\python.exe app.py
```

### Book example block 2103

```text
http://127.0.0.1:5000/employees
```

### Book example block 2106

```text
[
  {"department": "IT", "id": 1, "name": "Alice", "salary": 42000},
  {"department": "Finance", "id": 2, "name": "Sam", "salary": 38000},
  {"department": "IT", "id": 3, "name": "Priya", "salary": 45000}
]
```

### Book example block 2116

```text
@app.route("/employees/<int:employee_id>")
def get_employee(employee_id):
    connection = get_connection()
    cursor = connection.execute(
        "SELECT id, name, department, salary FROM employees WHERE id = ?",
        (employee_id,)
    )
    row = cursor.fetchone()
    connection.close()

    if row is None:
        return jsonify({"error": "Employee not found"}), 404

    employee = {
        "id": row[0],
        "name": row[1],
        "department": row[2],
        "salary": row[3]
    }
    return jsonify(employee)
```

### Book example block 2143

```text
venv/bin/python app.py
```

### Book example block 2145

```text
.\venv\Scripts\python.exe app.py
```

### Book example block 2149

```text
http://127.0.0.1:5000/employees/1
```

### Book example block 2151

```text
{
  "department": "IT",
  "id": 1,
  "name": "Alice",
  "salary": 42000
}
```

### Book example block 2158

```text
http://127.0.0.1:5000/employees/9999
```

### Book example block 2160

```text
{"error": "Employee not found"}
```

### Book example block 2190

```text
venv/bin/python update_employee.py
```

### Book example block 2192

```text
.\venv\Scripts\python.exe update_employee.py
```

### Book example block 2194

```text
Updated Alice's department
```

### Book example block 2197

```text
venv/bin/python app.py
```

### Book example block 2199

```text
.\venv\Scripts\python.exe app.py
```

### Book example block 2201

```text
http://127.0.0.1:5000/employees/1
```
