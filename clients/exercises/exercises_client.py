from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.users.private_users_client import get_private_users_client


class Exercise(TypedDict):
    """
    Описание структуры упражнения
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений в курсе.
    """
    courseId: str

class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CreateExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на создание упражнения.
    """
    exercise: Exercise

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение упражнений по номеру курса.
    """
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение упражнения.
    """
    exercise: Exercise

class UpdateExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на изменение упражнения.
    """
    exercise: Exercise



class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises.
    """

    def get_exercises_api(self, query: GetExercisesRequestDict) -> Response:
        """
        Метод получения списка упражнений в курсе.

        :param query: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод отправляет запрос на получение упражнения и извлекает JSON из ответа.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде JSON
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesRequestDict) -> GetExercisesResponseDict:
        """
        Метод отправляет запрос на получение всех упражнений в курсе и извлекает JSON из ответа.

        :param query: Идентификатор курса
        :return: Ответ от сервера в виде JSON
        """
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExercisesRequestDict) -> CreateExercisesResponseDict:
        """
        Метод отправляет запрос на создание упражнения и извлекает JSON из ответа.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде JSON
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExercisesResponseDict:
        """
        Метод отправляет запрос на изменение упражнения и извлекает JSON из ответа.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде JSON
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()



def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(get_private_http_client(user))