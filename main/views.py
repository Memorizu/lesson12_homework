from flask import Blueprint, render_template, request

from main.utils import searching_posts

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template("index.html")


@main_blueprint.get('/search')
def search_posts():
    string_ = request.args.get('s')
    posts = searching_posts(string_)

    return render_template('post_list.html', string_=string_, posts=posts)


