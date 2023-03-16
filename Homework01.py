# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

origin_list = [5, 2, 6, 5, 9, 1, 6, 6, 6]
doubles_list = []

for item in origin_list:
    if origin_list.count(item) > 1 and item not in doubles_list:
        doubles_list.append(item)

result_list = set(origin_list)

print(doubles_list)
print(result_list)
