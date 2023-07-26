import requests


# Performing the API call (request) and keeping the received repsonse

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd/github.v3+json'}
r = requests.get(url, headers)
print(f'Status code: {r.status_code}')

# Placing the received response in the dict variable
response_dict = r.json()

# Processing the results
print(response_dict.keys())
print(response_dict['incomplete_results'])

print(f"Total number of repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Number of returned repositories: {len(repo_dicts)}")

# Analyzing the first repository
repo_dict = repo_dicts[0]
print(f"Keys: {len(repo_dict)}")
print(repo_dict.keys())

print('Selected information about repositories:\n')
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created on: {repo_dict['created_at']}")
    print(f"Updated on: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
