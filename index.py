from flask import Flask

app = Flask(__name__)

@app.route('/')
def dashboard():
    return  "my first heroku app"

app.run()