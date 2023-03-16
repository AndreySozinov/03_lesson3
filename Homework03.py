# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве
# значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

BACKPACK_CAPACITY = 20
things_dict = {'rope': 2, 'pot': 5, 'matches': 1, 'axe': 10, 'notebook': 5, 'pizza': 3}

total_weight = 0
for item, weight in things_dict.items():
    total_weight += things_dict[item]
    if total_weight <= BACKPACK_CAPACITY:
        print(item, weight)
    else:
        break


