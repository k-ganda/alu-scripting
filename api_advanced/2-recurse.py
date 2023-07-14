#!/usr/bin/python3
"""Recurse"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """"
    Reddit sends an after property in the response.
    Keep retrieving comments until after is null.
    """
    url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}
    param = {'after': after}
    response = requests.get(url, headers=header, params=param)

    if response.status_code != 200:
        data = response.json().get('data')
        if data is not None:
            children = data.get('children')
            if children is not None:
                for child in children:
                    hot_list.append(child.get('data').get('title'))
                after = data.get('after')
                if after is not None:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
        else:
            return hot_list
    else:
        return None
