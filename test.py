import requests

# Публичная ссылка, которую выдали на Яндекс.Диске
public_url = "https://disk.yandex.ru/d/bhf2M8C557AFVw"

# Шаг 1. Получаем ссылку для скачивания
api_url = "https://cloud-api.yandex.net/v1/disk/public/resources/download"
params = {
    "public_key": public_url  # Публичная ссылка
}
response = requests.get(api_url, params=params)

# Если запрос успешен, извлекаем прямую ссылку из поля "href"
download_url = response.json()["href"]

# Шаг 2. Скачиваем файл по прямой ссылке
file_data = requests.get(download_url)

# Сохраняем содержимое в локальный архив 'my_archive.zip'
with open("my_archive.zip", "wb") as f:
    f.write(file_data.content)

print("Файл успешно скачан!")
