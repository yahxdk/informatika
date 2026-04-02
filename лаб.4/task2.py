import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as f:  # Чтение
        reader = csv.DictReader(f)  # Создание словаря с ключами
        data = list(reader)  # Сохранение в список
    with open(OUTPUT_FILENAME, "w") as f:  # Файл для записи
        json.dump(data, f, indent=4)  # Запись


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
