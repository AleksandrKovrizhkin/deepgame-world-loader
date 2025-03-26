import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_world(text):
    prompt = f"""
Прочитай следующий текст и извлеки из него структуру игрового мира:

1. Краткое описание мира
2. Жанр и уровень технологий
3. Есть ли магия?
4. Названия и описание ключевых регионов
5. Фракции и их цели
6. Ключевые персонажи с краткими описаниями
7. Главный конфликт

Текст:
{text}

Ответ в формате JSON:
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']
