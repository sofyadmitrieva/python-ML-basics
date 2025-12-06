# 0

numbers = []

while True:
    s = input("Числа через пробел: ")
    items = s.split()
    filtered = [int(x) for x in items if x.isdigit() and int(x) > 0 and int(x) % 2 == 0]
    numbers.extend(filtered)
    if "0" in items:
        break

print("Результат:", numbers)
print("Длина списка:", len(numbers))


# 1 (1)

celsius = [0, 15, 25, 30, 40, 100]
fahrenheit = [c * 9 / 5 + 32 for c in celsius]
print(fahrenheit)

# 1 (2)

grades = [45, 85, 92, 33, 67, 78, 90, 55, 29, 88]
passed = [g for g in grades if g >= 60]
print(passed)


# 2

transactions = [100, -50, 200, -30, 150, -20, 300]
taxes = [t * 0.15 for t in transactions if t > 0]
print(taxes)


# 3

products = ["футболка", "кружка", "блокнот"]
colors = ["красный", "синий", "зеленый"]
combinations = [f"{product} - {color}" for product in products for color in colors]
print(combinations)


# 4

employees = [("Иван", 45), ("Мария", 92), ("Петр", 33), ("Анна", 67)]
performance = [
    "Отлично" if percent >= 90 else "Хорошо" if percent >= 60 else "Требует улучшения"
    for name, percent in employees
]
print(performance)


# 5

sales = [
    {"name": "Алексей", "sales": 150, "returns": 10},
    {"name": "Ольга", "sales": 200, "returns": 5},
    {"name": "Дмитрий", "sales": 80, "returns": 25},
    {"name": "Елена", "sales": 300, "returns": 8},
]

top_managers = [
    s["name"]
    for s in sales
    if (s["sales"] - s["returns"] >= 150) and (s["returns"] / s["sales"] * 100 < 10)
]

print(top_managers)
