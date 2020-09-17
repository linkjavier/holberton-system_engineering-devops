#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def top_ten(subreddit):
    """ Function that queries the Reddit API and returns the number of
        subscribers (not active users, total subscribers) for a given
        subreddit. If an invalid subreddit is given, the function return 0.
    """

    user = {"User-Agent": "Javier"}
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit), headers=user)

    if response.status_code == 200:
        for child in response.json().get('data').get('children'):
            print(child.get('data').get('title'))
    else:
        print('None')
        return 0
