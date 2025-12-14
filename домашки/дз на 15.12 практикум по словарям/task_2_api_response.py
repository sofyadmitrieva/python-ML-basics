# Обработка ответа от NLP-сервиса
api_response = {
    "text": "I really enjoyed the movie, the acting was amazing!",
    "sentiment": {"label": "positive", "score": 0.95, "confidence": "high"},
    "entities": [
        {"entity": "movie", "type": "ENTERTAINMENT", "confidence": 0.89},
        {"entity": "acting", "type": "SKILL", "confidence": 0.92},
    ],
    "language": "en",
    "processed_in": 0.45,
}

# оценка тональности (score)
sentiment_score = api_response["sentiment"]["score"]
print(f"Оценка тональности: {sentiment_score}")

# названия сущностей
entity_names = [entity["entity"] for entity in api_response["entities"]]
print(f"Названия сущностей: {entity_names}")

# сущность с максимальной уверенностью
max_confidence = max(api_response["entities"], key=lambda x: x["confidence"])
print(
    f"3. Сущность с максимальной уверенностью: '{max_confidence['entity']}' (confidence: {max_confidence['confidence']})"
)

# добавьте в поле ответа "model_version": "2.1.0"
api_response["model_version"] = "2.1.0"
print(f"model_version: {api_response}")

# отфильтруйте все поля, значения которых являются строками
filtered_response = {
    key: value for key, value in api_response.items() if not isinstance(value, str)
}

print(f"Отфильтрованный ответ: {filtered_response}")
