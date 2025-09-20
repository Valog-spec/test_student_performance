import csv
from typing import List


def read_csv_files(file_paths: List):
    """Читает данные из нескольких CSV файлов"""
    all_data = []

    for file_path in file_paths:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    all_data.append(row)
        except Exception as e:
            raise IOError(f"Ошибка чтения файла {file_path}: {e}")

    return all_data
