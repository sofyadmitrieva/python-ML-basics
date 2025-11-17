# Координаты ВШЭ слайд 27
coordinates = (59.923040, 30.303444)

# еще примеры кортежей
# 1
user_data = ("Иванов Иван", +7123456789)
# 2
email = "example@mail.ru"
# 3
chosen_subjects = ("programming", "maths", "linguistics")

# множество из строки "программирование"слайд 28
stroka = "программирование"
set(stroka)
print(stroka)

# слайд 30
word = "hello"
set(word)
list(word)
tuple(word)

print(set(word))  # {'h', 'e', 'l', 'o'}
print(list(word))  # ['h', 'e', 'l', 'l', 'o']
print(tuple(word))  # ('h', 'e', 'l', 'l', 'o')

# Задачи на синтаксис списков слайд 38
numbers = [10, 20, 30]
numbers.append(40)  # 1. Добавьте число 40 в конец
numbers.remove(20)  # 2. Удалите число 20
numbers.insert(0, 5)  # 3. Вставьте число 5 на начало списка
print(numbers)  # Выведите результат

# Кортеж. Задача слайд 41
rgb = (255, 128, 0)
print(rgb[1])  # 1. Выведите второй элемент кортежа
rgb[0] = 200  # 2. Попробуйте изменить первый элемент на 200
# 3. Объясните, какая ошибка возникла: TypeError

# Множество. Задача слайд 44
# Дано:
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Найдите:
common_elements = set1 & set2  # 1. Общие элементы (пересечение)
unique_elements = set1 | set2  # 2. Все уникальные элементы (объединение)
different_elements = set1 - set2  # 3. Элементы, которые есть в set1, но нет в set2

print(common_elements)
print(unique_elements)
print(different_elements)

# слайд 50
mixed_data = [
    1,
    "hello",
    3.14,
    [1, 2],
    42,
    "world",
    0,
    (5, 6),
    {"name": "John"},
    True,
    {7, 8, 9},
]

data_ints = []
data_strings = []
data_lists = []
data_tuples = []
data_sets = []
data_floats = []

for structure in mixed_data:
    if isinstance(structure, int) and not isinstance(
        structure, bool
    ):  # bool — подкласс int, исключаем
        data_ints.append(structure)
    elif isinstance(structure, str):
        data_strings.append(structure)
    elif isinstance(structure, list):
        data_lists.append(structure)
    elif isinstance(structure, tuple):
        data_tuples.append(structure)
    elif isinstance(structure, set):
        data_sets.append(structure)
    elif isinstance(structure, float):
        data_floats.append(structure)

print("целые числа:", data_ints)
print("строки:", data_strings)
print("списки:", data_lists)
print("кортежи:", data_tuples)
print("множества:", data_sets)
print("дробные числа:", data_floats)
