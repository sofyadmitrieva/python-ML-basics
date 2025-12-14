import json

# конфигурация из json-файла
with open('nlp_service_config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

print("Исходная конфигурация:")
print(json.dumps(config, indent=2, ensure_ascii=False))

# добавьте новую модель для "summarization" с соответствующими параметрами
config["models"]["summarization"] = {
    "path": "/models/summarization",
    "max_input_length": 1024,
    "supported_languages": ["en", "es"]
}

# увеличьте rate_limit на 50%
config["rate_limit"] = int(config["rate_limit"] * 1.5)

# добавьте русский язык ("ru") в поддерживаемые языки для модели sentiment
config["models"]["sentiment"]["supported_languages"].append("ru")

# создайте отдельный словарь только с настройками сервера
server_config = config["server"].copy()

print("\nНастройки сервера (отдельный словарь):")
print(json.dumps(server_config, indent=2, ensure_ascii=False))

# сохраните обновленную конфигурацию в новый файл nlp_service_config_updated.json
with open('nlp_service_config_updated.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2, ensure_ascii=False)
