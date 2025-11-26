from pydantic import BaseModel, ConfigDict, Field


class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений в курсе.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")

class CreateExercisesRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CreateExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на создание упражнения.
    """
    exercise: ExerciseSchema

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение упражнений по номеру курса.
    """
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на получение упражнения.
    """
    exercise: ExerciseSchema

class UpdateExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа на изменение упражнения.
    """
    exercise: ExerciseSchema