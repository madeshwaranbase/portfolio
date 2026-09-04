import csv
import builtins
import pytest

import employee_manager as em


@pytest.fixture(autouse=True)
def isolate_file(tmp_path, monkeypatch):
    """Point FILE_NAME at a temp file so tests never touch real employees.csv."""
    test_file = tmp_path / "employees.csv"
    monkeypatch.setattr(em, "FILE_NAME", test_file)
    yield test_file


def make_inputs(monkeypatch, values):
    """Feed a sequence of canned responses to input()."""
    it = iter(values)
    monkeypatch.setattr(builtins, "input", lambda _="": next(it))


# ---------- load / save ----------

def test_load_employees_missing_file_returns_empty(isolate_file):
    assert em.load_employees() == []


def test_save_then_load_roundtrip(isolate_file):
    data = [{"id": "1", "name": "Asha", "department": "QA", "salary": "50000"}]
    em.save_employees(data)

    loaded = em.load_employees()
    assert loaded == data
    assert isolate_file.exists()


def test_save_writes_header(isolate_file):
    em.save_employees([{"id": "1", "name": "Asha", "department": "QA", "salary": "50000"}])
    with isolate_file.open(newline="", encoding="utf-8") as f:
        header = next(csv.reader(f))
    assert header == em.FIELDS


# ---------- add_employee ----------

def test_add_employee_success_persists(monkeypatch, isolate_file):
    employees = []
    make_inputs(monkeypatch, ["1", "Asha", "QA", "50000"])

    em.add_employee(employees)

    assert len(employees) == 1
    assert employees[0]["id"] == "1"
    assert employees[0]["salary"] == 50000.0
    # persisted to disk
    assert em.load_employees()[0]["name"] == "Asha"


def test_add_employee_duplicate_id_rejected(monkeypatch, isolate_file):
    employees = [{"id": "1", "name": "Asha", "department": "QA", "salary": 50000}]
    make_inputs(monkeypatch, ["1"])

    em.add_employee(employees)

    assert len(employees) == 1  # nothing added


def test_add_employee_empty_id_rejected(monkeypatch, isolate_file):
    employees = []
    make_inputs(monkeypatch, [""])

    em.add_employee(employees)

    assert employees == []


def test_add_employee_empty_name_rejected(monkeypatch, isolate_file):
    employees = []
    make_inputs(monkeypatch, ["1", "", "QA", "50000"])

    em.add_employee(employees)

    assert employees == []


def test_add_employee_invalid_salary_rejected(monkeypatch, isolate_file):
    employees = []
    make_inputs(monkeypatch, ["1", "Asha", "QA", "not-a-number"])

    em.add_employee(employees)

    assert employees == []


def test_add_employee_negative_salary_rejected(monkeypatch, isolate_file):
    employees = []
    make_inputs(monkeypatch, ["1", "Asha", "QA", "-500"])

    em.add_employee(employees)

    assert employees == []


# ---------- search_employee ----------

def test_search_employee_by_id(monkeypatch, isolate_file, capsys):
    employees = [{"id": "1", "name": "Asha", "department": "QA", "salary": 50000}]
    make_inputs(monkeypatch, ["1"])

    em.search_employee(employees)

    out = capsys.readouterr().out
    assert "Asha" in out


def test_search_employee_by_partial_name_case_insensitive(monkeypatch, isolate_file, capsys):
    employees = [{"id": "1", "name": "Asha Kumar", "department": "QA", "salary": 50000}]
    make_inputs(monkeypatch, ["ash"])

    em.search_employee(employees)

    out = capsys.readouterr().out
    assert "Asha Kumar" in out


def test_search_employee_no_match(monkeypatch, isolate_file, capsys):
    employees = [{"id": "1", "name": "Asha", "department": "QA", "salary": 50000}]
    make_inputs(monkeypatch, ["zzz"])

    em.search_employee(employees)

    out = capsys.readouterr().out
    assert "No matching employees found." in out


# ---------- delete_employee ----------

def test_delete_employee_confirmed_removes_and_persists(monkeypatch, isolate_file):
    employees = [{"id": "1", "name": "Asha", "department": "QA", "salary": 50000}]
    em.save_employees(employees)
    make_inputs(monkeypatch, ["1", "y"])

    em.delete_employee(employees)

    assert employees == []
    assert em.load_employees() == []


def test_delete_employee_declined_keeps_record(monkeypatch, isolate_file):
    employees = [{"id": "1", "name": "Asha", "department": "QA", "salary": 50000}]
    make_inputs(monkeypatch, ["1", "n"])

    em.delete_employee(employees)

    assert len(employees) == 1


def test_delete_employee_not_found(monkeypatch, isolate_file, capsys):
    employees = [{"id": "1", "name": "Asha", "department": "QA", "salary": 50000}]
    make_inputs(monkeypatch, ["999"])

    em.delete_employee(employees)

    out = capsys.readouterr().out
    assert "not found" in out.lower()
    assert len(employees) == 1
