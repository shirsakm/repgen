from flask import render_template
from markupsafe import escape
from . import routes


@routes.route('/join', defaults={'type': None})
@routes.route('/join/<type>')
def join(type):
    if type is None:
        return render_template('signup.html')

    return render_template('signup-{}.html'.format(escape(type)))


@routes.route('/login/<type>')
def login(type):
    return render_template('login-{}.html'.format(escape(type)))
