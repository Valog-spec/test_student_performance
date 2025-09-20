import argparse
import sys
from argparse import Namespace
from pathlib import Path

current_dir = Path(__file__).parent
root_dir = current_dir.parent
sys.path.append(str(root_dir))

from src.reports.student_performance import StudentPerformanceReport
from src.utils import read_csv_files
from src.utils.validator import validate_files_exist

REPORTS = {
    "students-performance": StudentPerformanceReport,
}


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser(description="Анализ успевемости студентов")

    parser.add_argument("--files", nargs="+", required=True, help="Пути к CSV файлам")
    parser.add_argument("--report", required=True, help="Название отчета")

    return parser.parse_args()


def main():
    args = parse_arguments()
    validate_files_exist(args.files)
    data = read_csv_files(args.files)

    if args.report not in REPORTS:
        print(
            f"Неизвестный отчёт: {args.report}\n"
            f"Доступные:, {", ".join(REPORTS.keys())}"
        )
        return

    report = REPORTS[args.report]()
    result = report.create(data)
    report.display(result)


if __name__ == "__main__":
    main()
