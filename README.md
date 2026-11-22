# Learn Python in 10 Minutes — Second Edition

**Companion code for the book by Victor Ebai.**

Use these files to copy and run the practical examples as you read. The explanations, exercise order, decisions and expected results remain in the book. The Python programs are extracted directly from the book; the final Flask `app.py` combines the two verbatim listings in Chapter 9 as instructed there.

## Start here

You need Python 3. On macOS, use `python3`; on Windows, use `python` (or `py` if your installation uses the Python launcher). Open a terminal in the relevant folder before running a script. The early examples also work in a browser-based Python runner.

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

Each directory has a short README and the exact chapter scripts. `additional-excerpts.md` preserves other short code snippets, commands and displayed outputs from the book; these excerpts are **not** necessarily independent runnable programs.

## Simple verification

Run the standard-library chapters with Python 3. For Chapter 9 install Flask in a virtual environment; for Chapter 10 install scikit-learn. Follow the book's commands for your operating system. The optional AWS bonus requires Boto3, a private lab S3 bucket and your own AWS credentials; it can incur charges. Always verify AWS identity and clean up the specific objects you create.

**About exact alignment:** Complete Python scripts have been transcribed without modifying their instructions, strings or variables. The two Chapter 9 listings are combined in `app.py` only because the book explicitly tells you to insert the second route into the first program. Test results and status are documented separately from the book's code.

**Book:** *Learn Python in 10 Minutes — Second Edition*, by Victor Ebai.
