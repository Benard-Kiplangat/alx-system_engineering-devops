#!/usr/bin/python3
""" A script that checks the number of subscribers of a given subreddit"""

import requests
import json


def number_of_subscribers(subreddit):
    """ A function that checks the number of subscribers of a given subredit"""

    header = {'user-agent': '/u/benardkiplangat API python for ALX Learning'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, allow_redirects=False, headers=header)
    if r.status_code != 200:
        return 0
    data = r.json().get("data")
    return (data.get("subscribers"))


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        num_subscribers = number_of_subscribers(subreddit)
        print(num_subscribers)
