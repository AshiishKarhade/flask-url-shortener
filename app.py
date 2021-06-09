from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__)
app.secret_key = 'kjhdfkjh3234'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == "POST":
        urls = {}
        code_form = request.form['code']
        url = request.form['url']

        if os.path.exists('urls.json'):
            with open('urls.json') as json_file:
                urls = json.load(json_file)

        if code_form in urls.keys():
            flash('That short name has already been taken. Please select different name.')
            return redirect(url_for('home'))

        urls[code_form] = {"url": url}

        with open('urls.json', 'w') as json_file:
            json.dump(urls, json_file)

        return render_template("your_url.html", code=code_form)
    else:
        return redirect(url_for('home'))

