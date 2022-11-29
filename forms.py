from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField
from wtforms.validators import DataRequired, NumberRange

class StudentForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    age = IntegerField('age', validators=[DataRequired(), NumberRange(min=0, max=20)])
    avg_grade = DecimalField('avg_grade', validators=[DataRequired(), NumberRange(min=0, max=100)])
