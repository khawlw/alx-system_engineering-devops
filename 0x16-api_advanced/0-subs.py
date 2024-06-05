#!/usr/bin/python3
"""Module that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """prints the number of subscribers for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Unfortunately I had to use a custom one'}
    req = requests.get(url, headers=headers).json()
    subs = req.get('data', {}).get('subscribers', 0)
    return subs
