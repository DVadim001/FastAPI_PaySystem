# Какой язык программирования
FROM python:latest

# Копируем наш проект внутри папки (Docker)
COPY . /paysystem

# Устанавливаем рабочую директорию в контейнере
WORKDIR /paysystem

# Скачтваем все библиотеки
RUN pip install -r requirements.txt
# в терминале pip freeze > requirements.txt

CMD ["uvicorn", "main:app", "--reload", "--host=0.0.0.0"]
