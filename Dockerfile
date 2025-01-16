FROM python:3.13-slim

# Встановимо робочу директорію всередині контейнера
WORKDIR /app

# Скопіюємо інші файли в робочу директорію контейнера
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Позначимо порт, де працює застосунок всередині контейнера
EXPOSE 3000

COPY . .

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["python", "main.py"]