from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index_flash():
    return render_template('index_flash.html')


@app.route('/login_flash', methods = ['GET', 'POST'])
def login_flash():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index_flash'))


    return render_template('login_flash.html', error = error)


if __name__ == '__main__':
    app.run(debug=True)