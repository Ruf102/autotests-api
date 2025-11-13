import httpx

# Вводим данные для входа в систему
login_payload = {
    "email": "user@example.com",
    "password": "12345"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

headers = {
    "Authorization": f'Bearer {login_response_data["token"]["accessToken"]}'
}

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
me_response_data = me_response.json()

print("user info:", me_response_data)
print("Status Code:", me_response.status_code)
