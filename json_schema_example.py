from jsonschema import validate, ValidationError

# Пример схемы
schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "number" }
  },
  "required": ["name"]
}

json = {
    "name": "Alisa",
    "age": 25
}

try:
    validate(instance=json, schema=schema)
    print("JSON соответствует схеме")
except ValidationError as e:
    print(f"Ошибка валидации {e}")