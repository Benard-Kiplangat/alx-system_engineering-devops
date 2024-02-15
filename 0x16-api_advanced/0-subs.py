#!/usr/bin/python3
""" A script that checks the number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """ A function that checks the number of subscribers of a given subredit"""

    header = {
            'user-agent': '/u/benardkiplangat API python for ALX Learning'
            }
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 404:
        return 0
    data = r.json().get("data")
    return data.get("subscribers")
