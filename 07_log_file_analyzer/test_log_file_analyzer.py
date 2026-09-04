import pytest

import log_file_analyzer as la


@pytest.fixture
def log_path(tmp_path):
    return tmp_path / "test.log"


def write_log(path, content):
    path.write_text(content, encoding="utf-8")
    return path


# ---------- ensure_sample_log ----------

def test_ensure_sample_log_creates_file_when_missing(log_path):
    assert not log_path.exists()
    la.ensure_sample_log(log_path)
    assert log_path.exists()
    assert log_path.read_text(encoding="utf-8") == la.SAMPLE_LOG


def test_ensure_sample_log_does_not_overwrite_existing(log_path):
    write_log(log_path, "INFO custom line\n")
    la.ensure_sample_log(log_path)
    assert log_path.read_text(encoding="utf-8") == "INFO custom line\n"


# ---------- parse_log ----------

def test_parse_log_counts_levels(log_path):
    write_log(log_path, la.SAMPLE_LOG)
    levels, messages = la.parse_log(log_path)

    assert levels["INFO"] == 2
    assert levels["ERROR"] == 3
    assert levels["WARNING"] == 1


def test_parse_log_counts_error_messages(log_path):
    write_log(log_path, la.SAMPLE_LOG)
    _, messages = la.parse_log(log_path)

    assert messages["Database connection failed"] == 2
    assert messages["Timeout occurred"] == 1


def test_parse_log_ignores_blank_lines(log_path):
    write_log(log_path, "INFO Login successful\n\n\nERROR Timeout occurred\n")
    levels, _ = la.parse_log(log_path)

    assert levels["INFO"] == 1
    assert levels["ERROR"] == 1
    assert sum(levels.values()) == 2


def test_parse_log_handles_level_with_no_message(log_path):
    write_log(log_path, "INFO\n")
    levels, messages = la.parse_log(log_path)

    assert levels["INFO"] == 1
    assert messages == {}


def test_parse_log_non_error_levels_not_in_messages(log_path):
    write_log(log_path, "WARNING Slow response\nINFO Login successful\n")
    _, messages = la.parse_log(log_path)

    assert messages == {}


def test_parse_log_empty_file(log_path):
    write_log(log_path, "")
    levels, messages = la.parse_log(log_path)

    assert levels == {}
    assert messages == {}


# ---------- format_summary ----------

def test_format_summary_includes_header():
    summary = la.format_summary(la.Counter(), la.Counter())
    assert summary.startswith("Log Summary\n-----------")


def test_format_summary_lists_level_counts():
    levels = la.Counter({"INFO": 2, "ERROR": 3})
    summary = la.format_summary(levels, la.Counter())

    assert "INFO    : 2" in summary
    assert "ERROR   : 3" in summary


def test_format_summary_includes_most_common_error_when_present():
    levels = la.Counter({"ERROR": 2})
    messages = la.Counter({"Database connection failed": 2, "Timeout occurred": 1})
    summary = la.format_summary(levels, messages)

    assert "Most common error:" in summary
    assert "Database connection failed" in summary


def test_format_summary_omits_error_section_when_no_errors():
    levels = la.Counter({"INFO": 1})
    summary = la.format_summary(levels, la.Counter())

    assert "Most common error" not in summary


# ---------- main (integration) ----------

def test_main_creates_log_and_prints_summary(tmp_path, monkeypatch, capsys):
    # main() uses the module-level LOG_FILE default (relative "sample.log"),
    # so run it from a temp cwd rather than fighting bound default args.
    monkeypatch.chdir(tmp_path)

    la.main()

    out = capsys.readouterr().out
    assert "Log Summary" in out
    assert "Most common error:" in out
    assert (tmp_path / "sample.log").exists()
