from flask import Blueprint, render_template, request, flash
#from .models import User
#from werkzeug.security import generate_password_hash, Check_password_hash
#from flask_bcrypt import Bcrypt
#from flask_migrate import Migrate
#from flask_login import (
#    UserMixin,
#    login_user,
#    LoginManager,
#    current_user,
#    logout_user,
#    login_required,
#)


auth = Blueprint('auth', __name__)


##signup page##
@auth.route('/signup', methods=['POST','GET'])
def sign_up():
    #create new user and get the info
    if request.method == 'POST':
        email = request.form['email']
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        tel = request.form.get('tel')
        

    #validate info entered
        if len(email) < 4:
            flash('must be a G-mail.com!', category = 'error')
        elif len(tel) != 10:
            flash('must start with 07--', category = 'error')
        elif password1 != password2 :
            flash('passwords don\'t match! ', category = 'error')
        elif len('password1') < 7:
            flash('Use a strong password!', category = 'error')

        else:
            flash('Account successfully created😁', category = 'success')
            # add user to DB

    return render_template('signup.html')


#user#
@auth.route('/login', methods=['POST','GET'])
def user():
    data = request.form
    print(data)
    return render_template('login.html')


#@auth.route('/logout')
# def logout():


#@auth.route('/signup')
#def signup():
