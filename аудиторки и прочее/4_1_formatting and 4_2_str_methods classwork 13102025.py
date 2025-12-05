#4_1_formatting
#1
rubles = 5500
exchange_rate = 0.0092  
euro = rubles * exchange_rate
print(f"{rubles} руб = {euro:.2f} €")

#2
celsius = 23.456
fahrenheit = celsius * 1.8 +32
print(f'{celsius:.1f}°C = {fahrenheit:.1f}°F')

#3
first_name = "иван"
last_name = "петров"
print(f'{first_name[0].upper()}.{last_name[0].upper()}{last_name[1::]}')

#4
price = 2500
discount = 15
new_price = price * discount / 100
print(f'Цена: {price} руб, со скидкой 15%: {int(price-new_price)} руб')

#5
downloaded = 355.678
total = 500
percent = downloaded / total * 100
print(f"Загружено: {downloaded:.1f} МБ ({percent:.1f}%)")

#6
city = "Москва"
temp = -5.3
humidity = 85
print(f'Погода в Москве: {temp}°C \nВлажность: {humidity}%')

#7
stock_name = "GAZP"
price = 158.4567
change = 2.345  # процентов
print(f'{stock_name}: {price:.2f} ₽ (+{change:.2f}%)')

#8
address = "ул. Пушкина, д. 15"
area = 75.5
price = 12500000
print(f'Продается квартира: {address} \nПлощадь: {area} м² \nЦена: {price:,.0f} руб')

#9
pi = 3.1415926535
radius = 5.5
area = pi * radius ** 2
print(f"Площадь круга (r={radius}): {area:.4f}")

#10
completed_tasks = 8
total_tasks = 15
hours_spent = 45.75
percent = completed_tasks / total_tasks * 100
print(f"Выполнено: {completed_tasks}/{total_tasks} задач ({percent:.1f}% \nЗатрачено времени: {hours_spent:.1f} часов")

#4_2_str_methods
#1
text = "   Python - отличный язык для начинающих! Python мощный.   "

# 1. Уберите лишние пробелы
clean_text = text.strip()
# 2. Подсчитайте общее количество символов
total_chars = len(clean_text)
# 3. Подсчитайте сколько раз встречается слово "Python"
python_count = clean_text.count("Python")
# 4. Проверьте, начинается ли текст с "Python"
starts_with_python = clean_text.startswith("Python")
# 5. Переведите текст в нижний регистр
lower_text = clean_text.lower()
print(f"Очищенный текст: '{clean_text}'")
print(f"Всего символов: {total_chars}")
print(f"Слов 'Python' найдено: {python_count}")
print(f"Начинается с 'Python': {starts_with_python}")
print(f"В нижнем регистре: {lower_text}")

#2
user_data = "ivanov:Иван:Петров:25:Москва"

# 1. Разбейте строку по разделителю ":"
part = user_data.split(":")
# 2. Извлеките отдельные данные
username = part[0]
first_name = part[1]
last_name = part[2]
age = part[3]
city = part[4]
print(f"Логин: {username}")
print(f"Имя: {first_name}")
print(f"Фамилия: {last_name}")
print(f"Возраст: {age}")
print(f"Город: {city}")

#3
email = "  USER@EXAMPLE.COM  "

# 1. Уберите пробелы и переведите в нижний регистр
clean_email = email.strip()
clean_email = clean_email.lower()
# 2. Проверьте, содержит ли email символ "@"
has_at = clean_email.find('@') 
# 3. Проверьте, заканчивается ли на ".com" или ".ru"
ends_with_com = clean_email.endswith('.com') 
ends_with_ru = clean_email.endswith('.ru')

print(f"Очищенный email: {clean_email}")
print(f"Содержит @: {has_at}")
print(f"Заканчивается на .com: {ends_with_com}")
print(f"Заканчивается на .ru: {ends_with_ru}")
