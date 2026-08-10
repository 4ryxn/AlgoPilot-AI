import requests

def fetch_github(username: str):
    headers = {"Accept": "application/vnd.github+json"}
    user = requests.get(
        f"https://api.github.com/users/{username}", headers=headers, timeout=10
    )
    user.raise_for_status()
    repos = requests.get(
        f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated",
        headers=headers, timeout=10
    )
    repos.raise_for_status()
    u = user.json()
    return {
        "login": u.get("login"),
        "name": u.get("name"),
        "avatar_url": u.get("avatar_url"),
        "bio": u.get("bio"),
        "public_repos": u.get("public_repos", 0),
        "followers": u.get("followers", 0),
        "following": u.get("following", 0),
        "html_url": u.get("html_url"),
        "repositories": [
            {
                "name": x.get("name"),
                "stars": x.get("stargazers_count", 0),
                "language": x.get("language"),
                "url": x.get("html_url"),
            }
            for x in repos.json()[:10]
        ],
    }
