import logging

from flask import Blueprint, render_template, request

from loader.utils import save_picture, add_post

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.get('/post')
def load_post_page():
    """

    :return: add posts page form
    """
    return render_template('post_form.html')


@loader_blueprint.post('/post')
def load_post():
    """
    loading post with picture and content to the server
    :return: form with loaded picture and with text
    """
    picture = request.files.get('picture')
    content = request.form.get('content')
    if not picture or not content:
        return "Не все поля заполнены"

    picture_path = save_picture(picture)
    if not picture_path:
        logging.info('Загружено не изображение')
        return 'Загружено не изображение'

    new_post = {
        "pic": picture_path,
        "content": content
    }
    add_post(new_post)

    return render_template('post_uploaded.html', picture_path=picture_path, content=content)
