from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    name = StringField('Имя')
    surname = StringField('Второе имя')
    email = StringField('Email')
    age = IntegerField('Возраст')
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Пароль повторить')
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')