#!/usr/bin/python3
"""Implement count_words function"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
        queries the Reddit API, parses the title of all hot articles,
        and prints a sorted count of given keywords
    """
    if not count_dict:
        count_dict = {key.lower(): 0 for key in word_list}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'limit': 100, 'after': after}
    headers = {'User-Agent': 'custom user-agent'}

    response = requests.get(url,
                            params=params,
                            headers=headers,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print()
        return
    data = response.json().get('data', {})
    for post in data.get('children', []):
        title = post.get('data', {}).get('title', '').lower().split()
        for key in count_dict.keys():
            if key in title:
                times = len([t for t in title if t == key.lower()])
                count_dict[key] += times
    if data.get('after'):
        return count_words(subreddit, word_list, data.get('after'), count_dict)
    else:
        if len(word_list) > len(count_dict.keys()):
            temp_dict = count_dict.copy()
            for word in word_list:
                word_in_lowecase = word.lower()
                if word not in count_dict and word_in_lowecase in count_dict:
                    count_dict[word_in_lowecase] += temp_dict[word_in_lowecase]
        count_dict = dict(sorted(count_dict.items(),
                                 key=lambda item: (item[1],
                                                   item[0].lower()),
                                 reverse=True))
        [print('{}: {}'.format(key, value))
         for key, value in count_dict.items() if value > 0]
