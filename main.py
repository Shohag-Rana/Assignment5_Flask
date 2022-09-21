from flask import *
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from flask_logins import flask_login_auth
from user_list import users
from pyjwt import decoded_token
import requests
from datetime import timedelta
app = Flask(__name__)
app.register_blueprint(flask_login_auth, url_prefix="/users")
app.config['SECRET_KEY'] = 'w3engineerslimited'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

# Basic authentication when we open window
auth = HTTPBasicAuth()


# verify basic authentication user is valid or not
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

# after basic authentication it renders login page directly
@app.route('/')
@auth.login_required
def index():
    return redirect(url_for('flasklogin.login'))


# User Dashboard and post data
@app.route("/post")
@app.route("/user/dashboard")
@auth.login_required
def user_dashboard():
    json_uri = requests.get("https://dummyjson.com/products")
    posts = (json_uri.json())['products']
    if "user" in session:
        user = session["user"]
        psw = session["password"]
        token = session["token"]
        return render_template("dashboard.html", posts=posts)
    else:
        return redirect(url_for('flasklogin.login'))


# Token based Authentication to show the post details
@app.route("/post/<id>", methods=['GET', 'POST'])
@auth.login_required
def posts(id):
    if request.method == 'POST':
        form_username = request.form['username']
        form_password = request.form['password']
        token_decode_data = decoded_token(session["token"])
        for x in token_decode_data:
            current_username = x
            current_user_password = token_decode_data[x]

        if form_username == current_username and form_password == current_user_password:
            json_uri = requests.get("https://dummyjson.com/products")
            id = int(id)-1
            post = (json_uri.json())['products'][id]
            if "user" in session:
                user = session["user"]
                flash('Token Authorized Successfull!!! Thank You')
                return render_template("post_details.html", user=user, post=post)
        else:
            flash(
                'User Token authentication is failed!!!! Enter current username and password')
            return redirect(url_for('user_dashboard'))
    else:
        return redirect(url_for('flasklogin.login'))



# user logout and remove from the session
@app.route("/user/logout")
@auth.login_required
def logout():
    session.pop("user", None)
    return redirect(url_for('flasklogin.login'))


#run the project
if __name__ == '__main__':
    app.run(debug=True)
