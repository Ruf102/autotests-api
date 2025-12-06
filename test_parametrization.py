import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("x, y", [(1, 1), (2, 2), (3, 3)])
def test_numbers(x, y):
    assert x == y


@pytest.mark.parametrize("os", ["mac", "linux", "windows"])
@pytest.mark.parametrize("host", ["dev", "test", "hf", "prod"])
def test_hosts(os: str, host: str):
    assert len(os + host) > 0

@pytest.fixture(params=["dev", "test", "hf", "prod"])
def host(request: SubRequest) -> str:
    return request.param


def test_host(host: str):
    print(f"Running host test: {host}")


import pytest

users = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}


@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identification(phone_number):
    pass

