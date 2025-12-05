# аудиторная работа по методам строк от 20.10.2025

# Задача 1: Форматирование ФИО
full_name = "иванов иван иванович"
# Ожидаемый вывод: "Иванов И.И."
surname, name, patronymic = full_name.split()
print(f"{surname.capitalize()}, {name.capitalize()[0]}. {patronymic.capitalize()[0]}.")

# Задача 2: Анализ пароля - показали сразу готовое решение, не решали самостоятельно

# Задача 3: Обработка пути к файлу
path = "/home/user/documents/report.pdf"
# Извлеките имя файла без расширения
# Ожидаемый вывод: "report"
print(path.split("/")[-1].split(".")[0])

# Задача 4: Поиск телефона
# Задача 4: Поиск телефона
import re

text = "Звоните по номеру +7-123-456-78-90 или +7-987-654-32-10"
# Найдите все номера телефонов (содержат +7-)
phone_numbers = re.findall(r"\+7-\d{3}-\d{3}-\d{2}-\d{2}", text)
print(phone_numbers)

# Задача 5: Нормализация текста
text = "   ЭТОТ ТЕКСТ ПИСАЛИ КАПСОМ    "
# Приведите к нормальному виду: первая буква заглавная, остальные маленькие
# Ожидаемый вывод: "Этот текст писали капсом"
text = text.strip()
text = text.lower()
print(text.capitalize())

# Задача 6: Подсчет слов
sentence = "Быстрый рыжий лис прыгает через ленивую собаку"
# Посчитайте количество слов в предложении
sentence_splitted = sentence.split()
print(len(sentence_splitted))

# Задача 7: Замена даты
text = "Встречаемся 2023-12-31 в 20:00"
# Замените формат даты на 31.12.2023
print(text.replace("2023-12-31", "31.12.2023"))

# Задача 8: Валидация имени файла
filename = "my_document.backup.pdf"
# Проверьте, является ли файл PDF-документом
print(filename.endswith(".pdf"))

# Задача 9: Разбор URL
url = "https://example.com/category/product.html"
# Извлеките домен и имя страницы
parts = url.split("/")
domain = parts[2]
page = parts[-1].replace(".html", "")
print(domain, page)

# Задача 10: Генератор логина
full_name = "Maria Ivanova"
# Создайте логин в формате: m_ivanova
name, surname = full_name.split()
login = f"{name[0].lower()}_{surname.lower()}"
print(login)
