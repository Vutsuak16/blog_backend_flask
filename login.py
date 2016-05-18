from flask import Flask, Response, redirect, url_for, request, session, abort,render_template
from flask.ext.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user

app = Flask(__name__)

# config
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret_xxx'
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# silly user model
class User(UserMixin):

    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)


# create some users with ids 1 to 8
name=["kaustuv","arpit"]
passwd=["beckham","ronaldo"]

# some protected url
@app.route('/')
@login_required
def home():
    return Response("Hello World!")


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in name and password in passwd:
            if name.index(username)==passwd.index(password):
                id = name.index(username)
                user = User(id)
                login_user(user)
                return redirect(url_for('write_blog'))
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p>USERNAME</p>
            <p><input type=password name=password>
            <p>PASSWORD</p>
            <p><input type=submit value=Login>
        </form>
        ''')


# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


# callback to reload the user object
@login_manager.user_loader
def load_user(userid):
    return User(userid)

@app.route("/write_blog")
def write_blog():
    return render_template('new-blog.html')


if __name__ == "__main__":
    app.run()