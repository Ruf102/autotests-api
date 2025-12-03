

def test_user_me(private_users_client):
    response = private_users_client.get_user_me_api()


    print(response.json())