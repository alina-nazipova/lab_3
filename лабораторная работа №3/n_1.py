def find_first_index(products, product): # вызываем функцию
    for position, item in enumerate(products):  # перебираем все элементы списка с их индексами
        if item == product: # проверяем, совпадает ли текущий товар с искомым
            return position # возвращает индекс первого вхождения товара
    return None  # если товар не найден, то возвращает None

items_list =  ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']: # проверяем вхождение товаров в список
    index_item = find_first_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")