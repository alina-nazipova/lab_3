
def find_common_participants(first_group, second_group, delimiter=','): # функция находит общих участников в двух группах
    first_list = first_group.split(delimiter) # разбиваем строку первой группы на список участников
    second_list = second_group.split(delimiter) # разбиваем строку второй группы на список участников
    common = set(first_list) & set(second_list) # возвращаем множество, содержащее элементы, которые есть в обоих множествах
    return sorted(common)  # возвращаем отсортированный список общих участников

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(f"Общие участники: {common_participants}")


result = find_common_participants('Иванов;Петров;Сидоров', 'Петров;Сидоров;Смирнов', ';') # пример с другим разделителем
print(result)