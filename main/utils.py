import json


import os


def load_file():
    posts = []
    with open(os.path.join('posts.json'), encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def searching_posts(string_):
    posts = []
    data = load_file()
    for post in data:
        if string_.lower() in post['content'].lower():
            posts.append(post)
    return posts
