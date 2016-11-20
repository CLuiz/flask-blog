from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3
from functools import wraps


# configuration
DATABASE = 'blog.db'
app = Flask(__name__)
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY ='\xe2\xca\xd0\x06\x8b\xb0\xb3\xee\x9e\xc2\xc8P+f\x99\xce\xa0\\\xf7r\xbc,P\xfb'

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function used for connecting to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
            request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route('/main')
def main():
    return render_template('main.html')

if __name__=='__main__':
    app.run(debug=True)
