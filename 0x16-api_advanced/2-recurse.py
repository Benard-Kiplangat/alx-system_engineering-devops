#!/usr/bin/python3
"""A script that prints the titles of hot posts ofa given subreddit"""

import requests


def recurse(subreddit, host_list=[], after="null"):
    """ A function that prints the nuof titles of hot posts using recursion"""

    header = {'user-agent': '/u/benardkiplangat API python for ALX Learning'}
    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}'
    r = requests.get(url, allow_redirects=False, headers=header)
    if r.status_code != 200:
        return None
    posts = r.json().get("data").get("children")
    for post in posts:
        host_list.append(post["data"]["title"])

    after = r.json().get("data").get("title")

    if after is not None:
        return recurse(subreddit, host_list, after)
    return host_list
