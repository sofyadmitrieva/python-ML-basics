pipeline_config = {
    "steps": {
        "tokenization": {"enabled": True, "method": "word"},
        "stopwords": {"enabled": True, "language": "english", "custom_words": []},
        "stemming": {"enabled": False, "algorithm": "porter"},
        "normalization": {"enabled": True, "lowercase": True, "remove_punct": True},
    },
    "input_encoding": "utf-8",
    "output_format": "tokens",
}

# включите stemming, установив "enabled": True
pipeline_config["steps"]["stemming"]["enabled"] = True
print(f"Stemming включен: {pipeline_config['steps']['stemming']['enabled']}")

# добавьте "numbers" в custom_words для стоп-слов
pipeline_config["steps"]["stopwords"]["custom_words"].append("numbers")
print(
    f"Custom_words для стоп-слов: {pipeline_config['steps']['stopwords']['custom_words']}"
)

# получите список всех включенных шагов пайплайна
enabled_steps = []
for step_name, step_config in pipeline_config["steps"].items():
    if step_config.get("enabled"):
        enabled_steps.append(step_name)

print(f"Включенные шаги пайплайна: {enabled_steps}")

# измените output_format на "vectors"
pipeline_config["output_format"] = "vectors"
print(f"Новый output_format: {pipeline_config['output_format']}")

# создайте упрощенную конфигурацию только с включенными шагами
simplified_config = {
    "steps": {},
    "input_encoding": pipeline_config["input_encoding"],
    "output_format": pipeline_config["output_format"],
}

for step_name, step_config in pipeline_config["steps"].items():
    if step_config.get("enabled"):
        simplified_config["steps"][step_name] = step_config.copy()

print(f"Упрощенная конфигурация:")
print(simplified_config)

print("\nФинальная полная конфигурация:")
print(pipeline_config)
