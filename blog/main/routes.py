
from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, current_user
from sqlalchemy import func

from blog import db, bcrypt
from blog.models import Post, User, Comment
from blog.user.utils import random_avatar, random_post_img, save_picture_post

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def home():
    return render_template('main/index.html', title='Главная')


def admin_board(username, email, password, range_posts):
    from mimesis import Text
    from random import randint

    text = Text('ru')

    user = User(username=username, email=email,
                password=bcrypt.generate_password_hash(password).decode('utf-8'))
    query_user = User.query.filter_by(username=user.username).first()
    if not query_user:
        db.session.add(user)
        user.image_file = random_avatar(user=user.username)
        db.session.commit()

        for i in range(randint(*range_posts)):
            post = Post(title=text.title(), content=text.text(quantity=randint(3, 7)),
                        image_post=random_post_img(user))
            db.session.add(post)
            post.image_post = save_picture_post(post.image_post, post, user)
            post.user_id = user.id
            db.session.commit()

            comment = Comment(username=user.username, body=text.title(), post_id=post.id)
            db.session.add(comment)
            db.session.commit()

    db.session.commit()


def random_post_bot(num_users):
    from mimesis import Text, Person
    from random import randint, choice
    person = Person('ru')
    text = Text('ru')
    all_users = User.query.all()
    print('Идёт заполнение блога пользователями и постами...')
    if not len(all_users) >= 100:
        for i in range(num_users):

            user = User(username=person.full_name(), email=person.email(),
                        password=bcrypt.generate_password_hash(person.password()).decode('utf-8'))
            query_user = User.query.filter_by(username=user.username).first()
            if not query_user:
                db.session.add(user)
                user.image_file = random_avatar(user=user.username)
                db.session.commit()

                for j in range(randint(0, 5)):
                    post = Post(title=text.title(), content=text.text(quantity=randint(3, 12)),
                                image_post=random_post_img(user))
                    db.session.add(post)
                    post.image_post = save_picture_post(post.image_post, post, user)
                    post.user_id = user.id
                    db.session.commit()

                    comment = Comment(username=user.username, body=text.title(), post_id=post.id)
                    db.session.add(comment)
                    all_users = User.query.all()
                    comment.post_id = choice(all_users).id
                    db.session.commit()
        print('Создание успешно завершено')
        db.session.commit()


@main.route('/blog', methods=['POST', 'GET'])
@login_required
def blog():
    all_posts = Post.query.all()
    all_users = User.query.all()
    post = Post.query.get(current_user.id)
    if post:
        page = request.args.get('page', 1, type=int)
        # posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=4)
        posts = Post.query.order_by(func.random()).paginate(page=page, per_page=10)
        image_file = url_for('static',
                             filename=f'profile_pics/{current_user.username}/{post.image_post}')

        return render_template('main/blog.html', title='Блог', posts=posts, image_file=image_file,
                               all_posts=all_posts, all_users=all_users)
    else:
        return render_template('main/blog.html', title='Блог', nothing='Постов пока нет', posts=all_posts)


@main.route('/html_page')
def html_page():
    return render_template('main/html_page.html')


@main.route('/css_page')
def css_page():
    return render_template('main/css_page.html')


@main.route('/js_page')
def js_page():
    return render_template('main/js_page.html')


@main.route('/python_page')
def python_page():
    return render_template('main/python_page.html')


@main.route('/flask_page')
def flask_page():
    return render_template('main/flask_page.html')


@main.route('/django_page')
def django_page():
    return render_template('main/django_page.html')
