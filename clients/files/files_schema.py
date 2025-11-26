from pydantic import BaseModel, HttpUrl

class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str

class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str       # имя файла
    directory: str      # путь к директории, куда файл должен быть загружен,
    upload_file: str    # путь к файлу на локальной машине, который будет загружен

class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema