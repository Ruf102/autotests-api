import json

data = {
    "name": "Мария",
    "age": 25,
    'is_student': True
}

data_2 = '{"name": "Иван", "age": 30, "is_student": false}'

json_string_2 = json.loads(data_2)
print(json_string_2['age'], type(json_string_2))

json_string = json.dumps(data, indent=2, ensure_ascii=False)
print(json_string, type(json_string))


with open("json_example.json", "r", encoding="utf-8") as file:
    open_json_file = json.load(file)
    print(open_json_file, type(open_json_file))

with open("json_test.json", "w", encoding="utf-8") as file_json:
    json.dump(data, file_json, indent=2, ensure_ascii=False)