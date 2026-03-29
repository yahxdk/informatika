def find_item_index(items, goal):  # Функция для 2 аргументов
    if goal in items:  # Есть ли нужный товар в списке
        return items.index(goal)  # Возвращается индекс, если товар есть в списке
    else:
        return None  # Если товар не в списке, то вернется None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
