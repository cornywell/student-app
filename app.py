import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# TODO: Restructure application, this needs to be in models.py
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    avg_grade = db.Column(db.Float)

    def __repr__(self):
        return f'<Student {self.firstname} {self.lastname}>'


@app.route('/', methods=['GET', 'POST'])
def Index():
    student_result = None
    if request.method == 'POST':
        student_result = Student.query.get(request.form['id'])
    students_id_and_fullname = Student.query.with_entities(Student.id, Student.firstname, Student.lastname)
    return render_template("index.html", fullnames=students_id_and_fullname, result=student_result)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
