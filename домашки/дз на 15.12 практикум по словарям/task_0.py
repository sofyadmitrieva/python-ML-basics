import json

# 1 прочитать json-файл в словарь data
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 2 итерировать по всем ключам верхнего уровня и вывести их
print("\nКлючи верхнего уровня:")
for key in data.keys():
    print(key)

# 3 итерировать по всем значениям словаря departments
print("\nЗначения словаря departments:")
for department in data["departments"].values():
    print(department)

# 4 итерировать по парам ключ-значение в departments
print("\nПары ключ-значение в departments:")
for key, value in data["departments"].items():
    print(f"{key}: {value}")

# 5 добавить David в отдел dev
data["departments"]["dev"].append("David")
print(f"{data['departments']['dev']}")

# 6 увеличить бюджет на 10%
data["budget"] *= 1.1
print(f"Бюджет после увеличения на 10%: {data['budget']}")

# 7 записать измененный словарь обратно в файл
with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

print("\nИзменения сохранены в файл data.json")