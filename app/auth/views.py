from . import auth
from flask import render_template 

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/test')
def test():
    return 'Hello People'