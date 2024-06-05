#!/usr/bin/python3
"""Module that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Unfortunately I had to use a custom one'}
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    data = response.json().get('data')
    after = data.get('after')
    count += data.get('dist')
    for title in data.get('children'):
        hot_list.append(title.get('data').get('title'))
    if after:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
