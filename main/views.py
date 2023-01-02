from flask import Blueprint, render_template, request

import logging

from main.utils import searching_posts

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logging.basicConfig(filename='basic.log', level=logging.INFO)


@main_blueprint.route('/')
def main_page():
    """
    main page
    :return: main page form
    """
    return render_template("index.html")


@main_blueprint.get('/search')
def search_posts():
    """
    searching posts
    :return: founded posts on request
    """
    string_ = request.args.get('s')
    logging.info(f'Поиск: {string_}')
    posts, error = searching_posts(string_)

    if error:
        logging.info(f'Ошибка: {error}')
        return 'Ошибка'

    return render_template('post_list.html', string_=string_, posts=posts)


