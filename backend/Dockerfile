# Используем официальный образ Python в качестве базового образа
FROM python
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app
# Копируем файл requirements.txt внутрь контейнера
COPY req.txt ./
# Устанавливаем зависимости, описанные в файле requirements.txt
RUN pip install -r req.txt