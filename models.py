from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    avg_grade = db.Column(db.Float)

    def __repr__(self):
        return f'<Student {self.firstname} {self.lastname}>'


def get_avg_all_students():
    '''
    Calculates the average grade of all the students
    '''
    sum_of_avg_grades = db.session.query(func.sum(Student.avg_grade).label("total_avg_grade")).all()[0][0] # strange indexing to unpack SA query
    num_students = db.session.query(Student).count()
    return sum_of_avg_grades / num_students