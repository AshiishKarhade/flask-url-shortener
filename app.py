from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/about')
def about():
    return "ABOUT"

if __name__ == "__main__":
    app.run()