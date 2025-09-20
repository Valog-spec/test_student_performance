import argparse
from argparse import Namespace

from reports.student_performance import StudentPerformanceReport
from utils.file_reader import read_csv_files
from utils.validator import validate_files_exist

REPORTS = {
    "students-performance": StudentPerformanceReport,
}


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser(description="Анализ успевемости студентов")

    parser.add_argument(
        "--test_files", nargs="+", required=True, help="Пути к CSV файлам"
    )
    parser.add_argument("--report", required=False, help="Название отчета")

    return parser.parse_args()


def main():
    args = parse_arguments()

    validate_files_exist(args.files)

    data = read_csv_files(args.files)

    if args.report not in REPORTS:
        print(f"Неизвестный отчёт: {args.report}")
        print("Доступные:", ", ".join(REPORTS.keys()))
        return

    report = REPORTS[args.report]()

    result = report.create(data)

    report.display(result)


if __name__ == "__main__":
    main()
