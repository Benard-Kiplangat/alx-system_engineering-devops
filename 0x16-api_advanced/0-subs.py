#!/usr/bin/python3
""" A script that checks the number of subscribers of a given subreddit"""

from requests import get
import requests
import json

def number_of_subscribers(subreddit):
    headers = {'user-agent': '/u/benardkiplangat API python for ALX Learning'}
    client = requests.session()
    client.headers = headers
    count = 0
    response = client.get('https://www.reddit.com/r/{}/about.json'.format(subreddit), allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    return (data.get("subscribers"))
