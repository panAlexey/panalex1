# app.py
from flask import Flask, request, jsonify, render_template, redirect, make_response
from data import db_session
from data.animals import Animals
from data.plants import Plants
from data.users import User
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from loginform import LoginForm
# from waitress import serve # если используем gunicorn то waitress не нужен
import os

dirpath = os.path.dirname(__file__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

name_base = "db/cats.sqlite"
name_base = name_base
login = -1
db_session.global_init(name_base)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # print('1234567890')
    form = LoginForm()
    print('0912')
    if form.validate_on_submit():
        print('1234567890')
        session = db_session.create_session()
        user = session.query(User).filter(User.name == form.username.data).first()
        print('5678', user)
        print(form.username.data, form.password.data)
        # print(user.check_password(form.password.data))
        if user and user.check_password(form.password.data):
            # print('1234')
            login_user(user, remember=form.remember_me.data)
            print(current_user)
            return redirect("/")
        return render_template('login2.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login2.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    # print('123')
    form = LoginForm()
    # print('456')
    if form.validate_on_submit():
        # print('789')
        if form.password.data != form.password_again.data:
            return render_template('register.html', title="Регистрация", message="Пароли не совпадают", form=form)
        # print('012')
        session = db_session.create_session()
        print('345')
        if (session.query(User).filter(User.email == form.email.data).first() or form.email.data == ''):
            return render_template('register.html', title="Регистрация", message="Такой аккаунт уже существуют",
                                   form=form)
        print('678')
        user = User(
            name=form.username.data,
            surname=form.surname.data,
            age=form.age.data,
            email=form.email.data,
            hashed_password=form.password.data
        )
        # user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return 'login'

    return render_template('register.html', form=form)


@app.route('/animals', methods=['GET', 'POST'])
def departments():
    # print("*****************")
    if request.method == 'GET':
        print('GET')
        session = db_session.create_session()
        # print('-----------')
        animalq = session.query(Animals).all()
        # print(animalq)
        # return "Hello World"
        return render_template('departaments.html', users=animalq, title='capitan',
                               name='Тотемные животные по зороастрийскому календарю, выберите и согласно их и современным раздумьям напишем')
    else:
        print('POST')
        print(request.form['animal'])
        ans = request.form['animal'].split(',')
        session = db_session.create_session()
        animals = session.query(Animals).filter(Animals.id == ans[0]).first()
        if current_user.is_authenticated:
            cr = session.query(User).filter(User.name == current_user.name).first()
            print(cr.id)
            if str(cr.id) not in animals.users.split(","):
                print(cr.id, '--------------------')
                animals.countReg += 1
                if animals.users != "":
                    animals.users =  str(animals.users) + ","
                else:
                    animals.users = ""
                animals.users = str(animals.users) + str(cr.id)
            print(animals.id)

            if str(animals.id) not in cr.animals.split(","):
                print(animals.id, '----------------')
                if cr.animals != "":
                    cr.animals =  str(cr.animals) + ","
                else:
                    cr.animals = ""
                cr.animals = str(cr.animals) + str(animals.id)
            print('auth_success')
        animals.count += 1
        print(animals.desc)
        session.commit()
        return render_template('answer.html', title=ans[2], username='Ребята', desc=animals.desc)


@app.route('/plants', methods=['GET', 'POST'])
def departments2():
    # print("*****************")
    if request.method == 'GET':
        print('GET')
        session = db_session.create_session()
        # print('-----------')
        animalq = session.query(Plants).all()
        # print(animalq)
        # return "Hello World"
        return render_template('departaments.html', users=animalq, title='capitan',
                               name='Деревья по друидскому календарю')
    else:
        print('POST')
        print(request.form['animal'])
        ans = request.form['animal'].split(',')
        session = db_session.create_session()
        animals = session.query(Animals).filter(Animals.id == ans[0]).first()
        if current_user.is_authenticated:
            cr = session.query(User).filter(User.name == current_user.name).first()
            print(cr.id)
            if str(cr.id) not in animals.users.split(","):
                print(cr.id, '--------------------')
                animals.countReg += 1
                if animals.users != "":
                    animals.users =  str(animals.users) + ","
                else:
                    animals.users = ""
                animals.users = str(animals.users) + str(cr.id)
            print(animals.id)

            if str(animals.id) not in cr.animals.split(","):
                print(animals.id, '----------------')
                if cr.animals != "":
                    cr.animals =  str(cr.animals) + ","
                else:
                    cr.animals = ""
                cr.animals = str(cr.animals) + str(animals.id)
            print('auth_success')
        animals.count += 1
        print(animals.desc)
        session.commit()
        return render_template('answer.html', title=ans[2], username='Ребята', desc=animals.desc)


@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)


@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {param} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD": "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })


@app.route('/diags')
def diags():
    session = db_session.create_session()
    count = 0
    ms = []
    for ch in session.query(Animals).filter(Animals.count > 0):
        count += ch.count
        # print(ch.animal, ch.count)
        ms.append([ch.animal, ch.count])
    for inum, ch in enumerate(ms):
        ms[inum][1] = ms[inum][1] / count * 100
    # print(ms)
    ms.insert(0, ['Животное', 'Процент'])
    return render_template('diagramma.html', title='Вебсервис', username='Alexis', data=ms)


# A welcome message to test our server
@app.route('/')
def index():
    return render_template('index.html', title='Вебсервис', username='Alexis')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    port = int(os.environ.get('PORT', 5000))
    # serve(app, host='0.0.0.0', port=port)
    app.run(threaded=True, port=5000)  # если используем gunicorn то waitress не нужен
