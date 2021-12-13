from blog import create_app, db
from blog.main.routes import admin_board, random_post_bot

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        admin_board(username='Маша Перепёлкина', email='masha_perepelkina@gmail.com',
                    password='12345', range_posts=(2, 17))
        random_post_bot(num_users=102)
        app.run(debug=True, port=8080, host='0.0.0.0')
