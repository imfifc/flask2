# Flask.redirect(location, statuscode, response)
'''
以下状态代码已标准化：

HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT
默认状态代码为302，表示'found'。
'''
from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('log_in.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form['nm'] == 'admin':
        return redirect(url_for('success'))
    return redirect(url_for('index'))


@app.route('/success')
def success():
    return 'logged in successfully'


if __name__ == '__main__':
    app.run(debug=True)