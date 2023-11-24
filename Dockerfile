# Используйте официальный образ Python как базовый
FROM python:3.9

# Установите рабочий каталог в контейнере
WORKDIR /usr/src/app

# Установите переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Установите зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте проект в контейнер
COPY . .

# Выполните миграции и сбор статических файлов

RUN python manage.py migrate


# Укажите команду для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
