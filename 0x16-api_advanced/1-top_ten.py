#!/usr/bin/python3
"""
A python module that takes a subreddit name
and returns the top ten topics
"""
import requests


def top_ten(subreddit):
    """
    this function takes a subreddit and returns the title of
    the top ten posts
    """

    endpoint = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "ALXSE/C22 (by /u/jossy2580)"}
    params = {'limit': 10}

    re = requests.get(endpoint,
                      headers=headers,
                      params=params,
                      allow_redirects=False)

    if re.status_code != 200:
        print(None)
        return

    data = re.json()
    posts = data['data']['children']
    for post in posts:
        print("{}".format(post['data']['title']))
