import requests

def get_repository_info(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "name": data["name"],
        "description": data["description"],
        "language": data["language"],
        "stars": data["stargazers_count"]
    }
def extract_repo_info(github_url):

    parts = github_url.rstrip("/").split("/")

    owner = parts[-2]
    repo = parts[-1]

    return owner, repo