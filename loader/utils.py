import json

from main.utils import load_file


def save_picture(picture):

    filename = picture.filename
    file_type = filename.split('.')[-1]
    correct_file_type = ['png', 'jpeg', 'jpg', 'bmp', 'svg']
    if file_type not in correct_file_type:
        return 'Неверный тип файла'
    picture.save(f'./uploads/images/{filename}')
    return f'uploads/images/{filename}'


def save_posts(posts):
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)


def add_post(post):
    posts = load_file()
    posts.append(post)
    save_posts(posts)

