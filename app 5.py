# -*- coding: utf-8 -*-

from flask import Flask,jsonify,request
from controllers import cSendings
from services import ParameterCheck
import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! (MediaService)"

###---------------------------------------------------------------------------------------

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        kwargs={
            "media_type" : "mail",
            "smtp" : ParameterCheck().secure_parameter(request.form['smtp']),
            "port" : ParameterCheck().secure_parameter(request.form['port']),
            "user_mail" : ParameterCheck().secure_parameter(request.form['user_mail']),
            "password" : ParameterCheck().secure_parameter(request.form['password']),
            "tolist" : ParameterCheck().secure_parameter(request.form['tolist']),
            "cclist" : ParameterCheck().secure_parameter(request.form['cclist']),
            "bcclist" : ParameterCheck().secure_parameter(request.form['bcclist']),
            "subject" : ParameterCheck().secure_parameter(request.form['subject']),
            "body" : ParameterCheck().secure_parameter(request.form['body']),
            "exportimport_service_url" : ParameterCheck().secure_parameter(request.form['exportimport_service_url']),
            "attachment_ids" : "",
            "insert_time" : str(datetime.datetime.now()),
            "is_deleted" : "0"
        }
        attachments = request.files.getlist('attachments[]')
        return jsonify(cSendings().sendmailwithfiles(kwargs,attachments))      
    
    return '''
        <!doctype html>
        <html><head>
        <title>Send Mail Test</title>
        </head><body>
        <h1>Send Mail Test</h1>
        <form action="" method="post" enctype="multipart/form-data">
        <table>
        <tr><td><input type="file" name="attachments[]" multiple="multiple"></td></tr>
        <tr><td>smtp</td><td><input type="text" id="smtp" name="smtp" value="smtp.gmail.com"/></td></tr>
        <tr><td>port</td><td><input type="text" id="port" name="port" value="587"/></td></tr>
        <tr><td>user_mail</td><td><input type="text" id="user_mail" name="user_mail" value="itmonitoringcommunity@gmail.com"/></td></tr>
        <tr><td>password</td><td><input type="text" id="password" name="password" value="pass"/></td></tr>
        <tr><td>tolist</td><td><input type="text" id="tolist" name="tolist" value="oguzkaragoz@gmail.com"/></td></tr>
        <tr><td>cclist</td><td><input type="text" id="cclist" name="cclist" value="oguzkaragoz@gmail.com"/></td></tr>
        <tr><td>bcclist</td><td><input type="text" id="bcclist" name="bcclist" value=""/></td></tr>
        <tr><td>subject</td><td><input type="text" id="subject" name="subject" value="subject"/></td></tr>
        <tr><td>body</td><td><input type="text" id="body" name="body" value="body"/></td></tr>
        <tr><td>exportimport_service_url</td><td><input type="text" id="exportimport_service_url" name="exportimport_service_url" value="http://127.0.0.1:5001"/></td></tr>

        <tr><td><input type="submit" value="Upload"></td><td></td></tr>
        </table>
        </form>
        </body>
        </html>
        '''

@app.route("/sendmailwithfiles", methods=['POST'])
def sendmailwithfiles():
    kwargs={
        "media_type" : "mail",
        "smtp" : ParameterCheck().secure_parameter(request.form['smtp']),
        "port" : ParameterCheck().secure_parameter(request.form['port']),
        "user_mail" : ParameterCheck().secure_parameter(request.form['user_mail']),
        "password" : ParameterCheck().secure_parameter(request.form['password']),
        "tolist" : ParameterCheck().secure_parameter(request.form['tolist']),
        "cclist" : ParameterCheck().secure_parameter(request.form['cclist']),
        "bcclist" : ParameterCheck().secure_parameter(request.form['bcclist']),
        "subject" : ParameterCheck().secure_parameter(request.form['subject']),
        "body" : ParameterCheck().secure_parameter(request.form['body']),
        "exportimport_service_url" : ParameterCheck().secure_parameter(request.form['exportimport_service_url']),
        "attachment_ids" : "",
        "insert_time" : str(datetime.datetime.now()),
        "is_deleted" : "0"
    }

    attachments = request.files.getlist('attachments[]')
    return jsonify(cSendings().sendmailwithfiles(kwargs,attachments)) 
    
@app.route("/sendmail", methods=['POST'])
def sendmail():
    kwargs={
        "media_type" : "mail",
        "smtp" : ParameterCheck().secure_parameter(request.form['smtp']),
        "port" : ParameterCheck().secure_parameter(request.form['port']),
        "user_mail" : ParameterCheck().secure_parameter(request.form['user_mail']),
        "password" : ParameterCheck().secure_parameter(request.form['password']),
        "tolist" : ParameterCheck().secure_parameter(request.form['tolist']),
        "cclist" : ParameterCheck().secure_parameter(request.form['cclist']),
        "bcclist" : ParameterCheck().secure_parameter(request.form['bcclist']),
        "subject" : ParameterCheck().secure_parameter(request.form['subject']),
        "body" : ParameterCheck().secure_parameter(request.form['body']),
        "exportimport_service_url" : "",
        "attachment_ids" : "",
        "insert_time" : str(datetime.datetime.now()),
        "is_deleted" : "0"
    }
    return jsonify(cSendings().sendmail(kwargs))

@app.route("/listsendings",methods=['GET'])
def listsendings():
    smtp = ParameterCheck().secure_parameter(request.form['smtp'])
    port = ParameterCheck().secure_parameter(request.form['port'])
    user_mail = ParameterCheck().secure_parameter(request.form['user_mail'])
    tolist = ParameterCheck().secure_parameter(request.form['tolist'])
    cclist = ParameterCheck().secure_parameter(request.form['cclist'])
    bcclist = ParameterCheck().secure_parameter(request.form['bcclist'])
    subject = ParameterCheck().secure_parameter(request.form['subject'])
    body = ParameterCheck().secure_parameter(request.form['body'])

    limit = ParameterCheck().secure_parameter(request.form['limit'])
    offset = ParameterCheck().secure_parameter(request.form['offset']) 

    return jsonify(cSendings().listsendings(smtp,port,user_mail,tolist,cclist,bcclist,subject,body,limit,offset))

###---------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
