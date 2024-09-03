from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def main_landing():
    return render_template('landing.html')

@main.route('/join')
def join():
    return render_template('join.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/contact')
def contact():
    return render_template('contact.html')

