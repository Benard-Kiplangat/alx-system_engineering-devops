#!/usr/bin/python3
"""A script that prints the titles of top ten hot posts ofa given subreddit"""

import requests
import json


def top_ten(subreddit):
    """ A function that prints the titles of top ten hot posts"""

    headers = {'user-agent': '/u/benardkiplangat API python for ALX Learning'}
    client = requests.session()
    client.headers = headers
    count = 0
    r = client.get('https://www.reddit.com/r/{}/hot.json'.format(subreddit),
                   allow_redirects=False)
    if r.status_code != 200:
        return (print("None"))
    titles = r.json().get("data").get("children")
    for title in titles[:10]:
        print(title["data"]["title"])
    return 0
