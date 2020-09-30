#!/usr/bin/python3
""" Queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API and returns the number of
        subscribers (not active users, total subscribers) for a given
        subreddit. If an invalid subreddit is given, the function return 0.
    """

    user = {"User-Agent": "Javier"}
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit), headers=user)

    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0
