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
