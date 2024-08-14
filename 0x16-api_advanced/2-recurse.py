#!/usr/bin/python3
"""
A recursive call to get all the topics from
the hot articles of a subreddit
"""
import requests


def recurse(subreddit, limit=100, hotlist=[], after=None):
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
    hotlist.extend([page['data']['title'] for page in pages])
    if after:
        return recurse(subreddit,
                       hotlist=hotlist,
                       after=after,
                       limit=limit)
    else:
        return hotlist
