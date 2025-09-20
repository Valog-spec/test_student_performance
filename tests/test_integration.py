from unittest.mock import patch

import pytest

from main import main
from reports.student_performance import StudentPerformanceReport
from utils.file_reader import read_csv_files


def test_with_valid_files(temp_csv_files, capsys):
    """Тест скрипта с валидными аргументами"""
    with patch(
        "sys.argv",
        ["main.py", "--files"] + temp_csv_files + ["--report", "students-performance"],
    ):
        main()
        captured = capsys.readouterr()
        assert "student_name" in captured.out
        assert "grade" in captured.out
        assert "Семенова Елена" in captured.out


def test_with_invalid_files(temp_csv_files, capsys):
    """Тест скрипта с несуществующими файлами"""
    with patch(
        "sys.argv",
        [
            "main.py",
            "--test_files test1.csv test2.csv --report",
            "students-performance",
        ],
    ):
        with pytest.raises(SystemExit):
            main()


def test_end_to_end(temp_csv_files, capsys):
    """Полный E2E тест"""
    data = read_csv_files(temp_csv_files)
    assert len(data) == 5

    report = StudentPerformanceReport()
    result = report.create(data)
    assert len(result) == 3

    report.display(result)
    captured = capsys.readouterr()
    assert "student_name" in captured.out
    assert "grade" in captured.out
