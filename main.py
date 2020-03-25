# app.py
from flask import Flask, request, jsonify, render_template
from data import db_session
from data.animals import Animals
from waitress import serve
import os

app = Flask(__name__)

name_base = "cats.sqlite"
name_base = "db/" + name_base
# db_session.global_init(name_base)


@app.route('/animals')
def departments():
    print("*****************")
    session = db_session.create_session()
    print('-----------')
    animals = session.query(Animals).all()
    # return "Hello World"
    return render_template('departaments.html', users=animals)


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
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return render_template('index.html', title='Вебсервис', username='Alexis')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    port = int(os.environ.get('PORT', 5000))
    serve(app, host='0.0.0.0', port=port)