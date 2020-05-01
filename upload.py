from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
import shutil
import subprocess

app = Flask(__name__)

@app.route('/')
def upload():
   return '''   <form action = "http://localhost:5000/uploader" method = "POST" 
                    enctype = "multipart/form-data">
                    <input type = "file" name = "file" />
                    <input type = "submit"/>
                </form>
            '''
	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		

def mv_to_bin(f):
    shutil.move('./{}'.format(f), './bin/{}'.format(f))



if __name__ == '__main__':
   app.run()
   mv_to_bin('a.out')
   subprocess.Popen(['mkdir', 'afl_in', 'afl_out'])
   subprocess.Popen(['chmod', '+x', './bin/a.out'])
   subprocess.Popen(['afl-fuzz', '-i', './afl_in/', '-o', './afl_out/', './bin/a.out'])
