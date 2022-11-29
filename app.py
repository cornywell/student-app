import os
from flask import Flask, render_template, request, redirect, url_for
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
def index():
    student_result = None
    if request.args.get("id"):
        student_result = Student.query.get_or_404(request.args.get("id"))
    students_id_and_fullname = Student.query.with_entities(Student.id, Student.firstname, Student.lastname)
    return render_template("index.html", fullnames=students_id_and_fullname, result=student_result)


@app.post('/<id>/delete/')
def delete(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
