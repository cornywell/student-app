import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from werkzeug.exceptions import NotFound
from sqlalchemy.sql import func
from models import db, Student

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def Index():
    student_result = None
    if request.args.get("id"):
        student_result = Student.query.get(request.args.get("id"))
        if student_result == None:
            return NotFound(request)

    students_id_and_fullname = Student.query.with_entities(Student.id, Student.firstname, Student.lastname)
    return render_template("index.html", fullnames=students_id_and_fullname, result=student_result)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
