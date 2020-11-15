'''
会话是客户端登录到服务器并注销服务器的时间间隔
在该会话中保存的数据会存储在服务器上的临时目录中。

为每个客户端的会话分配会话ID。会话数据存储在cookie的顶部，服务器以加密方式对其进行签名。对于此加密，Flask应用程序需要一个定义的SECRET_KEY。
Session对象也是一个字典对象，包含会话变量和关联值的键值对。
'''
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

app.secret_key = 'fkdjsafjdkfdlkjfadskjfadskljdsfklj'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return '登录用户名是:' + username + '<br>' + \
                 "<b><a href = '/logout'>点击这里注销</a></b>"

    return "您暂未登录， <br><a href = '/login'></b>" + \
         "点击这里登录</b></a>"


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
   <form action = "" method = "post">
      <p><input type ="text" name ="username"/></p>
      <p><input type ="submit" value ="登录"/></p>
   </form>
   '''


@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)

   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)