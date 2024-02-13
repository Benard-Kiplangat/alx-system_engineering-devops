#!/usr/bin/python3
"""A script that prints the titles of hot posts ofa given subreddit"""

import requests
import json


def recurse(subreddit, host_list=[], after="null"):
    """ A function that prints the titles of hot posts of a given subreddit"""

    headers = {'user-agent': '/u/benardkiplangat API python for ALX Learning'}
    client = requests.session()
    client.headers = headers
    paramss = {"limit": "100", "after": after}
    url =  'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = client.get(url, allow_redirects=False, params=paramss)
    if r.status_code != 200:
        return None
    titles = r.json().get("data").get("children")
    if after is not None:
        host_list.append(titles[len(host_list)]["data"]["title"])
        recurse(subreddit, host_list, after)
    return host_list
