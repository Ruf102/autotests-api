import faker
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from tools.assertions.schema import validate_json_schema

faker = faker.Faker()

from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.user_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema

public_users_client = get_public_users_client()


create_user_request = CreateUserRequestSchema(
    email=faker.email(),
    password=faker.password(),
    last_name=faker.last_name(),
    first_name=faker.first_name(),
    middle_name=faker.first_name()
)

create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user_api(create_user_response.user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)




