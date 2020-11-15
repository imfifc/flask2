from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/set_cookies")  #秒
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("name", "Lily",max_age=3600)
    return resp

@app.route("/get_cookies")
def get_cookie():
    cookie_1 = request.cookies.get("name")  # 获取名字为name 对应cookie的值
    return cookie_1

@app.route("/delete_cookies")   #注意删除，只是让 cookie 过期。
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("name")

    return resp

if __name__ == '__main__':
    app.run(debug=True)