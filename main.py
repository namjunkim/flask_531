from flask import Flask, render_template, request, jsonify
from resources.language import translations
from flask_cors import CORS
from __init__ import create_app
from src.model.models import Users

#init app
app = create_app("local")

#app = Flask('531 Project')

CORS(app)

@app.route('/', methods = ['GET'])
def hello():
    return 'Hello world'

@app.route('/home', methods = ['GET'])
def home():
    lang = request.args.get('lang', 'en')
    home_title = translations[lang]['home_title']
    return render_template('home/home.html', lang=lang, home_title=home_title)


@app.route('/vue/intro', methods = ['GET'])
def intro():
    lang = request.args.get('lang', 'ko')
    home_title = translations[lang]['home_title']
    return render_template('home/intro_ko.html', lang=lang)


@app.route('/body', methods = ['GET'])
def whole_body():
    lang = request.args.get('lang', 'en')
    home_title = translations[lang]['home_title']
    upper_nav_intro = translations[lang]['upper_nav_intro']
    return render_template('home/whole_body.html',
                           lang=lang, home_title=home_title, upper_nav_intro=upper_nav_intro
                           )

#@app.route('/vue/home', methods = ['GET'])
#def get_message():
#    return jsonify({'message': 'Hello from Flask!'})

@app.route('/test/data', methods = ['GET'])
def give_message():
    return jsonify({'message': 'Hello from Flask!'})

@app.route('/test/db/data', methods = ['GET'])
def get_db_data():
    users = Users.query.all()
    return jsonify([user.to_dict() for user in users])


app.run('0.0.0.0', port='8231')
#if __name__ == "__main__":
#    db.create_all()  # Create database tables
#    app.run(debug=True)