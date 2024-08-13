#!/usr/bin/python3
"""
A module containing a function that uses the Reddit API
to get the number of subscribers for a given sub-reddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function takes in a subreddit and returns the total
    number of subscribers it has (Not active users!)
    """

    endpoint = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'Ubuntu/20.04 ALXSE /u/jossyboy2580'}

    response = requests.get(
                            endpoint,
                            headers=header,
                            allow_redirects=False
                            )
    if response.status_code > 399:
        return 0
    return response.json()['data'].get('subscribers', 0)
