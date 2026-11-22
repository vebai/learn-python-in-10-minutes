# Additional examples

These examples accompany the chapter. Some are terminal commands or sample output rather than complete programs. Run the `.py` files in this folder for full exercises.

### Example 1

```text
employee_name = "Alice"
department = "IT"
annual_salary = 42000
```

### Example 2

```text
annual_salary = 42000
annual_salary = 48000
```

### Example 3

```text
employee_name = "Alice"
department = "IT"
```

### Example 4

```text
annual_salary = 42000
employee_count = 3
```

### Example 5

```text
hourly_rate = 22.50
```

### Example 6

```text
is_active = True
```

### Example 7

```text
print(type(annual_salary))
```

### Example 8

```text
<class 'int'>
```

### Example 9

```text
name = "  Alice  "
print(len(name))
print(name.strip())
print(name.strip().lower())
```

### Example 10

```text
9
Alice
alice
```

### Example 11

```text
annual_salary = 42000
monthly_salary = annual_salary / 12
print(monthly_salary)
```

### Example 12

```text
3500.0
```

### Example 13

```text
salary_text = input("Enter annual salary: ")
```

### Example 14

```text
salary_text = input("Enter annual salary: ")
annual_salary = int(salary_text)
monthly_salary = annual_salary / 12
print(monthly_salary)
```

### Example 15

```text
3500.0
```

### Example 16

```text
monthly_salary = 3500.0
print(f"Monthly salary: £{monthly_salary:,.2f}")
```

### Example 17

```text
Monthly salary: £3,500.00
```

### Example 18

```text
Employee: Alice
Annual salary: £42,000.00
Monthly salary: £3,500.00
```

### Example 19

```text
Employee: Alice
Annual salary: £48,000.00
Monthly salary: £4,000.00
```

### Example 20

```text
def classify(value):
    if value > 10:
        return "large"
    else:
        return "small"
```

### Example 21

```text
{"name": "Alice", "department": "IT", "salary": 42000}
```

### Example 22

```text
python3 -m venv venv
venv/bin/python -m pip install scikit-learn
```

### Example 23

```text
python -m venv venv
.\venv\Scripts\python.exe -m pip install scikit-learn
```

### Example 24

```text
from sklearn.datasets import load_iris

iris = load_iris()

print(iris.data.shape)
print(iris.target.shape)
```

### Example 25

```text
(150, 4)
(150,)
```

### Example 26

```text
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.3,
    random_state=42,
    stratify=iris.target
)

print(len(X_train))
print(len(X_test))
```

### Example 27

```text
105
45
```

### Example 28

```text
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.3,
    random_state=42,
    stratify=iris.target
)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

print("Model trained")
```

### Example 29

```text
Model trained
```

### Example 30

```text
predictions = model.predict(X_test)
```

### Example 31

```text
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")
```

### Example 32

```text
Accuracy: 0.98
```

### Example 33

```text
new_measurements = [[5.0, 3.5, 1.3, 0.3]]

prediction = model.predict(new_measurements)
species_name = iris.target_names[prediction[0]]

print(f"Predicted species: {species_name}")
```

### Example 34

```text
Predicted species: setosa
```

### Example 35

```text
venv/bin/python first_ai_model.py
```

### Example 36

```text
.\venv\Scripts\python.exe first_ai_model.py
```

### Example 37

```text
Accuracy: 0.98
Predicted species: setosa
```
