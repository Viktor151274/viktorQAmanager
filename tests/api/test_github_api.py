import pytest

from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 58
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('viktorQAmanager_repo_not_exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_list_commits_on_pr_not_found(github_api):
    commits = github_api.list_commits_on_pull_request("Viktor151274", "viktorQAmanager", "Bad_number")
    assert commits["message"] == "Not Found"
    assert commits["status"] == "404"

@pytest.mark.api
def test_list_releases_found(github_api):
    releases = github_api.list_releases("Viktor151274", "viktorQAmanager")
    assert len(releases) >= 1
    assert releases[0]["tag_name"] == "v1.0.0"
    assert releases[0]["author"]["login"] == "Viktor151274"

@pytest.mark.api
def test_list_releases_not_found(github_api):
    releases = github_api.list_releases("Viktor151274", "viktor")
    assert releases["status"] == "404"

@pytest.mark.api
def test_valid_emoji(github_api):
    emoji_name = "ukraine"
    r = github_api.get_all_emojis()
    assert emoji_name in r