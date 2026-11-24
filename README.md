# Learn Python in 10 Minutes — Second Edition

This is the companion repository for *Learn Python in 10 Minutes — Second Edition* by **Victor Ebai**. It provides the Python programs, supporting files and chapter guides used by the book's practical exercises.

**The book is fully self-contained.** You can follow its explanations and learning path without this repository. If you prefer to practise, the repository gives you ready-to-run examples that you can inspect, change and verify.

The practical learning cycle is **Understand → Write → Run → Observe → Modify → Verify**. Use the book to learn the concepts and reasoning; use these files to explore their behaviour and build confidence through practice.

## Get the paperback

**[Find the current edition on Amazon UK](https://www.amazon.co.uk/s?k=Learn+Python+in+10+Minutes+Second+Edition+Victor+Ebai&i=stripbooks)** (default) · [Find on Amazon US](https://www.amazon.com/s?k=Learn+Python+in+10+Minutes+Second+Edition+Victor+Ebai&i=stripbooks)

**Optional next read:** If you would like to strengthen your understanding of algorithms, variables and the ideas shared by programming languages, *Learn Programming in 10 Minutes* provides a concept-first introduction. [Find it on Amazon UK](https://www.amazon.co.uk/s?k=Learn+Programming+in+10+Minutes+Victor+Ebai&i=stripbooks). You do not need this additional book to complete the Python exercises.

**Quick navigation:** [Getting started](#getting-started) · [Chapter examples](#find-the-examples) · [Repository layout](#repository-structure) · [Verification](#verify-your-examples) · [Optional AWS bonus](#optional-aws-bonus)

## The learning journey

Start with a short Python program, build an Employee Directory, work with files and SQLite, create a Flask web API and train a simple machine-learning model. The optional AWS bonus introduces cloud automation. Each stage builds on skills developed earlier in the book.

![Learn Python in 10 Minutes — Second Edition learning overview showing Python fundamentals, modules and objects, troubleshooting, files and SQLite, Flask APIs, machine learning and an optional AWS bonus; beneath it, the Understand, Write, Run, Observe, Modify and Verify cycle.](docs/images/learn-python-overview.png)

*Figure 0.1 — From your first Python program to practical applications. The AWS bonus is optional; the book's main learning path does not require an AWS account.*

## What you will build and practise

- Run Python programs and work with variables, decisions, loops, functions and objects.
- Develop a small Employee Directory while learning to organise and transform data.
- Read and write files, use JSON and store records in SQLite.
- Investigate errors by comparing expected output with observed behaviour.
- Create a Flask API and train a simple machine-learning model.
- Verify working examples and, optionally, practise carefully scoped S3 automation.

## Before you begin

You can start in **GitHub Codespaces** without installing Python locally, or use a terminal on **macOS or Windows**. The examples support **Python 3.10–3.13**; Codespaces is configured for Python 3.12. A GitHub account is needed for Codespaces, and its usage limits depend on your plan.

The first eight chapters use Python's standard library. Flask is required for Chapter 9, and scikit-learn for Chapter 10. Install only the dependencies you need. No AWS account is required except for the separate, optional AWS bonus.

For the AWS bonus, use a practice account, check the active identity and Region, protect your credentials and review any potential charges. The accompanying scripts do not automatically create AWS resources merely by being cloned.

## Getting started

**Option 1 — Run in the browser:** [Open this repository in GitHub Codespaces](https://codespaces.new/vebai/learn-python-in-10-minutes). Open its terminal and run the Quick Start example.

**Option 2 — Run locally:** Clone the repository with Git, or use **Code → Download ZIP** on GitHub and extract it.

```bash
git clone https://github.com/vebai/learn-python-in-10-minutes.git
cd learn-python-in-10-minutes
```

If you downloaded the ZIP, open a terminal in the extracted folder instead. Then follow [Set up on your computer](#set-up-on-your-computer).

[![Example tests](https://github.com/vebai/learn-python-in-10-minutes/actions/workflows/test.yml/badge.svg)](https://github.com/vebai/learn-python-in-10-minutes/actions/workflows/test.yml)

## Open in your browser

Choose **Open in GitHub Codespaces** above and create a codespace. The environment provides Python 3.12, Flask and scikit-learn for Chapters 1–10. Codespaces availability and usage limits depend on your GitHub account.

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

**Windows — PowerShell**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell prevents script activation under your organisation's policy, use the Command Prompt instructions above instead of changing a system-wide policy.

Chapters 1–8 use the Python standard library and need no extra packages. The installation above prepares Flask for Chapter 9. When you reach Chapter 10 or the optional AWS bonus:

```bash
python -m pip install scikit-learn
python -m pip install boto3
```

Install just the package needed for your chapter, or install both later using `python -m pip install -r requirements-extras.txt`. Run `deactivate` when you finish.

## Find the examples

| Reading section | Directory | Main program |
|---|---|---|
| Quick Start and local setup | [`quick-start/`](quick-start/) | [`hello.py`](quick-start/hello.py) |
| Chapter 1: Data | [`chapter-01-data/`](chapter-01-data/) | [`salary.py`](chapter-01-data/salary.py) |
| Chapter 2: Collections | [`chapter-02-collections/`](chapter-02-collections/) | [`directory.py`](chapter-02-collections/directory.py) |
| Chapter 3: Decisions and loops | [`chapter-03-decisions/`](chapter-03-decisions/) | [`filter_employees.py`](chapter-03-decisions/filter_employees.py) |
| Chapter 4: Functions | [`chapter-04-functions/`](chapter-04-functions/) | [`salary_functions.py`](chapter-04-functions/salary_functions.py) |
| Chapter 5: Modules and objects | [`chapter-05-modules-objects/`](chapter-05-modules-objects/) | [`modules_and_objects.py`](chapter-05-modules-objects/modules_and_objects.py) |
| Chapter 6: Errors | [`chapter-06-errors/`](chapter-06-errors/) | [`safe_salary.py`](chapter-06-errors/safe_salary.py) |
| Chapter 7: Files and JSON | [`chapter-07-files-json/`](chapter-07-files-json/) | [`save_employees.py`](chapter-07-files-json/save_employees.py) |
| Chapter 8: SQLite | [`chapter-08-sqlite/`](chapter-08-sqlite/) | [`employee_database.py`](chapter-08-sqlite/employee_database.py) |
| Chapter 9: Flask web API | [`chapter-09-flask/`](chapter-09-flask/) | [`init_db.py`](chapter-09-flask/init_db.py), then [`app.py`](chapter-09-flask/app.py) |
| Chapter 10: AI model | [`chapter-10-ai/`](chapter-10-ai/) | [`first_ai_model.py`](chapter-10-ai/first_ai_model.py) |
| Optional AWS bonus | [`bonus-aws-s3/`](bonus-aws-s3/) | [`upload_to_s3.py`](bonus-aws-s3/upload_to_s3.py), then [`cleanup_s3.py`](bonus-aws-s3/cleanup_s3.py) |

Each directory includes a chapter README and an `additional-excerpts.md` page for smaller examples, commands and expected output. For example, run `cd chapter-01-data` followed by `python salary.py`.

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

## Licence and book guidance

The example code may be used and adapted for learning and your projects under the [repository licence](LICENSE). The published book's explanations, artwork and illustrations remain separately protected. Follow the book for the complete learning journey; use this repository for ready-to-run examples and verification.
