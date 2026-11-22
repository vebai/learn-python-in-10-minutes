import sqlite3

connection = sqlite3.connect("employees.db")

connection.execute(
    "UPDATE employees SET department = ? WHERE id = ?",
    ("Engineering", 1)
)

connection.commit()
connection.close()

print("Updated Alice's department")
