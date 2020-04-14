from flask import render_template, flash, redirect, request, url_for,Flask
from werkzeug.urls import url_parse
from app import app
from app.forms import *
from flask_login import current_user, login_user, logout_user, login_required
from app.models import *
import pyodbc, json
from app import db
import sqlite3
from feedgen.feed import FeedGenerator
from flask import make_response

# app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page=request.args.get('next')
        if not next_page or url_parse(next_page).netloc!='':
            next_page=url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/getdata')
@login_required
def getdata():
    connection = pyodbc.connect('Driver={SQL Server};Server=.;Database=rakmo;uid=root;pwd=root')  # Creating Cursor

    cursor = connection.cursor()
    cursor.execute("SELECT top 100 * FROM reviews")
    rows= cursor.fetchall()
    # s = "<table style='border:3px  red'>"
    # for row in cursor:
    #     s = s + "<tr border=2>"
    # for x in row:
    #     s = s + "<td>" + str(x) + "</td>"
    # s = s + "</tr>"
    # connection.close()
    #
    # return '<html>'+s+'</html>'

    # print()
    return str(rows)