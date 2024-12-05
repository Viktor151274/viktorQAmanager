import pytest
from modules.api.clients.github import Github


@pytest.mark.api
def test_user_exists():
    api = Github()
    user = api.get_user_defunkt()
    assert user['login'] == 'defunkt'
