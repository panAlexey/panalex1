from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField("email / login", validators=[DataRequired()])
    # surname = StringField('Фамилия', validators=[DataRequired()])
    # name = StringField('Имя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    # password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    # age = StringField('Ваш возраст', validators=[DataRequired()])
    # position = StringField('Должность', validators=[DataRequired()])
    # speciality = StringField('Специальность', validators=[DataRequired()])
    # address = StringField('Адрес', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Зарегистрироваться')