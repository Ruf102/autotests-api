from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_user(request: CreateUserResponseSchema, response: GetUserResponseSchema):
    """
    Проверяет, что поля пользователя в ответе на получение (GetUserResponseSchema)
    соответствуют полям пользователя в ответе на создание (CreateUserResponseSchema).

    :param request: Ответ от запроса на создание пользователя (CreateUserResponseSchema).
    :param response: Ответ от запроса на получение пользователя (GetUserResponseSchema).
    :raise AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.id, request.user.id, "id")
    assert_equal(response.user.email, request.user.email, "email")
    assert_equal(response.user.last_name, request.user.last_name, "last_name")
    assert_equal(response.user.first_name, request.user.first_name, "first_name")
    assert_equal(response.user.middle_name, request.user.middle_name, "middle_name")


def assert_get_user_response(request: CreateUserResponseSchema, response: GetUserResponseSchema):
    """
    Проверяет, что ответ на получение пользователя (GetUserResponseSchema)
    соответствует данным, которые были использованы для его создания
    (представленным в CreateUserResponseSchema).

    Использует внутреннюю функцию assert_user для сравнения основных полей пользователя.

    :param request: Ответ от запроса на создание пользователя, содержащий ожидаемые данные пользователя.
    :param response: Фактический ответ от запроса на получение пользователя.
    :raise AssertionError: Если данные пользователя в ответах не совпадают.
    """
    assert_user(request, response)
