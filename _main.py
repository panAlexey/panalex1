from flask import Flask, url_for, request, render_template, redirect
from loginform import LoginForm
import json
# from requests import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/login2', methods=['GET', 'POST'])
def login2():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login2.html', title='Авторизация', form=form)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/index3')
def index3():
    user = "Ученик Яндекс.Лицея"
    return render_template('index3.html', title='Домашняя страница',
                           username=user)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route('/index2')
def index2():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея 2"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/students')
def students():
    return render_template('stufdents.html')


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)


if __name__ == '__main__':
    app.run()