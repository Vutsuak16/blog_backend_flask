from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
from flask.ext.login import LoginManager, UserMixin, login_required, login_user, logout_user, session
import sqlite3 as sql
import os
import time
from slacker import Slacker

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx'
)
UPLOAD_FOLDER = 'static/img/'


# config

# some protected url
@app.route('/')
# @login_required
def home():
    return Response("Hello World!")


@app.route("/echo", methods=["GET", "POST"])
def echo():
    return render_template('index.html')


# config


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


# somewhere in login
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
        file = request.files['pic']
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        cur = con.cursor()
        check = "published" in request.form
        if check:
            cur.execute("INSERT  INTO Prreview (AUTHOR,DATE,TITLE,CONTENT,OPTION,IMAGE_URL) VALUES (?,?,?,?,?,?)",
                        (author, Date, title, Content, option, path))
            con.commit()
            return redirect('/preview')
        else:
            cur.execute("INSERT  INTO blOgsS (AUTHOR,DATE,TITLE,CONTENT,OPTION,IMAGE_URL) VALUES (?,?,?,?,?,?)",
                        (author, Date, title, Content, option, path))
            con.commit()
            return redirect('/write_blog')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template('contact.html')
    else:
        con = sql.connect('C:\Users\windows 7\Desktop\echo_crew_launch.db')
        slack = Slacker('xoxp-17745507104-43143624772-44861627974-c398e9ece2')
        slack.chat.post_message('#random', 'Hello interns this is James Bond !!')

        name = request.form["your-name"]
        email = request.form["your-email"]
        subject = request.form["your-subject"]
        message = request.form["your-message"]
        cur = con.cursor()
        cur.execute("INSERT  INTO visitors (NAME,EMAIL,SUBJECT,MESSAGE) VALUES (?,?,?,?)",
                    (name, email, subject, message))
        con.commit()
        return redirect('/contact')


@app.route("/blog", methods=["GET", "POST"])
def blog():
    con = sql.connect('C:\Users\windows 7\Desktop\Blogs_time_being.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM blOgsS")
    p = cur.fetchall()
    return render_template('blog.html', posts=p)


@app.route("/preview", methods=["GET", "POST"])
def preview():
    con = sql.connect('C:\Users\windows 7\Desktop\Blogs_time_being.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Prreview WHERE ID=(SELECT MAX(ID) FROM Prreview)")
    p = cur.fetchall()
    return render_template('preview.html', posts=p[0])


@app.route("/full_blog/<int:post_id>", methods=["GET", "POST"])
def full_blog(post_id):
    con = sql.connect('C:\Users\windows 7\Desktop\Blogs_time_being.db')
    cur = con.cursor()
    cur.execute("select * from blOgsS WHERE ID=%d" % post_id)
    p = cur.fetchall()
    return render_template('full_blog.html', posts=p[0])


@app.route("/options/<string:post_options>", methods=["GET", "POST"])
def options(post_options):
    con = sql.connect('C:\Users\windows 7\Desktop\Blogs_time_being.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM blOgsS WHERE OPTION LIKE ?', ('%' + post_options + '%',))
    p = cur.fetchall()
    return render_template('post_options.html', posts=p)


if __name__ == "__main__":
    app.run(debug=True)
