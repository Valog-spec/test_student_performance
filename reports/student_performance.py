from collections import defaultdict
from typing import Any, List

from tabulate import tabulate


class StudentPerformanceReport:
    """Отчет об успеваемости студентов"""

    @staticmethod
    def create(data: List[dict]) -> List[Any]:
        """Создает отсортированный по убыванию отчет со средними оценками студентов"""

        student_grades = defaultdict(list)

        for row in data:
            student_name = row["student_name"]
            grade = float(row["grade"])
            student_grades[student_name].append(grade)

        student_averages = []
        for student, grades in student_grades.items():
            average = sum(grades) / len(grades)
            student_averages.append((student, round(average, 2)))

        student_averages.sort(key=lambda x: x[1], reverse=True)
        return student_averages

    @staticmethod
    def display(data: List) -> None:
        """Вывод отчета в виде таблицы"""
        if not data:
            print("Нет данных для отображения.")
            return
        table_data = []
        for i, (student, grade) in enumerate(data, 1):
            table_data.append([i, student, grade])

        headers = ["student_name", "grade"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
