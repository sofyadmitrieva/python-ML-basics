models_stats = {
    "bert-base": {
        "accuracy": 0.92,
        "f1_score": 0.91,
        "inference_time": 120,
        "size_mb": 440
    },
    "distilbert": {
        "accuracy": 0.89,
        "f1_score": 0.88,
        "inference_time": 65,
        "size_mb": 250
    },
    "roberta-large": {
        "accuracy": 0.94,
        "f1_score": 0.93,
        "inference_time": 210,
        "size_mb": 1600
    }
}

# модель с максимальной точностью
max_accuracy_model = max(models_stats.items(), key=lambda x: x[1]["accuracy"])
print(f"Модель с максимальной точностью: {max_accuracy_model[0]} (accuracy={max_accuracy_model[1]['accuracy']})")

# среднее время инференса по всем моделям
avg_inference_time = sum(model["inference_time"] for model in models_stats.values()) / len(models_stats)
print(f"Среднее время инференса: {avg_inference_time:.2f} мс")

# новый словарь только с accuracy и f1_score
metrics_only = {name: {"accuracy": data["accuracy"], "f1_score": data["f1_score"]} 
                for name, data in models_stats.items()}
print("Словарь с метриками:", metrics_only)

# добавление новой модели "albert-base"
models_stats["albert-base"] = {
    "accuracy": 0.87,
    "f1_score": 0.86,
    "inference_time": 55,
    "size_mb": 180
}
print("После добавления albert-base:", models_stats.keys())

# фильтрация моделей размером меньше 500 МБ
small_models = {name: data for name, data in models_stats.items() if data["size_mb"] < 500}
print("Модели < 500 МБ:", small_models.keys())