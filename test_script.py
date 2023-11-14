import requests

# Пример данных для POST-запроса
data = {"field_name_1": "example@email.com", "field_name_2": "+7 123 456 78 90"}

# URL API
api_url = "http://127.0.0.1:8000/get_form/"

# Отправка POST-запроса
response = requests.post(api_url, data=data)

# Проверка, содержит ли ответ данные перед декодированием JSON
if response.text:
    # Вывод ответа
    print(response.json())
else:
    print("Empty response")