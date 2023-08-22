from operator import itemgetter
import requests
import json


# Performing the API call (request) and keeping the received repsonse
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Processing information about every article
submission_ids = r.json()
readable_file = 'data/readable_hn_data_2.json'
with open(readable_file, 'w') as f:
    json.dump(submission_ids, f, indent=4)
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Prepare separate API request for each article
    url = f'https://hacker-news.firebaseio.com/v0/{submission_id}.json'
    r = requests.get(url)
    print(f'id: {submission_id}\tstatus: {r.status_code}')
    response_dict = r.json()
    readable_file = 'data/readable_hn_data_3.json'
    with open(readable_file, 'w') as f:
        json.dump(response_dict, f, indent=4)

    # Create dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f'http://news.ycombinator.com/item?id={submission_id}',
        'comments': response_dict['descendants'],
    }

    submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

    for submission_dict in submission_dicts:
        print(f"\nArticle title: {submission_dict['title']}")
        print(f"\nLink to discussion: {submission_dict['hn_link']}")
        print(f"\nTotal amount of comments: {submission_dict['comments']}")