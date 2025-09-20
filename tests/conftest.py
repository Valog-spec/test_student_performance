import csv
import os
import tempfile
from typing import Any, Generator, List

import pytest

from src.reports.student_performance import StudentPerformanceReport


@pytest.fixture
def sample_student_data() -> List[dict]:
    """Фикстура с тестовыми данными студентов"""
    return [
        {
            "student_name": "Семенова Елена",
            "subject": "Английский язык",
            "teacher_name": "Ковалева Анна",
            "date": "2023-10-10",
            "grade": "5",
        },
        {
            "student_name": "Титов Владислав",
            "subject": "География",
            "teacher_name": "Орлов Сергей",
            "date": "2023-10-12",
            "grade": "4",
        },
        {
            "student_name": "Власова Алина",
            "subject": "Биология",
            "teacher_name": "Ткаченко Наталья",
            "date": "2023-10-15",
            "grade": "5",
        },
        {
            "student_name": "Семенова Елена",
            "subject": "Математика",
            "teacher_name": "Петров Иван",
            "date": "2023-10-16",
            "grade": "3",
        },
        {
            "student_name": "Титов Владислав",
            "subject": "Физика",
            "teacher_name": "Сидоров Петр",
            "date": "2023-10-17",
            "grade": "5",
        },
    ]


@pytest.fixture
def sample_student_invalid_data() -> List[dict]:
    """Фикстура с тестовыми данными студентов"""
    return [
        {
            "student_name": "Семенова Елена",
            "subject": "Английский язык",
            "teacher_name": "Ковалева Анна",
            "date": "2023-10-10",
            "grade": "5",
        },
        {
            "student_name": "Титов Владислав",
            "subject": "География",
            "teacher_name": "Орлов Сергей",
            "date": "2023-10-12",
            "grade": "f",
        },
    ]


def create_test_csv(file_path, data) -> None:
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["student_name", "subject", "teacher_name", "date", "grade"],
        )
        writer.writeheader()
        writer.writerows(data)


@pytest.fixture
def temp_csv_files(sample_student_data) -> Generator[list[Any], Any, None]:
    """Создает временные CSV файлы для тестирования."""
    fd1, path1 = tempfile.mkstemp(suffix=".csv")
    os.close(fd1)
    create_test_csv(path1, sample_student_data[:3])

    fd2, path2 = tempfile.mkstemp(suffix=".csv")
    os.close(fd2)
    create_test_csv(path2, sample_student_data[3:])

    files = [path1, path2]

    yield files

    for file_path in files:
        if os.path.exists(file_path):
            os.unlink(file_path)


@pytest.fixture
def student_performance_report() -> StudentPerformanceReport:
    return StudentPerformanceReport()
