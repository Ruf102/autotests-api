import pytest

@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Отправляем данные в сервис аналитики")

@pytest.fixture(scope="session")
def setting():
    print("[SESSION] Инициализируем настройки автотестов")

@pytest.fixture(scope="class")
def user():
    print("[CLASS] Создаем данные пользователя один раз на тестовый класс")

@pytest.fixture(scope="function")
def user_client():
    print("[FUNCTION] Создаем API клиент на каждый автотест")
    ...


class TestUserFlow:
    def test_user_can_login(self, setting, user_client, user):
        ...

    def test_user_can_create_course(self, setting, user_client, user):
        ...


class TestAccountFlow:
    def test_user_account(self, setting, user_client, user):
        ...