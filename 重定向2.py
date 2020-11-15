'''
400 - 用于错误请求
401 - 用于未身份验证的
403 - Forbidden
404 - 未找到
406 - 表示不接受
415 - 用于不支持的媒体类型
429 - 请求过多
'''

from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('log_in.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      if request.form['nm'] == 'admin' :
         return redirect(url_for('success'))
      else:
         abort(401)
   else:
       # abort(429)
       return redirect(url_for('index'))

@app.route('/success')
def success():
   return 'logged in successfully'

if __name__ == '__main__':
   app.run(debug = True)