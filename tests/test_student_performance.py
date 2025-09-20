import pytest


def test_create_report(sample_student_data, student_performance_report) -> None:
    """Тест создания отчета с валидными данными"""
    result = student_performance_report.create(sample_student_data)

    assert len(result) == 3

    student_grades = dict(result)
    assert student_grades["Власова Алина"] == 5.0
    assert student_grades["Титов Владислав"] == 4.5


def test_create_report_empty_data(student_performance_report):
    """Тест с пустыми данными"""
    result = student_performance_report.create([])
    assert result == []


def test_create_report_invalid_grades(
    sample_student_invalid_data, student_performance_report
) -> None:
    """Тест создания отчета с не валидными оценками"""
    with pytest.raises(ValueError):
        student_performance_report.create(sample_student_invalid_data)
