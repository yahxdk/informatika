
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


def find_common_participants(text1, text2, separator=","):   # Функция с 2 строками и разделителем
    text1 = text1.split(separator)  # Разбивает 1 строку на части с помощью ","
    text2 = text2.split(separator)  # Разбивает 2 строку на части с помощью ","
    set1 = set(text1)  # Создание множества 1 (для поиска общих далее)
    set2 = set(text2)  # Создание множества 2 (для поиска общих далее)
    common = set1.intersection(set2)  # Поиск общих
    return sorted(common)
