from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'kjhdfkjh3234'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == "POST":
        urls = {}
        url = 0
        if os.path.exists('urls.json'):
            with open('urls.json') as json_file:
                urls = json.load(json_file)

        if request.form['code'] in urls.keys():
            flash('That short name has already been taken. Please select different name.')
            return redirect(url_for('home'))

        if 'url' in request.form.keys():
            urls[request.form['code']] = {'url': request.form['url']}
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)
            f.save(request.form['code'])
            urls[request.form['code']] = {'file': full_name}

        with open('urls.json', 'w') as json_file:
            json.dump(urls, json_file)

        return render_template("your_url.html", code=request.form['code'])
    else:
        return redirect(url_for('home'))

