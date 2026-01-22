from http import HTTPStatus

import pytest

from clients.coursrs.courses_client import CoursesClient
from clients.coursrs.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, GetCoursesQuerySchema, \
    GetCoursesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture, function_user
from tools.assertions.base import assert_status_code
from tools.assertions.course import assert_update_course_response, assert_course_path_get_match, \
    assert_get_courses_response
from tools.assertions.schema import validate_json_schema

@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_update_course(self, courses_client: CoursesClient, function_course: CourseFixture):
        request_update_course = UpdateCourseRequestSchema()
        request_update_course_data = courses_client.update_course_api(function_course.response.course.id, request_update_course)
        response_data = UpdateCourseResponseSchema.model_validate_json(request_update_course_data.text)

        assert_status_code(request_update_course_data.status_code, HTTPStatus.OK)
        assert_update_course_response(request_update_course, response_data)
        validate_json_schema(request_update_course_data.json(), response_data.model_json_schema())

        response_get_courses = courses_client.get_course(function_course.response.course.id)
        assert_course_path_get_match(response_get_courses, response_data)

    def test_get_courses(
            self,
            courses_client: CoursesClient,
            function_course: CourseFixture,
            function_user: UserFixture
    ):
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query)

        response_data = GetCoursesResponseSchema.model_validate_json(response.text)
        assert_status_code(response.status_code, HTTPStatus.OK)

        assert_get_courses_response(response_data, [function_course.response])

        validate_json_schema(response.json(), response_data.model_json_schema())




