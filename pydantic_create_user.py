import uuid
from pydantic import BaseModel, EmailStr, Field, constr
from tools.fakers import fake


class UserBaseSchema(BaseModel):
    email: EmailStr = Field(default_factory=lambda:fake.email())
    last_name: constr(min_length=1, max_length=50) = Field(alias="lastName", default_factory=lambda: fake.last_name())
    first_name: constr(min_length=1, max_length=50) = Field(alias="firstName", default_factory=lambda: fake.first_name())
    middle_name: constr(min_length=1, max_length=50) = Field(alias="middleName", default_factory=lambda: fake.middle_name())

class UserSchema(UserBaseSchema):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))

class CreateUserRequestSchema(UserBaseSchema):
    password: constr(min_length=1, max_length=250) = Field(default_factory=lambda: fake.password())

class CreateUserResponseSchema(BaseModel):
    user: UserSchema

