import requests


def get_top_starred_repositories():
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'stars:>0',
        'sort': 'stars',
        'order': 'desc',
        'per_page': 100  # Ustawiamy ilość wyników na 50 na jednej stronie.
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        repositories = data['items']
        return repositories
    else:
        print(f"Nie udało się pobrać danych. Kod błędu: {response.status_code}")
        return None


if __name__ == "__main__":
    top_starred_repositories = get_top_starred_repositories()
    if top_starred_repositories:
        for repo in top_starred_repositories:
            print(f"Repozytorium: {repo['name']}, Gwiazdki: {repo['stargazers_count']}")