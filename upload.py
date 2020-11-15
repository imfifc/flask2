from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './upload/'
app.config['MAX_CONTENT_PATH']= 100000
@app.route('/upload')
def upload_file():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      basepath = os.path.dirname(__file__)  # 当前文件所在路径
      upload_path = os.path.join(basepath, 'uploads',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
      f.save(upload_path)
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run()