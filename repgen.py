from flask import Flask

from admin.routes import admin
from faculty.routes import faculty
from student.routes import student
from main.routes import main


app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(admin)
app.register_blueprint(student)
app.register_blueprint(faculty)

if __name__ == '__main__':
    app.run(debug=True)
