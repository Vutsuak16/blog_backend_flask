from flask import Flask, Response, redirect, url_for, request, session, abort,render_template
from flask.ext.login import LoginManager, UserMixin, \
                                login_required, login_user, logout_user

app = Flask(__name__)

# config

# some protected url
@app.route('/')
#@login_required
def home():
    return Response("Hello World!")


# somewhere to login
@app.route("/blog", methods=["GET", "POST"])
def blog():
        return render_template('index.html')



# somewhere to logout
@app.route("/about")
def about():
    return render_template('about.html')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


# callback to reload the user object

@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)