from flask import Flask
from flask_cors import CORS
from dataImport import import_data, flush_all, about_me

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/')
def index():
    return {'Read with Italian accent': 'Mamma mia marcello! What are you doing here?'}


@app.route('/about_me')
def about_us():
    return about_me()


@app.route('/skills')
def skills():
    result = import_data("skills")
    return result


@app.route('/experience')
def experience():
    result = import_data("experience")
    return result


@app.route('/projects')
def projects():
    result = import_data("projects")
    return result


@app.route('/certificates')
def certificates():
    result = import_data("certificates")
    return result


@app.route('/contact')
def contact():
    result = import_data("contact")
    return result


@app.route('/flush_all')
def reset_all():
    result = flush_all()
    return result


if __name__ == '__main__':
    app.run()
