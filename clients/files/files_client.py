from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


# Добавили описание структуры файла
class File(TypedDict):
    """
    Описание структуры файла.
    """
    id: str
    url: str
    filename: str
    directory: str

class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str       # имя файла
    directory: str      # путь к директории, куда файл должен быть загружен,
    upload_file: str    # путь к файлу на локальной машине, который будет загружен

class CreateFileResponseDict(TypedDict):
    """
    Описание структуры ответа создания файла.
    """
    file: File


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """

    def get_files_api(self, file_id: str) -> Response:
        """
        Метод получения файла по идентификатору файла

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла по идентификатору

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request['upload_file'], 'rb')}
        )

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        """
        Метод отправляет запрос на добавление файла и извлекает JSON из ответа

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде JSON
        """
        response = self.create_file_api(request)
        return response.json()

def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию FilesClient.
    """
    return FilesClient(client=get_private_http_client(user))