from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation,Products, Size, Categories
from flask import Response, abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt
from sqlalchemy import extract
from sqlalchemy import func
# from fpdf import FPDF

main = Blueprint('main', __name__)


# index page
@main.route('/', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    if request.method == 'POST':
        User = db.session.query(Users).filter_by(Email=request.form['Email']).first()
        if User and bcrypt.check_password_hash(User.Pasword, request.form['Pasword']):
            login_user(User)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            return render_template('login.html')
    return render_template('login.html')


# index page
@main.route('/index', methods=['POST', 'GET'])
@login_required
def index():
    NumberProducts = db.session.query(Products).count()
    NumberofCategories = db.session.query(Categories).count()

    return render_template('index.html', NumberProducts = NumberProducts, NumberofCategories = NumberofCategories)

# logout route
@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))
