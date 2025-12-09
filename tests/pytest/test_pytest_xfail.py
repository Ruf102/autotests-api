import pytest

@pytest.mark.xfail(reason="Найден баг, тест падает с ошибокой")
def test_with_bug():
    assert False

@pytest.mark.xfail(reason="баг исправлен но тесте xfail")
def test_without_bug():
    ...

@pytest.mark.xfail(reason="Внешний сервис временно недоступен")
def test_external_service_is_unavailable():
    assert False