# -*- coding: utf-8 -*-
from flask import Flask,request, jsonify, send_file
from controllers import cFiles
from services import ParameterCheck
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! (ExportImportService)"

###---------------------------------------------------------------------------------------

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        kwargs ={
            "type":"import",
            "user_mail": ParameterCheck().secure_parameter(request.form['user_mail']),
            "description": ParameterCheck().secure_parameter(request.form['description']),
            "file_name":"",
            "file_path":"",
            "file_data":"",
            "insert_time":str(datetime.datetime.now()),
            "is_deleted":"0"
        }
        file_data = request.files.get('file_data') if 'file_data' in request.files else False
        return jsonify(cFiles().createfile(kwargs,file_data))  

    return '''
        <!doctype html>
        <html><head>
        <title>Upload File Test</title>
        </head><body>
        <h1>Upload File Test</h1>
        <form action="" method="post" enctype="multipart/form-data">
        <table>
        <tr><td><input type="file" name="file_data"></td></tr>
        <tr><td>user_mail</td><td><input type="text" id="user_mail" name="user_mail" value="oguzkaragoz@gmail.com"/></td></tr>
        <tr><td>description</td><td><input type="text" id="description" name="description" value="description"/></td></tr>
        <tr><td><input type="submit" value="Upload"></td><td></td></tr>
        </table>
        </form>
        </body>
        </html>
        '''

@app.route("/importfile",methods=['POST'])
def importfile():
    kwargs ={
        "type":"import",
        "user_mail": ParameterCheck().secure_parameter(request.form['user_mail']),
        "description": ParameterCheck().secure_parameter(request.form['description']),
        "file_name":"",
        "file_path":"",
        "file_data":"",
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    
    file_data = request.files.get('file_data') if 'file_data' in request.files else False
    return jsonify(cFiles().createfile(kwargs,file_data))

@app.route("/updatefile",methods=['POST'])
def updatefile():
    kwargs ={
        "type":"import",
        "id":ParameterCheck().secure_parameter(request.form['id']),
        "user_mail": ParameterCheck().secure_parameter(request.form['user_mail']),
        "description": ParameterCheck().secure_parameter(request.form['description']),
        "file_name":"",
        "file_path":"",
        "file_data":"",
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    
    file_data = request.files.get('file_data') if 'file_data' in request.files else False
    return jsonify(cFiles().updatefile(kwargs,file_data))

@app.route("/downloadfile/<file_id>",methods=['GET'])
def downloadfile(file_id):
    return jsonify(cFiles().downloadfile(file_id))

@app.route("/getfile",methods=['GET'])
def getfile():
    file_id = ParameterCheck().secure_parameter(request.form['file_id'])
    return jsonify(cFiles().getfile(file_id))

@app.route("/deletefile",methods=['GET'])
def deletefile():
    file_id = ParameterCheck().secure_parameter(request.form['file_id'])
    return jsonify(cFiles().deletefile(file_id))

@app.route("/listfiles",methods=['GET'])
def listfiles():
    user_mail = ParameterCheck().secure_parameter(request.form['user_mail'])
    description = ParameterCheck().secure_parameter(request.form['description'])
    limit = ParameterCheck().secure_parameter(request.form['limit'])
    offset = ParameterCheck().secure_parameter(request.form['offset'])    
    return jsonify(cFiles().listfiles(user_mail,description,limit,offset))

###---------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
    
