import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.execute(
    "SELECT id, name, department, salary FROM employees ORDER BY id"
)
print("Records after reopening:")
for row in cursor:
    print(row)

connection.close()
