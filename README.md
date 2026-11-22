# Learn Python in 10 Minutes — Second Edition

**Companion code for the book by Victor Ebai.** Follow the book for explanations and exercises; use this repository to find, run and modify the Python programs.

[![Python 3.10–3.13](https://img.shields.io/badge/Python-3.10--3.13-blue)](https://www.python.org/)
[![Example tests](https://github.com/vebai/learn-python-in-10-minutes/actions/workflows/test.yml/badge.svg)](https://github.com/vebai/learn-python-in-10-minutes/actions/workflows/test.yml)
[![Licence](https://img.shields.io/badge/licence-see%20LICENSE-blue)](LICENSE)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/vebai/learn-python-in-10-minutes)

[Find the book on Amazon UK](https://www.amazon.co.uk/s?k=Learn+Python+in+10+Minutes+Victor+Ebai)

## Open in your browser

Choose **Open in GitHub Codespaces** and create a codespace. The environment provides Python 3.12, Flask and scikit-learn for Chapters 1–10. Codespaces availability and usage limits depend on your GitHub account.

Open a terminal and try:

```bash
cd quick-start
python hello.py
```

## Set up on your computer

Install Python 3. Open Terminal (macOS) or Command Prompt (Windows) in the repository folder.

**macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

**Windows — Command Prompt**

```bat
py -3 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
```

Chapters 1–8 use the Python standard library and need no extra packages. The installation above prepares Flask for Chapter 9. When you reach Chapter 10 or the optional AWS bonus:

```bash
python -m pip install scikit-learn
python -m pip install boto3
```

Install just the package needed for your chapter, or install both later using `python -m pip install -r requirements-extras.txt`. Run `deactivate` when you finish.

## Find the examples

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

Each directory has a short README and an `additional-excerpts.md` page for smaller examples, commands and expected output. For example, run `cd chapter-01-data` followed by `python salary.py`.

## Repository structure

```text
learn-python-in-10-minutes/
├── quick-start/               Greeting and local setup
├── chapter-01-data/           Data and salary calculator
├── chapter-02-collections/    Employee Directory
├── chapter-03-decisions/      Decisions and loops
├── chapter-04-functions/      Reusable functions
├── chapter-05-modules-objects/
├── chapter-06-errors/         Errors and diagnostics
├── chapter-07-files-json/    Files and JSON
├── chapter-08-sqlite/        SQLite databases
├── chapter-09-flask/         Flask web API
├── chapter-10-ai/            First machine-learning model
├── bonus-aws-s3/             Optional AWS automation
├── tests/                    Automated example tests
├── .github/workflows/        GitHub Actions
├── .devcontainer/            Codespaces environment
├── requirements.txt          Flask dependency
└── requirements-extras.txt   Optional AI and AWS dependencies
```

## Verify your examples

After installing Flask and scikit-learn, run this from the repository root:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions checks the examples on Python 3.10, 3.11, 3.12 and 3.13. The tests use temporary data and do not contact AWS. One Chapter 6 program deliberately raises an error as part of the lesson.

## Optional AWS bonus

Use your own private practice bucket and sign in through an AWS CLI profile or IAM Identity Center (SSO). Follow the [AWS bonus instructions](bonus-aws-s3/README.md), check your AWS identity and Region, and clean up afterwards. AWS charges may apply. Never commit credentials.
