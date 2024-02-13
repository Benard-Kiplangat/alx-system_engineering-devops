#!/usr/bin/python3
"""A script that prints the titles of top ten hot posts ofa given subreddit"""

import requests
import json


def top_ten(subreddit):
    """ A function that prints the titles of top ten hot posts"""

    header = {'user-agent': '/u/benardkiplangat API python for ALX Learning'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, allow_redirects=False, headers=header)
    if r.status_code != 200:
        return (print("None"))
    titles = r.json().get("data").get("children")
    for title in titles[:10]:
        print(title["data"]["title"])
    return 0


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        titles = top_ten(subreddit)
