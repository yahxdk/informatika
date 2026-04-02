import json
INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE, "r") as f:  # Открыть файл
        data = json.load(f)   # Преобразование данных из json в python
    result = 0.0  # Переменная для суммы
    for item in data:
        score = item["score"]  # Получение чисел из словаря по ключам score, weight
        weight = item["weight"]
        result = result + (score * weight)
    return round(result, 3)


if __name__ == '__main__':  # Проверка
    print(task())
