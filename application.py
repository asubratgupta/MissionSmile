from flask import Flask, render_template, request, session
from flask_session import Session
import json

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
@app.route('/index/',  methods=["GET", "POST"])
def index():
    return render_template("home.html")

@app.route('/home/',  methods=["GET", "POST"])
def home():
    return render_template("home.html")

@app.route('/categories/',  methods=["GET", "POST"])
def categories():
    return render_template("categories.html")

@app.route('/profiles/',  methods=["GET", "POST"])
def profiles():
    return render_template("profiles.html")

@app.route('/faq/',  methods=["GET", "POST"])
def faq():
    return render_template("faq.html")

@app.route('/contact_us/',  methods=["GET", "POST"])
def contact_us():
    return render_template("contact_us.html")

@app.route('/sign_in/',  methods=["GET", "POST"])
def sign_in():
    return render_template("sign_in.html")

@app.route('/sign_up/',  methods=["GET", "POST"])
def sign_up():
    return render_template("sign_up.html")


# @app.route("/add_course/", methods=["GET", "POST"])
# def add_course():
#     if request.method == "POST":
#         data = request.form.to_dict()
#         print(data)
#     return render_template("add_course.html")
#
#
#
# @app.route("/find_learners/", methods=["GET", "POST"])
# def find_learners():
#     if request.method == "POST":
#         data = request.form.to_dict()
#         print(data)
#     return render_template("find_learners.html")
#
#
#
#
# @app.route("/search_course/", methods=["GET", "POST"])
# def search_course():
#     if request.method == "POST":
#         data = request.form.to_dict()
#         print(data)
#     return render_template("search_course.html")
