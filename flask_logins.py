
from flask import *
from werkzeug.security import generate_password_hash, check_password_hash
from user_list import users
from forms import LoginForm
from pyjwt import generate_token
from flask_login import LoginManager, login_user
login_manager = LoginManager()
app = Flask(__name__)
flask_login_auth = Blueprint("flasklogin", __name__, static_folder="static", template_folder="templates")

@login_manager.user_loader
def load_user(user):
    return user in users

#Flask login authorization
@flask_login_auth.route('/login', methods=['GET', 'POST'])
@flask_login_auth.route('/', methods=['GET', 'POST'])
def login():
    if "user" in session:
        return redirect(url_for('user_dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = form.username.data in users
        if user:
            if check_password_hash(users[form.username.data], form.password.data):
                user = form.username.data 
                session.permanent = True
                session["user"] = user
                session["password"] = form.password.data
                user_data = {
                    form.username.data : form.password.data
                }
                token = generate_token(user_data)
                session["token"] = token
                flash('Logged in successfully.') 
                return redirect(url_for('user_dashboard'))
            else:
                flash('Please check your username and password and try again.')
                return redirect(url_for('flasklogin.login'))
    return render_template('login.html', form=form)
