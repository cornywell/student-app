import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from werkzeug.exceptions import NotFound
from sqlalchemy.sql import func
from models import db, Student, get_avg_all_students
from forms import StudentForm

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "SUPER_SECRET_KEY"
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
    student_result = None
    if request.args.get("id"):
        student_result = Student.query.get_or_404(request.args.get("id"))
    students_id_and_fullname = Student.query.with_entities(Student.id, Student.firstname, Student.lastname)
    return render_template("index.html", fullnames=students_id_and_fullname, result=student_result, avg=get_avg_all_students(), form=StudentForm())


@app.route('/create/', methods=['POST'])
def create():
    form = StudentForm()
    if form.validate_on_submit():
        firstname = form.firstname.data
        lastname = form.lastname.data
        age = form.age.data
        avg_grade = form.avg_grade.data
    
        student = Student(firstname=firstname, lastname=lastname, age=age, avg_grade=avg_grade)
        db.session.add(student)
        db.session.commit()
    return redirect(url_for('index'))


@app.post('/<id>/delete/')
def delete(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
