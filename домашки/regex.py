"""
Задачи на регулярные выражения
"""
import re
text = "Цены: 100 руб, $50, 75.50 евро, 200₽, 300"
# Задача: Найти все цены с валютами (руб, $, евро, ₽)
# Ожидаемый результат: ['100 руб', '$50', '75.50 евро', '200₽']
prices = re.findall(r'(?:\d+(?:\.\d+)?\s?(?:руб|евро|₽)|\$\d+(?:\.\d+)?)', text)
print(prices)

import re
html = "<div>Текст <b>жирный</b> и <i>курсивный</i></div>"
# Задача: Удалить все HTML-теги, оставив только текст
# Ожидаемый результат: "Текст жирный и курсивный"
new_html = re.sub(r'<.*?>', '', html)
print(new_html)

import re
text = "Версии: Python 3.9, Java 17.0.1, Node.js v18.15.0, проект v1.2.3.4"
# Задача: Найти все номера версий (числа с точками)
# Ожидаемый результат: ['3.9', '17.0.1', '18.15.0', '1.2.3.4']
numbers = re.findall(r'\d+\.\d+|\d+\.\d+\.\d+|\d+\.\d+\.\d+\.\d+', text)
print(numbers)

import re
complex_text = """
Клиент Иван Иванов (ivan@mail.com, +7-912-345-67-89) 
заказал товар #12345 за 1,500.50 руб. 
Статус: ВЫПОЛНЕНО. Версия заказа v2.1.5.
Сайт: https://store.com/order/12345
"""
# Задачи:
# 1. Найти email и телефон
# 2. Найти номер заказа (#12345)
# 3. Найти цену (1,500.50 руб)
# 4. Найти версию заказа (v2.1.5)
email = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', complex_text)
phone = re.findall(r'\b(?:\+7-9\d{2}-\d{3}-\d{2}-\d{2}|\+7\d{10}|8\d{10})\b', complex_text)
order_number = re.findall(r'#\d+', complex_text)
price = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?\s?руб', complex_text)
order_version = re.findall(r'v\d+(?:\.\d+)+', complex_text)
print("Email:", email)
print("Телефон:", phone)
print("Номер заказа:", order_number)
print("Цена:", price)
print("Версия заказа:", order_version)
