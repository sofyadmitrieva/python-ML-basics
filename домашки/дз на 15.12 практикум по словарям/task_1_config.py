config = {
    "model_name": "bert-base-uncased",
    "batch_size": 32,
    "max_length": 128,
    "learning_rate": 2e-5,
    "epochs": 3,
    "labels": ["positive", "negative", "neutral"]
}

# получить значение learning_rate двумя способами
learning_rate1 = config["learning_rate"]
learning_rate2 = config.get("learning_rate")

print(f"learning_rate (через скобки): {learning_rate1}")
print(f"learning_rate (через get()): {learning_rate2}")

# добавить новый параметр "early_stopping": True
config["early_stopping"] = True
print(f"Добавлен параметр early_stopping: {config['early_stopping']}")
print()

# изменить batch_size на 64
config["batch_size"] = 64
print(f"Изменен batch_size: {config['batch_size']}")
print()

# пройтись по всем параметрам и вывести только числовые значения
print("Числовые параметры конфигурации:")
for key, value in config.items():
    if isinstance(value, (int, float)):
        print(f"   {key}: {value}")

# копия конфигурации для тестирования
test_config = config.copy()
test_config["batch_size"] = 8
test_config["epochs"] = 1

print("Исходная конфигурация:")
for key, value in config.items():
    print(f"   {key}: {value}")

print("\n Конфигурация для тестирования:")
for key, value in test_config.items():
    print(f"   {key}: {value}")