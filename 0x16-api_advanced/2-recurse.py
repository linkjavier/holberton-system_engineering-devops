#!/usr/bin/python3
""" Queries the Reddit API - Recursive """
import requests


def recurse(subreddit, hot_list=[]):
    """ Recursive function that queries the Reddit API
        and returns a list containing the titles of all
        hot articles for a given subreddit. If no results
        are found for the given subreddit, the function should return None.
    """

    user = {"User-Agent": "Javier"}
    if len(hot_list) == 0:
        resp = requests.get("https://www.reddit.com/r/{}/hot.json?"
                            .format(subreddit), headers=user)
    else:
        resp = requests.get("https://www.reddit.com/r/{}/hot.json?after={}_{}"
                            .format((subreddit),
                                    hot_list[-1].get('kind'),
                                    hot_list[-1].get('data').get('id')),
                            headers=user)
    if resp.status_code == 200:
        if len(resp.json().get('data').get('children')) < 1:
            return hot_list
        else:
            hot_list.extend(resp.json().get('data').get('children'))
            return recurse(subreddit, hot_list)
    else:
        return None
