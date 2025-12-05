#3_numbers
#Задание 1
birth = int(input("Введите год рождения "))
current_year = int(input("Введите текущий год "))
age = current_year - birth
print('Вам', age, 'лет', sep=' ')

#Задание 2
rub = float(input('Сумма в рублях: '))
kurs = float(input('Курс доллара: '))
dollar = rub / kurs
print(rub, 'рублей по курсу ', kurs, '= ', dollar) 

#Задание 3
number = int(input('Введите число: '))
thousand = number // 1000
hundred = number // 100 % 10
ten = number % 100 // 10
unit = number % 10

print (number, '->', thousand, ' тысячи', hundred,  ' сотен', ten, ' десятков', unit, ' единиц')

#3_strings

# Создание форматированных логов с разделителями
print("=== USER INFORMATION ===")

# Создание визуальных разделителей
separator = "=" * 50
subseparator = "-" * 30
user = "Andrew"
action = "login"
status = "SUCCESS"
date = "15 Sep 2025"

# Склеивание лог-сообщения
log_line = date + " >> " + "User: " + user + "\n" + date + " >> " + "Action: " + action + "\n" + date + " >> " + "Status: " + status
log_block = separator + "\n" + log_line + "\n" + subseparator
print(separator)
print("User 1")
print(subseparator)
print (log_line)
print (subseparator)
print("User 2")
print(separator)

print("=== АНАЛИЗ БЛОКЧЕЙН-АДРЕСА ===")

wallet_address = "0x1a2b3c4d5e6f7890abc123def456ghi789jkl012mno345pqr678stu901vwx234yz"

# Извлекаем критически важные части адреса
protocol = wallet_address[0:2]          # первые 2 символа
checksum = wallet_address[1:10]         # от 2 до 10 символа
user_identifier = wallet_address[9:20] # от 10 до 20
network_marker = wallet_address [-8:]   # последние 8 символов

print(f"Протокол: {protocol}")
print(f"Контрольная сумма: {checksum}")
print(f"ID пользователя: {user_identifier}")
print(f"Маркер сети: {network_marker}")

# Секретный код через каждый 4-й символ
secret_pattern = wallet_address[::4]
print(f"Секретный паттерн: {secret_pattern}")

print("=== ГЕНЕРАТОР УМНЫХ ПАРОЛЕЙ ===")

base_string = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789!@#$%^&*"

# Генерируем пароли разной сложности через срезы
simple_password = base_string[::8]    # Каждый 8-й символ
medium_password = base_string[4:40:3]  # С 5-го по 40-й, каждый 3-й
complex_password = base_string[9::2] + base_string[0:31:5]  # Комбинация: c 10го каждый второй + с 0 по 30, каждый 5ый

print(f"Уровни паролей:")
print(f"Простой: {simple_password}")
print(f"Средний: {medium_password}")
print(f"Сложный: {complex_password}")

print("=== АНАЛИЗ ВРЕМЕННЫХ МЕТОК ===")

# Лог с временными метками
timestamps = [
    "2024-01-15T10:30:25Z",
    "2024-01-15T10:31:10Z", 
    "2024-01-15T10:32:45Z",
    "2024-01-15T10:33:20Z"
]

print("Анализ временных меток:")
for ts in timestamps:
    date = ts[0:10]        # 2024-01-15
    time = ts[11:19]       # 10:30:25
    hour = ts[11:13]         # 10
    minute = ts[14:16]       # 30
    
    print(f"{date} : {time} (час: {hour}, минута: {minute})")
