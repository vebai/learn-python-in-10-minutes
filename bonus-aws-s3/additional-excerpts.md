# Additional examples from the book

These are verbatim formatted blocks from the book, preserved in reading order. They include code fragments, terminal commands and example outputs. Some depend on previous steps and are not complete standalone programs. Use the named `.py` files in this directory for running the full practical builds.

### Book example block 2484

```text
aws sts get-caller-identity
```

### Book example block 2491

```text
python3 -m venv venv
venv/bin/python -m pip install boto3
```

### Book example block 2494

```text
python -m venv venv
.\venv\Scripts\python.exe -m pip install boto3
```

### Book example block 2529

```text
venv/bin/python upload_to_s3.py
```

### Book example block 2531

```text
.\venv\Scripts\python.exe upload_to_s3.py
```

### Book example block 2533

```text
Verified s3://your-lab-bucket-name/python-bonus/employees.json
Object size: 612 bytes
```

### Book example block 2580

```text
venv/bin/python cleanup_s3.py
```

### Book example block 2582

```text
.\venv\Scripts\python.exe cleanup_s3.py
```

### Book example block 2584

```text
Delete requested for s3://your-lab-bucket-name/python-bonus/employees.json
Verify in the AWS Console that the object no longer appears.
```
