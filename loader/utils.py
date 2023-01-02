import json

from main.utils import load_file


def save_picture(picture):
    """
    Save picture to "uploads" directory
    :param picture: file "picture"
    :return: path to picture
    """
    filename = picture.filename
    file_type = filename.split('.')[-1]
    correct_file_type = ['png', 'jpeg', 'jpg', 'bmp', 'svg', 'avif']
    if file_type not in correct_file_type:
        return 'Неверный тип файла'
    picture.save(f'./uploads/images/{filename}')
    return f'uploads/images/{filename}'


def save_posts(posts):
    """
    save post to json file
    :param posts: list
    :return: json file with new post
    """
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)


def add_post(post):
    """
    add new post
    :param post:
    :return:
    """
    posts, error = load_file()
    posts.append(post)
    save_posts(posts)

