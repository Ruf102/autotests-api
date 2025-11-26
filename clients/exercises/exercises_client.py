from httpx import Response
from typing import TypedDict
from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesRequestSchema, CreateExercisesRequestSchema, \
    UpdateExerciseRequestSchema, GetExerciseResponseSchema, GetExercisesResponseSchema, CreateExercisesResponseSchema, \
    UpdateExercisesResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises.
    """

    def get_exercises_api(self, query: GetExercisesRequestSchema) -> Response:
        """
        Метод получения списка упражнений в курсе.

        :param query: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def create_exercise_api(self, request: CreateExercisesRequestSchema) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод отправляет запрос на получение упражнения и извлекает JSON из ответа.

        :param exercise_id: Идентификатор упражнения.
        :return: Экземпляр модели GetExerciseResponseSchema
        """
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesRequestSchema) -> GetExercisesResponseSchema:
        """
        Метод отправляет запрос на получение всех упражнений в курсе и извлекает JSON из ответа.

        :param query: Идентификатор курса
        :return: Экземпляр модели GetExercisesResponseSchema
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExercisesRequestSchema) -> CreateExercisesResponseSchema:
        """
        Метод отправляет запрос на создание упражнения и извлекает JSON из ответа.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Экземпляр модели CreateExercisesResponseSchema
        """
        response = self.create_exercise_api(request)
        return CreateExercisesResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExercisesResponseSchema:
        """
        Метод отправляет запрос на изменение упражнения и извлекает JSON из ответа.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Экземпляр модели UpdateExercisesResponseSchema
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExercisesResponseSchema.model_validate_json(response.text)


def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(get_private_http_client(user))