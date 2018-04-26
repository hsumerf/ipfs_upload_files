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
      #lst = subprocess.call(["ipfs","add","APCO.jpg"])
      #cmd = [ 'echo', 'arg1', 'arg2' ]
      cmd = ["ipfs","add","APCO.jpg"]
      output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
      output = output.decode()
      hash = output.split(' ')[1]
      print(output,output[1],type(output),hash)

      #hsh = os.system('ipfs','add',APCO.jpg)
      #print(hsh)
      return 'file uploaded successfully and hash = ' + hash


@app.route('/hello')
def hello():
    return 'Hello, World'



    if __name__ == "__main__":
            app.run()
