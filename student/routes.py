from flask import Blueprint

student = Blueprint('student', __name__)

@student.route('/student')
def student_landing():
    return 'Student Landing'
