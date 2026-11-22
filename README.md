# Learn Python in 10 Minutes — Second Edition

**Companion code for the book by Victor Ebai.**

Use this repository to find and run the examples while reading the book. Follow the book for explanations, exercises and expected results.

## Getting started

You need Python 3. On macOS, run scripts using `python3`; on Windows, use `python` (or `py` if your installation uses the Python launcher). Open Terminal or Command Prompt in the relevant chapter folder before running a script. The early examples can also be used in a browser-based Python environment.

| Reading section | Directory | Main program |
|---|---|---|
| Quick Start and local setup | [`quick-start/`](quick-start/) | `hello.py` |
| Chapter 1: Data | [`chapter-01-data/`](chapter-01-data/) | `salary.py` |
| Chapter 2: Collections | [`chapter-02-collections/`](chapter-02-collections/) | `directory.py` |
| Chapter 3: Decisions and loops | [`chapter-03-decisions/`](chapter-03-decisions/) | `filter_employees.py` |
| Chapter 4: Functions | [`chapter-04-functions/`](chapter-04-functions/) | `salary_functions.py` |
| Chapter 5: Modules and objects | [`chapter-05-modules-objects/`](chapter-05-modules-objects/) | `modules_and_objects.py` |
| Chapter 6: Errors | [`chapter-06-errors/`](chapter-06-errors/) | `safe_salary.py` |
| Chapter 7: Files and JSON | [`chapter-07-files-json/`](chapter-07-files-json/) | `save_employees.py` |
| Chapter 8: SQLite | [`chapter-08-sqlite/`](chapter-08-sqlite/) | `employee_database.py` |
| Chapter 9: Flask web API | [`chapter-09-flask/`](chapter-09-flask/) | `init_db.py`, then `app.py` |
| Chapter 10: AI model | [`chapter-10-ai/`](chapter-10-ai/) | `first_ai_model.py` |
| Optional AWS bonus | [`bonus-aws-s3/`](bonus-aws-s3/) | `upload_to_s3.py`, then `cleanup_s3.py` |

Each folder has a short README with instructions. See its `additional-excerpts.md` file for other examples, commands and sample output.

## Running the later projects

Chapters 1–8 use Python's standard library. Chapter 9 needs Flask, Chapter 10 needs scikit-learn, and the optional AWS bonus needs Boto3. Install dependencies in a virtual environment as described in the book.

For the AWS bonus, use your own private lab bucket and AWS credentials. Check the active AWS account before making changes, be aware of possible charges and clean up resources after the exercise. Never commit credentials.
