import pytest
from pydantic import BaseModel
from clients.exercises.exercises_client import ExercisesClient, get_exercise_client
from clients.exercises.exercises_schema import CreateExercisesRequestSchema, CreateExercisesResponseSchema
from fixtures.courses import function_course, CourseFixture
from fixtures.users import UserFixture

class ExerciseFixture(BaseModel):
    request: CreateExercisesRequestSchema
    response: CreateExercisesResponseSchema

@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercise_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(
        function_course: CourseFixture,
        exercises_client: ExercisesClient
) -> ExerciseFixture:
    request = CreateExercisesRequestSchema(
        course_id=function_course.response.course.id
    )
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
