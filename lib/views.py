from flask import render_template

from app import app
# from models import User

# from auth import auth


@app.route('/')
def homepage():
    return render_template('homepage.html')


# @app.route('/private/')
# def private_view():
#     user = auth.get_logged_in_user()
#     return render_template('welcome.html')
