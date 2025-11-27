import httpx
import faker

from tools.fakers import fake

# Заполнение тела запроса рандомными данными использую библиотеку faker
create_user_payload = {
    "email": fake.email(),
    "password": fake.password(),
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.middle_name()
}
# Выполнение запроса на создание пользователя
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# Получение токена авторизации
login_payload = {
  "email": create_user_payload['email'],
  "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

# Обновление пользователя
update_user_payload = {
    "email": fake.email(),
    "password": fake.password(),
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.middle_name()
}
client = httpx.Client(headers={"Authorization": f'Bearer {login_response_data["token"]["accessToken"]}'})
update_user_response = client.patch(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}", json=update_user_payload)

print(f"Update user data: {update_user_response.json()}")
print(f"Status code: {update_user_response.status_code}")