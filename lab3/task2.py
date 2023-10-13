# TODO Напишите функцию find_common_participants
def find_common_participants(str1: str, str2: str, sep=","):
    first_unique_part = set(str.split(str1, sep=sep))
    sec_unique_part = set(str.split(str2, sep=sep))
    return sorted(first_unique_part & sec_unique_part)



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
