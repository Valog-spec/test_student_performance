import os
from typing import List


def validate_files_exist(file_paths: List) -> None:
    for file_path in file_paths:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл '{file_path}' не найден")
