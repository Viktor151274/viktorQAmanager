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
    
#individual tasks
    def search_emoji_by_name(self, name):
        r2 = requests.get("https://api.github.com/emojis", params={"q":name})
        body = r2.json()

        return body
    