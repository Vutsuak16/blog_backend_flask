from flask import Flask, Response, redirect, url_for, request, session, abort, render_template
from flask.ext.login import LoginManager, UserMixin, \
    login_required, login_user, logout_user
import sqlite3 as sql

app = Flask(__name__)


# config

# some protected url
@app.route('/')
# @login_required
def home():
    return Response("Hello World!")


@app.route("/blog", methods=["GET", "POST"])
def blog():
    con = sql.connect('C:\Users\windows 7\Desktop\Blogs_time_being.db')
    cur=con.cursor()
    cur.execute("select * from blOOgs")
    p=cur.fetchall()
    return render_template('index.html',posts=p)


@app.route("/full_blog/<int:post_id>", methods=["GET", "POST"])
def full_blog(post_id):
    con = sql.connect('C:\Users\windows 7\Desktop\Blogs_time_being.db')
    cur=con.cursor()
    cur.execute("select * from blOOgs WHERE ID=%d"%post_id)
    p=cur.fetchall()
    print request.data
    return render_template('full_blog.html',posts=p[0])




@app.route("/about")
def about():
    return render_template('about.html')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


# callback to reload the user object

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template('contact.html')
    else:
        con = sql.connect('C:\Users\windows 7\Desktop\contacts_ahmad.db')

        name = request.form["your-name"]
        email = request.form["your-email"]
        subject = request.form["your-subject"]
        message = request.form["your-message"]

        cur = con.cursor()
        cur.execute("INSERT  INTO info (NAME,EMAIL,SUBJECT,MESSAGE) VALUES (?,?,?,?)", (name, email, subject, message))

        con.commit()
        msg = "recorded successfully"
        print msg

        return redirect('/contact')


if __name__ == "__main__":
    app.run(debug=True)
