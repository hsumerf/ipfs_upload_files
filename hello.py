from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.utils import secure_filename
import os,sys
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = 'docs/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      file = request.files['file']
      filename = secure_filename(file.filename)
      file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      file.save(file_path)
      print(file_path)
      #hsh = os.system('ipfs','add',APCO.jpg)
      #print(hsh)
      lst = os.system('ls')
      print(lst)
      return 'file uploaded successfully'


@app.route('/hello')
def hello():
    return 'Hello, World'



    if __name__ == "__main__":
            app.run()
