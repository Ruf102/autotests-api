import faker

from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict

faker = faker.Faker()

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=faker.email(),
    password=faker.password(),
    lastName=faker.last_name(),
    firstName=faker.first_name(),
    middleName=faker.first_name()
)

create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(authentication_user)

# Отправляем GET запрос на получение данных пользователя
get_user_response = private_users_client.get_user(create_user_response['user']['id'])
print('Get user data:', get_user_response)