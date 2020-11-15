from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/hello/<name>')
def hello_world2(name):
   return f'Hello World {name}'

def hello_world3():  #有点问题
   return 'Hello World'
app.add_url_rule('/','3', hello_world)

@app.route('/blog/<int:postID>')   #整型
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>') #float
def revision(revNo):
   return 'Revision Number %f' % revNo


@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')  #即python   或 python/ 都可以
def hello_python():
   return 'Hello Python'



if __name__ == '__main__':
   app.run(debug=True)