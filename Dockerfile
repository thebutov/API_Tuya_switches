# Используем базовый образ Python
FROM python:3.10

# Установка необходимых зависимостей
RUN pip install --upgrade pip
RUN pip install datetime flask requests telebot tuyacloud python-dotenv

# Копирование исходного кода в рабочую директорию контейнера
COPY . /

# Установка рабочей директории
WORKDIR /app

# Определение переменной окружения для Flask
ENV FLASK_APP=main.py

# Экспозиция порта
EXPOSE 5000

# Запуск приложения Flask
# RUN echo "Building the Docker image..."
#
# RUN echo $(pwd)
# RUN echo $(ls)
# CMD ["flask", "run", "--host=0.0.0.0"]
#

