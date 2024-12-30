import requests

class GitHub:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    
    def list_commits_on_pull_request(self, owner, repository, pull_number):
        address = f"https://api.github.com/repos/{owner}/{repository}/pulls/{pull_number}/commits"
        r = requests.get(address)
        body = r.json()

        return body
    
    def list_releases(self, owner, repository):
        address = f"https://api.github.com/repos/{owner}/{repository}/releases"
        r = requests.get(address)
        body = r.json()

        return body