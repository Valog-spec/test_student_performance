# Анализ успеваемости студентов

Скрипт для анализа успеваемости студентов на основе CSV файлов. Генерирует отчеты об успеваемости с расчетом средних оценок.

## Требования
- Python
- PDM
## Установка и запуск

1. Клонируйте репозиторий:
```bash
   git clone <repository-url>
   cd src
```
2. Установите pdm(если не установлен)
```bash
  pip install pdm
```
3. Запуск скрипта 
```bash
  pdm run python main.py --files <your_file(s)> --report students-performance
```
4. Запуск скрипта с готовыми данными(для примера)
```bash
  pdm run python main.py --files example_files/students1.csv example_files/students2.csv --report students-performance
```

## Добавление нового отчета
Создайте новый файл в папке /reports. В этом файле создайте
класс, который наследуется от абстрактного класса находящийся в папке base_report.py.
Реализуйте два метода create и display. Откройте файл main.py и добавьте в словарь REPORTS
в качестве ключа название отчета, в качестве значения сам класс

## Запуск тестов

Перейдите в корень проекта и запустите тесты
```bash
   pdm run pytest tests
```