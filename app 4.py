# -*- coding: utf-8 -*-
from flask import Flask,request, jsonify
#from servicemodel import Model
from servicegraylog import testlog,testlog2
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! (GraylogService)"
        
  
@app.route("/test",methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        logger = request.form['logger']
        localhost = request.form['localhost']
        port = request.form['port']
        message = request.form['message']
        message = message + "----" + str(datetime.datetime.now())
        
        return jsonify(testlog(logger,localhost,port,message))
    
    return '''
        <!doctype html>
        <html><head>
        <title>Upload new File</title>
        </head><body>
        <h1>Upload new File</h1>
        <form action="" method="post" enctype="multipart/form-data">
        <table>
        <tr><td>logger</td><td><input type="text" id="logger" name="logger" value="test-gelf-udp"/></td></tr>
        <tr><td>localhost</td><td><input type="text" id="localhost" name="localhost" value="192.168.1.106"/></td></tr>
        <tr><td>port</td><td><input type="text" id="port" name="port" value="12203"/></td></tr>
        <tr><td>message</td><td><input type="text" id="message" name="message" value="message"/></td></tr>
        <tr><td><input type="submit" value="Upload"></td><td></td></tr>
        </table>
        </form>
        </body>
        </html>
        '''

@app.route("/test2",methods=['GET', 'POST'])
def test2():
    if request.method == 'POST':
        logger = request.form['logger']
        localhost = request.form['localhost']
        port = request.form['port']
        message = request.form['message']
        type = request.form['type']
        description = request.form['description']
        message = message + "----" + str(datetime.datetime.now())
        
        return jsonify(testlog2(logger,localhost,port,message,type,description))
    
    return '''
        <!doctype html>
        <html><head>
        <title>Upload new File</title>
        </head><body>
        <h1>Upload new File</h1>
        <form action="" method="post" enctype="multipart/form-data">
        <table>
        <tr><td>logger</td><td><input type="text" id="logger" name="logger" value="test-gelf-udp-2"/></td></tr>
        <tr><td>localhost</td><td><input type="text" id="localhost" name="localhost" value="192.168.1.106"/></td></tr>
        <tr><td>port</td><td><input type="text" id="port" name="port" value="12204"/></td></tr>
        <tr><td>message</td><td><input type="text" id="message" name="message" value="message"/></td></tr>
        <tr><td>type</td><td><input type="text" id="type" name="type" value="text"/></td></tr>
        <tr><td>description</td><td><input type="text" id="description" name="description" value="description"/></td></tr>        
        <tr><td><input type="submit" value="Upload"></td><td></td></tr>
        </table>
        </form>
        </body>
        </html>
        '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5007)
    
