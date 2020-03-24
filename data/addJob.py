from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class AddForJob(FlaskForm):
    job = StringField("Работа ", validators=[DataRequired()])
    # surname = StringField('Фамилия', validators=[DataRequired()])
    # name = StringField('Имя', validators=[DataRequired()])
    team_leader = IntegerField('id Лидера команды', validators=[DataRequired()])
    work_size = IntegerField('Время на выполнение', validators=[DataRequired()])
    collaborators = StringField('id соучастников', validators=[DataRequired()])
    # password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    # age = StringField('Ваш возраст', validators=[DataRequired()])
    # position = StringField('Должность', validators=[DataRequired()])
    # speciality = StringField('Специальность', validators=[DataRequired()])
    # address = StringField('Адрес', validators=[DataRequired()])
    is_finished = BooleanField('Работа выполнена')
    submit = SubmitField('Принять')