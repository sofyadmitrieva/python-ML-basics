# Слайд 8 (задача 1)
# Создайте любой словарь из 5 объектов

order = {
    "order_id": 5521,
    "customer": "Ольга",
    "items": ["Пицца Маргарита", "Чай", "Тортик"],
    "delivery_time": "19:30",
    "address": "ул. Садовая, 14",
}

order = dict(
    order_id=5521,
    customer="Ольга",
    items=["Пицца Маргарита", "Чай", "Тортик"],
    delivery_time="19:30",
    address="ул. Садовая, 14",
)

order = dict(
    [
        ("order_id", 5521),
        ("customer", "Ольга"),
        ("items", ["Пицца Маргарита", "Чай", "Тортик"]),
        ("delivery_time", "19:30"),
        ("address", "ул. Садовая, 14"),
    ]
)

# Слайд 9 (задача 2)

value = order["order_id"]
value = order["customer"]
value = order["items"]
value = order["delivery_time"]
value = order["address"]
value = order["price"]  # KeyError
value = order.get("price")
print(value)  # None
value = order.get("price", "не указана")
print(value)  # не указана

# Слайд 10 (задача 3)

order["delivery_time"] = "20:00"  # было 19:30
order["status"] = "в пути"  # новое значение

# Слайд 11 (задача 4)
removed_status = order.pop("status")
del order["address"]

print("Удалённый статус:", removed_status)
print(order)
