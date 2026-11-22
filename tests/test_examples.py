"""Exercise the examples without editing their code or using AWS."""

import contextlib
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_example(path, directory, input_text=None):
    return subprocess.run(
        [sys.executable, str(ROOT / path)],
        cwd=directory,
        input=input_text,
        text=True,
        capture_output=True,
        timeout=90,
        check=False,
    )


@contextlib.contextmanager
def temp_workdir():
    with tempfile.TemporaryDirectory() as folder:
        previous = Path.cwd()
        try:
            os.chdir(folder)
            yield Path(folder)
        finally:
            os.chdir(previous)


class BookExamples(unittest.TestCase):
    def test_python_syntax(self):
        for path in ROOT.rglob("*.py"):
            if ".venv" not in path.parts and "venv" not in path.parts:
                with self.subTest(path=path):
                    compile(path.read_text(encoding="utf-8"), str(path), "exec")

    def test_quick_start_and_chapters_1_to_5(self):
        cases = (
            ("quick-start/hello.py", "Hello, Alex!"),
            ("chapter-01-data/salary.py", "Monthly salary: £3,500.00"),
            ("chapter-02-collections/directory.py", "Employee count: 4"),
            ("chapter-03-decisions/filter_employees.py", "Priya: £45,000.00"),
            ("chapter-04-functions/salary_functions.py", "Alice's monthly salary: £3,500.00"),
            ("chapter-05-modules-objects/modules_and_objects.py", "Alice: IT"),
        )
        with temp_workdir() as folder:
            for path, expected in cases:
                with self.subTest(path=path):
                    result = run_example(path, folder)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn(expected, result.stdout)

    def test_chapter_6_errors(self):
        with temp_workdir() as folder:
            good = run_example("chapter-06-errors/safe_salary.py", folder, "42000\n")
            bad = run_example("chapter-06-errors/safe_salary.py", folder, "hello\n")
            deliberate = run_example("chapter-06-errors/traceback_demo.py", folder)
            self.assertEqual(good.returncode, 0, good.stderr)
            self.assertEqual(bad.returncode, 0, bad.stderr)
            self.assertIn("£3,500.00", good.stdout)
            self.assertIn("Please enter a whole number.", bad.stdout)
            self.assertNotEqual(deliberate.returncode, 0)
            self.assertIn("TypeError", deliberate.stderr)

    def test_chapter_7_files(self):
        scripts = (
            "chapter-07-files-json/write_text.py",
            "chapter-07-files-json/read_text.py",
            "chapter-07-files-json/save_employees.py",
            "chapter-07-files-json/load_employees.py",
        )
        with temp_workdir() as folder:
            for path in scripts:
                result = run_example(path, folder)
                self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((folder / "employees.json").exists())
            self.assertIn("Loaded 3 employees", result.stdout)

    def test_chapter_8_sqlite(self):
        with temp_workdir() as folder:
            for path in ("chapter-08-sqlite/employee_database.py", "chapter-08-sqlite/verify_database.py"):
                result = run_example(path, folder)
                self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Engineering", result.stdout)

    def test_chapter_9_flask(self):
        from importlib.util import module_from_spec, spec_from_file_location

        with temp_workdir() as folder:
            init = run_example("chapter-09-flask/init_db.py", folder)
            self.assertEqual(init.returncode, 0, init.stderr)
            spec = spec_from_file_location("book_flask_app", ROOT / "chapter-09-flask/app.py")
            module = module_from_spec(spec)
            spec.loader.exec_module(module)
            with module.app.test_client() as client:
                self.assertEqual(client.get("/").status_code, 200)
                listing = client.get("/employees")
                self.assertEqual(listing.status_code, 200)
                self.assertEqual(len(listing.get_json()), 3)
                employee = client.get("/employees/1")
                self.assertEqual(employee.status_code, 200)
                self.assertEqual(employee.get_json()["name"], "Alice")
                missing = client.get("/employees/9999")
                self.assertEqual(missing.status_code, 404)
                self.assertEqual(missing.get_json(), {"error": "Employee not found"})

    def test_chapter_10_ai(self):
        with temp_workdir() as folder:
            result = run_example("chapter-10-ai/first_ai_model.py", folder)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Accuracy:", result.stdout)
            self.assertIn("Predicted species:", result.stdout)


if __name__ == "__main__":
    unittest.main()
