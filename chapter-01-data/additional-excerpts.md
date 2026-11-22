# Additional examples from the book

These are verbatim formatted blocks from the book, preserved in reading order. They include code fragments, terminal commands and example outputs. Some depend on previous steps and are not complete standalone programs. Use the named `.py` files in this directory for running the full practical builds.

### Book example block 273

```text
employee_name = "Alice"
department = "IT"
annual_salary = 42000
```

### Book example block 279

```text
annual_salary = 42000
annual_salary = 48000
```

### Book example block 290

```text
employee_name = "Alice"
department = "IT"
```

### Book example block 293

```text
annual_salary = 42000
employee_count = 3
```

### Book example block 296

```text
hourly_rate = 22.50
```

### Book example block 298

```text
is_active = True
```

### Book example block 300

```text
print(type(annual_salary))
```

### Book example block 302

```text
<class 'int'>
```

### Book example block 306

```text
name = "  Alice  "
print(len(name))
print(name.strip())
print(name.strip().lower())
```

### Book example block 311

```text
9
Alice
alice
```

### Book example block 320

```text
annual_salary = 42000
monthly_salary = annual_salary / 12
print(monthly_salary)
```

### Book example block 324

```text
3500.0
```

### Book example block 329

```text
salary_text = input("Enter annual salary: ")
```

### Book example block 332

```text
salary_text = input("Enter annual salary: ")
annual_salary = int(salary_text)
monthly_salary = annual_salary / 12
print(monthly_salary)
```

### Book example block 337

```text
3500.0
```

### Book example block 343

```text
monthly_salary = 3500.0
print(f"Monthly salary: £{monthly_salary:,.2f}")
```

### Book example block 346

```text
Monthly salary: £3,500.00
```

### Book example block 365

```text
Employee: Alice
Annual salary: £42,000.00
Monthly salary: £3,500.00
```

### Book example block 369

```text
Employee: Alice
Annual salary: £48,000.00
Monthly salary: £4,000.00
```

### Book example block 2244

```text
def classify(value):
    if value > 10:
        return "large"
    else:
        return "small"
```

### Book example block 2261

```text
{"name": "Alice", "department": "IT", "salary": 42000}
```

### Book example block 2267

```text
python3 -m venv venv
venv/bin/python -m pip install scikit-learn
```

### Book example block 2270

```text
python -m venv venv
.\venv\Scripts\python.exe -m pip install scikit-learn
```

### Book example block 2286

```text
from sklearn.datasets import load_iris

iris = load_iris()

print(iris.data.shape)
print(iris.target.shape)
```

### Book example block 2293

```text
(150, 4)
(150,)
```

### Book example block 2304

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

### Book example block 2320

```text
105
45
```

### Book example block 2332

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

### Book example block 2351

```text
Model trained
```

### Book example block 2355

```text
predictions = model.predict(X_test)
```

### Book example block 2358

```text
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")
```

### Book example block 2363

```text
Accuracy: 0.98
```

### Book example block 2369

```text
new_measurements = [[5.0, 3.5, 1.3, 0.3]]

prediction = model.predict(new_measurements)
species_name = iris.target_names[prediction[0]]

print(f"Predicted species: {species_name}")
```

### Book example block 2376

```text
Predicted species: setosa
```

### Book example block 2410

```text
venv/bin/python first_ai_model.py
```

### Book example block 2412

```text
.\venv\Scripts\python.exe first_ai_model.py
```

### Book example block 2414

```text
Accuracy: 0.98
Predicted species: setosa
```
