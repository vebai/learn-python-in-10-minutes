# Additional examples

These examples accompany the chapter. Some are terminal commands or sample output rather than complete programs. Run the `.py` files in this folder for full exercises.

### Example 1

```text
def classify(value):
    if value > 10:
        return "large"
    else:
        return "small"
```

### Example 2

```text
{"name": "Alice", "department": "IT", "salary": 42000}
```

### Example 3

```text
python3 -m venv venv
venv/bin/python -m pip install scikit-learn
```

### Example 4

```text
python -m venv venv
.\venv\Scripts\python.exe -m pip install scikit-learn
```

### Example 5

```text
from sklearn.datasets import load_iris

iris = load_iris()

print(iris.data.shape)
print(iris.target.shape)
```

### Example 6

```text
(150, 4)
(150,)
```

### Example 7

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

### Example 8

```text
105
45
```

### Example 9

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

### Example 10

```text
Model trained
```

### Example 11

```text
predictions = model.predict(X_test)
```

### Example 12

```text
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy:.2f}")
```

### Example 13

```text
Accuracy: 0.98
```

### Example 14

```text
new_measurements = [[5.0, 3.5, 1.3, 0.3]]

prediction = model.predict(new_measurements)
species_name = iris.target_names[prediction[0]]

print(f"Predicted species: {species_name}")
```

### Example 15

```text
Predicted species: setosa
```

### Example 16

```text
venv/bin/python first_ai_model.py
```

### Example 17

```text
.\venv\Scripts\python.exe first_ai_model.py
```

### Example 18

```text
Accuracy: 0.98
Predicted species: setosa
```
