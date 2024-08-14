#!/usr/bin/python3
"""
A recursive call to count all the occurence of th
words in the keywords list
"""
import re
import requests


def count_words(subreddit, word_list,
                limit=100, counts={}, after=None):
    """
    A recursive function that fetches the title of the
    hot articles of a subreddit
    """

    endpoint = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': limit}
    headers = {'User-Agent': 'ALXSE/C22 (by /u/jossyboy2580)'}

    if after:
        params['after'] = after

    res = requests.get(endpoint,
                       params=params,
                       headers=headers,
                       allow_redirects=False)

    if res.status_code != 200:
        return None
    res_dict = res.json()
    after = res_dict['data']['after']

    pages = res_dict['data']['children']
    titles = [page['data']['title'].lower() for page in pages]
    for word in word_list:
        for title in titles:
            how_many = re.findall(f'\s{word.lower()}\s', title)
            if not how_many:
                continue
            counts[word.lower()] = counts.get(word.lower(), 0) + len(how_many)
    if after:
        count_words(subreddit,
                    word_list,
                    counts=counts,
                    after=after,
                    limit=limit)
    print({key: counts[key] for key in sorted(counts)})
