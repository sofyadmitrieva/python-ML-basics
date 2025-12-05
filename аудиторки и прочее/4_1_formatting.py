print("=== ФИНАНСОВЫЙ ОТЧЕТ ===")

company = "ООО 'Рога и копыта'"
quarter = 4
year = 2023
revenue = 15000000.5678
expenses = 9000000.1234
profit = revenue - expenses
profit_margin = (profit / revenue) * 100

# Создайте отчет с использованием f-строк и форматирования чисел
print(company.upper())
print(f"ОТЧЕТ ЗА {quarter}-Й КВАРТАЛ {year} ГОДА")
print("-" * 50)
print(f"Выручка:           {revenue:,.2f} ₽")
print(f"Расходы:           {expenses:,.2f} ₽")
print(f"Прибыль:           {profit:,.2f} ₽")
print(f"Рентабельность:           {profit_margin:,.1f} %")

"""
=== ФИНАНСОВЫЙ ОТЧЕТ ===

ООО 'РОГА И КОПЫТА'
ОТЧЕТ ЗА 4-Й КВАРТАЛ 2023 ГОДА
--------------------------------------------------
Выручка:            15,000,000.57 ₽
Расходы:             9,000,000.12 ₽
Прибыль:             6,000,000.44 ₽
Рентабельность:             40.0 %
"""

print("=== ПРОГРЕСС ВЫПОЛНЕНИЯ ЗАДАЧ ===")

total_tasks = 150
completed_tasks = 87
progress = (completed_tasks / total_tasks) * 100

# Создайте строку прогресс-бара
bar_length = 30
filled_length = int(bar_length * completed_tasks // total_tasks)
bar = "█" * filled_length + "░" * (bar_length - filled_length)


print("ВЫПОЛНЕНИЕ ЗАДАЧ:")
print(f"[{bar}] {progress:.1f}%")
print(f"Завершено: {completed_tasks}/{total_tasks} задач")

"""
=== ПРОГРЕСС ВЫПОЛНЕНИЯ ЗАДАЧ ===

ВЫПОЛНЕНИЕ ЗАДАЧ:
[█████████████████░░░░░░░░░░░░░] 58.0%
Завершено: 87/150 задач
"""
