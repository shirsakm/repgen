from flask import Blueprint

faculty = Blueprint('faculty', __name__)

@faculty.route('/faculty')
def faculty_landing():
    return 'Faculty Landing'
