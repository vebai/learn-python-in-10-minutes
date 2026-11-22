# Additional examples

These examples accompany the chapter. Some are terminal commands or sample output rather than complete programs. Run the `.py` files in this folder for full exercises.

### Example 1

```text
aws sts get-caller-identity
```

### Example 2

```text
python3 -m venv venv
venv/bin/python -m pip install boto3
```

### Example 3

```text
python -m venv venv
.\venv\Scripts\python.exe -m pip install boto3
```

### Example 4

```text
venv/bin/python upload_to_s3.py
```

### Example 5

```text
.\venv\Scripts\python.exe upload_to_s3.py
```

### Example 6

```text
Verified s3://your-lab-bucket-name/python-bonus/employees.json
Object size: 612 bytes
```

### Example 7

```text
venv/bin/python cleanup_s3.py
```

### Example 8

```text
.\venv\Scripts\python.exe cleanup_s3.py
```

### Example 9

```text
Delete requested for s3://your-lab-bucket-name/python-bonus/employees.json
Verify in the AWS Console that the object no longer appears.
```
