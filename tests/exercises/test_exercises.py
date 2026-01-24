from http import HTTPStatus

import pytest

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExercisesRequestSchema, CreateExercisesResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.course import assert_update_course_response
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        request = CreateExercisesRequestSchema(course_id=function_course.response.course.id)
        response = exercises_client.create_exercise_api(request)
        response_date = CreateExercisesResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_date)
        validate_json_schema(response.json(), response_date.model_json_schema())

    def test_get_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        response_date = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_date, function_exercise.response)
        validate_json_schema(response.json(), response_date.model_json_schema())

    def test_update_exercise(self, exercises_client: ExercisesClient, function_exercise: ExerciseFixture):
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(function_exercise.response.exercise.id, request)
        response_date = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_date)

        validate_json_schema(response.json(), response_date.model_json_schema())

    def test_delete_exercise(
            self, exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture,
    ):
        response_delete_exercise = exercises_client.delete_exercise_api(function_exercise.response.exercise.id)
        assert_status_code(response_delete_exercise.status_code, HTTPStatus.OK)

        response_get_exercise = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        response_get_exercise_date = InternalErrorResponseSchema.model_validate_json(response_get_exercise.text)

        assert_status_code(response_get_exercise.status_code, HTTPStatus.NOT_FOUND)
        assert_exercise_not_found_response(response_get_exercise_date)
        validate_json_schema(response_get_exercise.json(), response_get_exercise_date.model_json_schema())







