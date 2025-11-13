import faker
import httpx
import faker
from tools.fakers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": faker.Faker().email(),
    "password": faker.Faker().password(),
    "lastName": faker.Faker().last_name(),
    "firstName": faker.Faker().first_name(),
    "middleName": faker.Faker().first_name()
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)


login_payload = {
  "email": create_user_payload['email'],
  "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

get_user_headers  = {
    "Authorization": f'Bearer {login_response_data["token"]["accessToken"]}'
}
user_response = httpx.get(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}", headers=get_user_headers )
get_user_response_data = user_response.json()
print('Get user data:', get_user_response_data)

assert create_user_response_data == get_user_response_data