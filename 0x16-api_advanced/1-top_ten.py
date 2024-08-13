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
    headers = {"User-Agent": "Ubuntu/20.04.06 ALXSE (by /u/jossy2580)"}

    re = requests.get(endpoint, headers=headers, allow_redirects=False)

    if re.status_code != 200:
        print(None)
        return

    data = re.json()
    data_dict = data['data']['children']

    for i in range(10):
        print("{}".format(data_dict[i]['data']['title']))
    return
