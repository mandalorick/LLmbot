# User Chat with Ollama
Необходимы следующие зависимости  
```
pip install litellm
pip install aiogram
pip install python-docx
```

---
После создания класса есть 2 метода
Все переписки пользователей сохраняются

## Методы
1) `add_question` - Добавляет вопрос в переписку с lm и возращает ответ  
2) `clear_chat_user` - Очищает чат юзера, принимает в себя особые параметры  
    2.1 `clear_chat_user(number=0)` - Очищает по номеру в списке включая ответ ии  
    2.2 `clear_chat_user(question="")` - Очищает конкрентный вопрос пользователя включая ответ ии  

## Пример использования
```python
matve = User_chat_Ollama()  # Создаем объект класса

matve.add_question("Сколько время?")
matve.add_question("Сколько время в мск")

matve.clear_chat_user(question="Сколько время в мск")  # Удаление по вопросу
matve.clear_chat_user(number=0)  # Удаление по индексу
matve.clear_chat_user()  # Полная очистка

print(matve)  # Вывод всей истории чата
```

