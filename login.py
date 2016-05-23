from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
from flask.ext.login import LoginManager, UserMixin, \
    login_required, login_user, logout_user, session
import re
import os
import sqlite3 as sql
import time

app = Flask(__name__)

# config
app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)
UPLOAD_FOLDER = 'static/img/'


# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
from HTMLParser import HTMLParser


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


# silly user model
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        # self.name = "user" + str(id)
        # self.password = self.name + "_secret"

    def __repr__(self):
        pass
        # return "%d/%s/%s" % (self.id, self.name, self.password)


# create some users with ids 1 to 8
name = ["kaustuv", "arpit"]
passwd = ["beckham", "ronaldo"]


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
        session["username"] = username
        password = request.form['password']
        if username in name and password in passwd:
            if name.index(username) == passwd.index(password):
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


@app.route("/write_blog", methods=['GET', 'POST'])
@login_required
def write_blog():
    con = sql.connect('C:\Users\windows 7\Desktop\Blogs_time_being.db')
    if request.method == "GET":
        return render_template('simple_edit.html')
    else:

        title = request.form["title"]
        Content = request.form["content"]
        author = session["username"]
        option = request.form["option"]
        Date = time.strftime("%x")
        tags = request.form["tags"]
        file = request.files['pic']
        path=os.path.join(UPLOAD_FOLDER,file.filename)
        file.save(path)

        cur = con.cursor()

        # Content=re.sub("<p[^>]*>", "", Content)
        # Content=re.sub("</p[^>]*>", "", Content)
        #Content = strip_tags(Content)

        cur.execute("INSERT  INTO bloooogs (AUTHOR,DATE,TITLE,CONTENT,OPTION,TAGS,IMAGE_URL) VALUES (?,?,?,?,?,?,?)",
                    (author, Date, title, Content, option, tags, path))
        con.commit()

        print title
        print Date
        print author
        print Content
        print option
        print tags
        print path

        return redirect('/write_blog')


if __name__ == "__main__":
    app.run()
