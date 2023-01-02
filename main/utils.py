import json


import os
from json import JSONDecodeError


def load_file():
    """
    convering json file to list
    :return: posts list
    """
    try:
        with open(os.path.join('posts.json'), encoding='utf-8') as file:
            posts = json.load(file)
    except JSONDecodeError:
        return posts, 'Ошибка получение данных из JSON'
    return posts, None


def searching_posts(string_):
    """
    search post in posts
    :param string_: str
    :return: posts list on request
    """
    posts = []
    data, error = load_file()
    for post in data:
        if string_.lower() in post['content'].lower():
            posts.append(post)
    return posts, error
