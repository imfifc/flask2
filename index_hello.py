from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 往模板中传入的数据
    my_str = 'Hello Word'
    my_int = 10
    my_list = [3, 4, 2, 1, 7, 9]
    my_dict = {
        'name': 'xiaoming',
        'age': 18
    }
    return render_template('hello.html',
                           my_str=my_str,
                           my_int=my_int,
                           my_list=my_list,
                           my_dict=my_dict
                           )
if __name__ == '__main__':
    app.run(debug=True)