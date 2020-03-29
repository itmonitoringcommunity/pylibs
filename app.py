# -*- coding: utf-8 -*-
from flask import Flask,jsonify,request,g,session
from flask_login import LoginManager,UserMixin,current_user,login_required, login_user, logout_user
from controllers import cBulletinProcedures,cBulletinStates,cBulletinTypes,cBulletins,cGroups,cLanguages,cServices,cSLA,cTerms,cUserLogs,cUsers
from services import ParameterCheck
import datetime,os

app = Flask(__name__)
app.config.update(
    DEBUG = False,
    SECRET_KEY = os.urandom(24)
)

login_manager = LoginManager()
login_manager.init_app(app)

class SessionUser(UserMixin):
    def __init__(self,url,kwargs):
        self.url=url
        self.id = str(kwargs["userid"])
        self.userid = str(kwargs["userid"])
        self.role = str(kwargs["role"])
        self.username = str(kwargs["username"])
        self.title = str(kwargs["title"])
        self.fullname = str(kwargs["fullname"])
        self.organization = str(kwargs["organization"])
        self.department = str(kwargs["department"])       


@login_manager.user_loader
def user_load(url,kwargs):   
    try:
        return SessionUser(url,kwargs)
    except:
        return None

@app.before_request
def before_request():
    session.permanent=True
    app.permanent_session_lifetime=datetime.timedelta(minutes=20)
    session.modified = True
    g.user = current_user

@app.after_request
def after_request(response):
    return response

@app.route("/")
def hello():    
    return "Hello World! (BulletinService)"
	
###---------------------------------------------------------------------------------------

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        kwargs ={
            "language_id":ParameterCheck().secure_parameter(request.form['language_id']),
            "organization":ParameterCheck().secure_parameter(request.form['organization']),
            "bulletin_type_id":ParameterCheck().secure_parameter(request.form['bulletin_type_id']),
            "bulletin_state_id":ParameterCheck().secure_parameter(request.form['bulletin_state_id']),
            
            "bulletin_classification":ParameterCheck().secure_parameter(request.form['bulletin_classification']),
            "bulletin_priority":ParameterCheck().secure_parameter(request.form['bulletin_priority']),
            "contact":ParameterCheck().secure_parameter(request.form['contact']),
                 
            "ticket_service_url":ParameterCheck().secure_parameter(request.form['ticket_service_url']),
            "ticket_service_user":ParameterCheck().secure_parameter(request.form['ticket_service_user']),
            "ticket_service_password":ParameterCheck().secure_parameter(request.form['ticket_service_password']),
            "ticket_support_group":ParameterCheck().secure_parameter(request.form['ticket_support_group']),
            "ticket_assigned_to":ParameterCheck().secure_parameter(request.form['ticket_assigned_to']),
            "ticket_case_url":ParameterCheck().secure_parameter(request.form['ticket_case_url']),
            "ticket_case_id":ParameterCheck().secure_parameter(request.form['ticket_case_id']),

            "media_service_url":ParameterCheck().secure_parameter(request.form['media_service_url']),
            "media_service_smtp":ParameterCheck().secure_parameter(request.form['media_service_smtp']),
            "media_service_port":ParameterCheck().secure_parameter(request.form['media_service_port']),
            "media_service_user":ParameterCheck().secure_parameter(request.form['media_service_user']),
            "media_service_password":ParameterCheck().secure_parameter(request.form['media_service_password']),
                 
            "created_by":ParameterCheck().secure_parameter(request.form['created_by']),
            "code":"",
            "title":ParameterCheck().secure_parameter(request.form['title']),
            "detail":ParameterCheck().secure_parameter(request.form['detail']),
            "effect":ParameterCheck().secure_parameter(request.form['effect']),
            "begin_time":ParameterCheck().secure_parameter(request.form['begin_time']),
            "end_time":ParameterCheck().secure_parameter(request.form['end_time']),
            "duration":"",
                 
            "bulletin_resolution":ParameterCheck().secure_parameter(request.form['bulletin_resolution']),    
            "root_cause":ParameterCheck().secure_parameter(request.form['root_cause']),
            "resolved_time":ParameterCheck().secure_parameter(request.form['resolved_time']), 
            "resolved_by":ParameterCheck().secure_parameter(request.form['resolved_by']),
            "is_resolved":"0",

            "insert_time":str(datetime.datetime.now()),
            "modify_time":str(datetime.datetime.now()),
            "is_deleted":"0"
        }
        
        return jsonify(cBulletins().createbulletin(kwargs)) 

        
    return '''
        <!doctype html>
        <html><head>
        <title>Create Bulletin Test</title>
        </head><body>
        <h1>Create Bulletin Test</h1>
        <form action="" method="post">
        <table>
        <tr><td>language_id</td><td><input type="text" id="language_id" name="language_id" value="1"/></td></tr>        
        <tr><td>bulletin_type_id</td><td><input type="text" id="bulletin_type_id" name="bulletin_type_id" value="1"/></td></tr>
        <tr><td>bulletin_state_id</td><td><input type="text" id="bulletin_state_id" name="bulletin_state_id" value="1"/></td></tr>
        
        <tr><td>bulletin_classification</td><td><input type="text" id="bulletin_classification" name="bulletin_classification" value="bulletin_classification"/></td></tr>
        <tr><td>bulletin_priority</td><td><input type="text" id="bulletin_priority" name="bulletin_priority" value="bulletin_priority"/></td></tr>
        <tr><td>contact</td><td><input type="text" id="contact_id" name="contact" value="contact"/></td></tr>       
        
        <tr><td>ticket_service_url</td><td><input type="text" id="ticket_service_url" name="ticket_service_url" value="http://127.0.0.1:5005"/></td></tr>
        <tr><td>ticket_service_user</td><td><input type="text" id="ticket_service_user" name="ticket_service_user" value=""/></td></tr>
        <tr><td>ticket_service_password</td><td><input type="text" id="ticket_service_password" name="ticket_service_password" value=""/></td></tr>
        <tr><td>ticket_support_group</td><td><input type="text" id="ticket_support_group" name="ticket_support_group" value="ticket_support_group"/></td></tr>
        <tr><td>ticket_assigned_to</td><td><input type="text" id="ticket_assigned_to" name="ticket_assigned_to" value="ticket_assigned_to"/></td></tr>
        <tr><td>ticket_case_url</td><td><input type="text" id="ticket_case_url" name="ticket_case_url" value="http://127.0.0.1:5005"/></td></tr>
        
        <tr><td>media_service_url</td><td><input type="text" id="media_service_url" name="media_service_url" value="http://127.0.0.1:5002"/></td></tr>
        <tr><td>media_service_smtp</td><td><input type="text" id="media_service_smtp" name="media_service_smtp" value="smtp.gmail.com"/></td></tr>
        <tr><td>media_service_port</td><td><input type="text" id="media_service_port" name="media_service_port" value="587"/></td></tr>
        <tr><td>media_service_user</td><td><input type="text" id="media_service_user" name="media_service_user" value="itmonitoringcommunity@gmail.com"/></td></tr>
        <tr><td>media_service_password</td><td><input type="text" id="media_service_password" name="media_service_password" value="pass"/></td></tr>   
        
        <tr><td>created_by</td><td><input type="text" id="created_by" name="created_by" value="oguz burak karagoz"/></td></tr>
        <tr><td>title</td><td><input type="text" id="title" name="title" value="deneme bulteni"/></td></tr>
        <tr><td>detail</td><td><input type="text" id="detail" name="detail" value="detail"/></td></tr>
        <tr><td>effect</td><td><input type="text" id="effect" name="effect" value="www.google.com"/></td></tr>
        <tr><td>begin_time</td><td><input type="text" id="begin_time" name="begin_time" value="2018-09-08 12:00:00"/></td></tr>
        <tr><td>end_time</td><td><input type="text" id="end_time" name="end_time" value=""/></td></tr>
         
        <tr><td>bulletin_resolution</td><td><input type="text" id="bulletin_resolution" name="bulletin_resolution" value="bulletin_resolution"/></td></tr>
        <tr><td>root_cause</td><td><input type="text" id="root_cause" name="root_cause" value="root cause"/></td></tr>
        <tr><td>resolved_time</td><td><input type="text" id="resolved_time" name="resolved_time" value="2018-09-08 12:00:00"/></td></tr>
        <tr><td>resolved_by</td><td><input type="text" id="resolved_by" name="resolved_by" value="obk"/></td></tr>
        <tr><td>is_resolved</td><td><input type="text" id="is_resolved" name="is_resolved" value="0"/></td></tr>

        <tr><td><input type="submit" value="Create"></td><td></td></tr>
        </table>
        </form>
        </body>
        </html>
        '''

@app.route("/test2",methods=['GET','POST'])
def test2():
    if request.method == 'POST':
        begin_time = ParameterCheck().secure_parameter(request.form['begin_time'])
        end_time = ParameterCheck().secure_parameter(request.form['end_time'])
        
        return jsonify(cSLA().get_service_list_SLA(begin_time,end_time))  
    
    return '''
        <!doctype html>
        <html><head>
        <title>getservicelistSLAtest</title>
        </head><body>
        <h1>get service list SLA test</h1>
        <form action="" method="post" enctype="multipart/form-data">
        <table>
        <tr><td>begin_time</td><td><input type="text" id="begin_time" name="begin_time" value=""/></td></tr>
        <tr><td>end_time</td><td><input type="text" id="end_time" name="end_time" value=""/></td></tr>
         
        <tr><td><input type="submit" value="search"></td><td></td></tr>
        </table>
        </form>
        </body>
        </html>
        '''
		
@app.route("/test3",methods=['GET','POST'])
def test3():
    if request.method == 'POST':
        service_id = ParameterCheck().secure_parameter(request.form['service_id'])
        begin_time = ParameterCheck().secure_parameter(request.form['begin_time'])
        end_time = ParameterCheck().secure_parameter(request.form['end_time'])
        
        return jsonify(cSLA().get_service_bulletins(service_id,begin_time,end_time))  
    
    return '''
        <!doctype html>
        <html><head>
        <title>getservicebulletinstest</title>
        </head><body>
        <h1>get service bulletins test</h1>
        <form action="" method="post" enctype="multipart/form-data">
        <table>
        <tr><td>service_id</td><td><input type="text" id="service_id" name="service_id" value=""/></td></tr>        
        <tr><td>begin_time</td><td><input type="text" id="begin_time" name="begin_time" value=""/></td></tr>
        <tr><td>end_time</td><td><input type="text" id="end_time" name="end_time" value=""/></td></tr>
         
        <tr><td><input type="submit" value="search"></td><td></td></tr>
        </table>
        </form>
        </body>
        </html>
        '''

###---------------------------------------------------------------------------------------

@app.route("/createbulletinprocedure", methods=['GET'])
#@login_required
def createbulletinprocedure():
    kwargs = {
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "description":ParameterCheck().secure_parameter(request.form['description']),
        "tolist":ParameterCheck().secure_parameter(request.form['tolist']),
        "cclist":ParameterCheck().secure_parameter(request.form['cclist']),
        "bcclist":ParameterCheck().secure_parameter(request.form['bcclist']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cBulletinProcedures().createbulletinprocedure(kwargs))

@app.route("/updatebulletinprocedure", methods=['GET'])
#@login_required
def updatebulletinprocedure():
    kwargs = {
        "id":ParameterCheck().secure_parameter(request.form['id']),
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "description":ParameterCheck().secure_parameter(request.form['description']),
        "tolist":ParameterCheck().secure_parameter(request.form['tolist']),
        "cclist":ParameterCheck().secure_parameter(request.form['cclist']),
        "bcclist":ParameterCheck().secure_parameter(request.form['bcclist']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cBulletinProcedures().updatebulletinprocedure(kwargs))
    
@app.route("/deletebulletinprocedure", methods=['GET'])
#@login_required
def deletebulletinprocedure(): 
    bulletin_procedure_id = ParameterCheck().secure_parameter(request.form['bulletin_procedure_id'])
    return jsonify(cBulletinProcedures().deletebulletinprocedure(bulletin_procedure_id))
   
@app.route("/listbulletinbulletinprocedures", methods=['GET'])
#@login_required
def listbulletinbulletinprocedures(): 
    return jsonify(cBulletinProcedures().listbulletinprocedures())
    
@app.route("/getbulletinprocedure", methods=['GET'])
#@login_required
def getbulletinprocedure():
    bulletin_procedure_id = ParameterCheck().secure_parameter(request.form['bulletin_procedure_id'])
    return jsonify(cBulletinProcedures().getbulletinprocedure(bulletin_procedure_id))

@app.route("/searchbulletinprocedure", methods=['GET'])
#@login_required
def searchbulletinprocedure():
    search_text = ParameterCheck().secure_parameter(request.form['search_text'])
    return jsonify(cBulletinProcedures().searchbulletinprocedure(search_text))

###---------------------------------------------------------------------------------------

@app.route("/createbulletinstate", methods=['GET'])
#@login_required
def createbulletinstate():
    kwargs = {
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "description":ParameterCheck().secure_parameter(request.form['description']),
        "color":ParameterCheck().secure_parameter(request.form['color']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cBulletinStates().createbulletinstate(kwargs))

@app.route("/updatebulletinstate", methods=['GET'])
#@login_required
def updatebulletinstate():
    kwargs = {
        "id":ParameterCheck().secure_parameter(request.form['id']),
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "description":ParameterCheck().secure_parameter(request.form['description']),
        "color":ParameterCheck().secure_parameter(request.form['color']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cBulletinStates().updatebulletinstate(kwargs))
    
@app.route("/deletebulletinstate", methods=['GET'])
#@login_required
def deletebulletinstate(): 
    bulletin_state_id = ParameterCheck().secure_parameter(request.form['bulletin_state_id'])
    return jsonify(cBulletinStates().deletebulletinstate(bulletin_state_id))
   
@app.route("/listbulletinstates", methods=['GET'])
#@login_required
def listbulletinstates(): 
    return jsonify(cBulletinStates().listbulletinstates())
    
@app.route("/getbulletinstate", methods=['GET'])
#@login_required
def getbulletinstate():
    bulletin_state_id = ParameterCheck().secure_parameter(request.form['bulletin_state_id'])
    return jsonify(cBulletinStates().getbulletinstate(bulletin_state_id))

@app.route("/searchbulletinstate", methods=['GET'])
#@login_required
def searchbulletinstate():
    search_text = ParameterCheck().secure_parameter(request.form['search_text'])
    return jsonify(cBulletinStates().searchbulletinstate(search_text))

###---------------------------------------------------------------------------------------

@app.route("/createbulletintype", methods=['GET'])
#@login_required
def createbulletintype():
    kwargs = {
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "description":ParameterCheck().secure_parameter(request.form['description']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cBulletinTypes().createbulletintype(kwargs))

@app.route("/updatebulletintype", methods=['GET'])
#@login_required
def updatebulletintype():
    kwargs = {
        "id":ParameterCheck().secure_parameter(request.form['id']),
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "description":ParameterCheck().secure_parameter(request.form['description']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cBulletinTypes().updatebulletintype(kwargs))
    
@app.route("/deletebulletintype", methods=['GET'])
#@login_required
def deletebulletintype(): 
    bulletin_type_id = ParameterCheck().secure_parameter(request.form['bulletin_type_id'])
    return jsonify(cBulletinTypes().deletebulletintype(bulletin_type_id))
   
@app.route("/listbulletinbulletinstates", methods=['GET'])
#@login_required
def listbulletinbulletintypes(): 
    return jsonify(cBulletinTypes().listbulletintypes())
    
@app.route("/getbulletintype", methods=['GET'])
#@login_required
def getbulletintype():
    bulletin_type_id = ParameterCheck().secure_parameter(request.form['bulletin_type_id'])
    return jsonify(cBulletinTypes().getbulletintype(bulletin_type_id))

@app.route("/searchbulletintype", methods=['GET'])
#@login_required
def searchbulletintype():
    search_text = ParameterCheck().secure_parameter(request.form['search_text'])
    return jsonify(cBulletinTypes().searchbulletintype(search_text))

###---------------------------------------------------------------------------------------

@app.route("/createbulletin",methods=['GET'])
#@login_required
def createbulletin():
    kwargs ={
        "language_id":ParameterCheck().secure_parameter(request.form['language_id']),
        "organization":ParameterCheck().secure_parameter(request.form['organization']),
        "bulletin_type_id":ParameterCheck().secure_parameter(request.form['bulletin_type_id']),
        "bulletin_state_id":ParameterCheck().secure_parameter(request.form['bulletin_state_id']),
        
        "bulletin_classification":ParameterCheck().secure_parameter(request.form['bulletin_classification']),
        "bulletin_priority":ParameterCheck().secure_parameter(request.form['bulletin_priority']),
        "contact":ParameterCheck().secure_parameter(request.form['contact']),
                
        "ticket_service_url":ParameterCheck().secure_parameter(request.form['ticket_service_url']),
        "ticket_service_user":ParameterCheck().secure_parameter(request.form['ticket_service_user']),
        "ticket_service_password":ParameterCheck().secure_parameter(request.form['ticket_service_password']),
        "ticket_support_group":ParameterCheck().secure_parameter(request.form['ticket_support_group']),
        "ticket_assigned_to":ParameterCheck().secure_parameter(request.form['ticket_assigned_to']),
        "ticket_case_url":ParameterCheck().secure_parameter(request.form['ticket_case_url']),
        "ticket_case_id":ParameterCheck().secure_parameter(request.form['ticket_case_id']),
            
        "media_service_url":ParameterCheck().secure_parameter(request.form['media_service_url']),
        "media_service_smtp":ParameterCheck().secure_parameter(request.form['media_service_smtp']),
        "media_service_port":ParameterCheck().secure_parameter(request.form['media_service_port']),
        "media_service_user":ParameterCheck().secure_parameter(request.form['media_service_user']),
        "media_service_password":ParameterCheck().secure_parameter(request.form['media_service_password']),
                
        "created_by":ParameterCheck().secure_parameter(request.form['created_by']),
        "code":"",
        "title":ParameterCheck().secure_parameter(request.form['title']),
        "detail":ParameterCheck().secure_parameter(request.form['detail']),
        "effect":ParameterCheck().secure_parameter(request.form['effect']),
        "begin_time":ParameterCheck().secure_parameter(request.form['begin_time']),
        "end_time":ParameterCheck().secure_parameter(request.form['end_time']),
        "duration":"",
                
        "bulletin_resolution":ParameterCheck().secure_parameter(request.form['bulletin_resolution']),    
        "root_cause":ParameterCheck().secure_parameter(request.form['root_cause']),
        "resolved_time":ParameterCheck().secure_parameter(request.form['resolved_time']), 
        "resolved_by":ParameterCheck().secure_parameter(request.form['resolved_by']),
        "is_resolved":"0",

        "insert_time":str(datetime.datetime.now()),
        "modify_time":str(datetime.datetime.now()),
        "is_deleted":"0"
        }
    
    return jsonify(cBulletins().createbulletin(kwargs))

@app.route("/updatebulletin",methods=['GET'])
#@login_required
def updatebulletin():
    kwargs ={
        "id":ParameterCheck().secure_parameter(request.form['id']),
        "language_id":ParameterCheck().secure_parameter(request.form['language_id']),
        "organization":ParameterCheck().secure_parameter(request.form['organization']),
        "bulletin_type_id":ParameterCheck().secure_parameter(request.form['bulletin_type_id']),
        "bulletin_state_id":ParameterCheck().secure_parameter(request.form['bulletin_state_id']),
        
        "bulletin_classification":ParameterCheck().secure_parameter(request.form['bulletin_classification']),
        "bulletin_priority":ParameterCheck().secure_parameter(request.form['bulletin_priority']),
        "contact":ParameterCheck().secure_parameter(request.form['contact']),
                
        "ticket_service_url":ParameterCheck().secure_parameter(request.form['ticket_service_url']),
        "ticket_service_user":ParameterCheck().secure_parameter(request.form['ticket_service_user']),
        "ticket_service_password":ParameterCheck().secure_parameter(request.form['ticket_service_password']),
        "ticket_support_group":ParameterCheck().secure_parameter(request.form['ticket_support_group']),
        "ticket_assigned_to":ParameterCheck().secure_parameter(request.form['ticket_assigned_to']),
        "ticket_case_url":ParameterCheck().secure_parameter(request.form['ticket_case_url']),
        "ticket_case_id":ParameterCheck().secure_parameter(request.form['ticket_case_id']),
            
        "media_service_url":ParameterCheck().secure_parameter(request.form['media_service_url']),
        "media_service_smtp":ParameterCheck().secure_parameter(request.form['media_service_smtp']),
        "media_service_port":ParameterCheck().secure_parameter(request.form['media_service_port']),
        "media_service_user":ParameterCheck().secure_parameter(request.form['media_service_user']),
        "media_service_password":ParameterCheck().secure_parameter(request.form['media_service_password']),
                
        "created_by":ParameterCheck().secure_parameter(request.form['created_by']),
        "code":ParameterCheck().secure_parameter(request.form['code']),
        "title":ParameterCheck().secure_parameter(request.form['title']),
        "detail":ParameterCheck().secure_parameter(request.form['detail']),
        "effect":ParameterCheck().secure_parameter(request.form['effect']),
        "begin_time":ParameterCheck().secure_parameter(request.form['begin_time']),
        "end_time":ParameterCheck().secure_parameter(request.form['end_time']),
        "duration":"",
                
        "bulletin_resolution_id":ParameterCheck().secure_parameter(request.form['bulletin_resolution_id']),    
        "root_cause":ParameterCheck().secure_parameter(request.form['root_cause']),
        "resolved_time":ParameterCheck().secure_parameter(request.form['resolved_time']), 
        "resolved_by":ParameterCheck().secure_parameter(request.form['resolved_by']),
        "is_resolved":ParameterCheck().secure_parameter(request.form['is_resolved']),

        "insert_time":ParameterCheck().secure_parameter(request.form['insert_time']),
        "modify_time":str(datetime.datetime.now()),
        "is_deleted":"0"
        }
    
    return jsonify(cBulletins().updatebulletin(kwargs))

@app.route("/deletebulletin",methods=['GET'])
#@login_required
def deletebulletin():
    id = ParameterCheck().secure_parameter(request.form['id'])
    return jsonify(cBulletins().deletebulletin(id))

@app.route("/getbulletin",methods=['GET'])
#@login_required
def getbulletin():
    id = ParameterCheck().secure_parameter(request.form['id'])
    return jsonify(cBulletins().getbulletin(id)) 

@app.route("/sendbulletin",methods=['GET'])
#@login_required
def sendbulletin():
    bulletin_id = ParameterCheck().secure_parameter(request.form['bulletin_id'])
    bulletin_procedure_id = ParameterCheck().secure_parameter(request.form['bulletin_procedure_id'])
    return jsonify(cBulletins().sendbulletin(bulletin_id,bulletin_procedure_id)) 

@app.route("/searchbulletin",methods=['GET'])
#@login_required
def searchbulletin():
    code = ParameterCheck().secure_parameter(request.form['code'])
    return jsonify(cBulletins().searchbulletin(code)) 

@app.route("/getallbulletins")
#@login_required
def getallbulletins():
    return jsonify(cBulletins().getallbulletins()) 

@app.route("/gettopbulletins")
#@login_required
def gettopbulletins():
    top = ParameterCheck().secure_parameter(request.form['top'])
    return jsonify(cBulletins().gettopbulletins(top)) 

@app.route("/getactivebulletins")
def getactivebulletins():
    return jsonify(cBulletins().getactivebulletins()) 

@app.route("/getwaitingbulletins")
#@login_required
def getwaitingbulletins():
    return jsonify(cBulletins().getwaitingbulletins()) 

@app.route("/getbulletins")
#@login_required
def getbulletins():
    begin_time = ParameterCheck().secure_parameter(request.form['begin_time'])
    end_time = ParameterCheck().secure_parameter(request.form['end_time'])
    return jsonify(cBulletins().listbulletins(begin_time,end_time)) 

###---------------------------------------------------------------------------------------

@app.route("/creategroup", methods=['GET'])
#@login_required
def creategroup():
    kwargs = {
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "description":ParameterCheck().secure_parameter(request.form['description']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cGroups().creategroup(kwargs))

@app.route("/updategroup", methods=['GET'])
#@login_required
def updategroup():
    kwargs = {
        "id":ParameterCheck().secure_parameter(request.form['id']),
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "description":ParameterCheck().secure_parameter(request.form['description']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cGroups().updategroup(kwargs))
    
@app.route("/deletegroup", methods=['GET'])
#@login_required
def deletegroup(): 
    group_id = ParameterCheck().secure_parameter(request.form['group_id'])
    return jsonify(cGroups().deletegroup(group_id))
   
@app.route("/listgroups", methods=['GET'])
#@login_required
def listgroups(): 
    return jsonify(cGroups().listgroups())
    
@app.route("/getgroup", methods=['GET'])
#@login_required
def getgroup():
    group_id = ParameterCheck().secure_parameter(request.form['group_id'])
    return jsonify(cGroups().getgroup(group_id))

@app.route("/searchgroup", methods=['GET'])
#@login_required
def searchgroup():
    search_text = ParameterCheck().secure_parameter(request.form['search_text'])
    return jsonify(cGroups().searchgroup(search_text))

###---------------------------------------------------------------------------------------

@app.route("/createlanguage", methods=['GET'])
#@login_required
def createlanguage():
    kwargs = {
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "short_name":ParameterCheck().secure_parameter(request.form['short_name']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cLanguages().createlanguage(kwargs))

@app.route("/updatelanguage", methods=['GET'])
#@login_required
def updatelanguage():
    kwargs = {
        "id":ParameterCheck().secure_parameter(request.form['id']),
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "short_name":ParameterCheck().secure_parameter(request.form['short_name']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cLanguages().updatelanguage(kwargs))
    
@app.route("/deletelanguage", methods=['GET'])
#@login_required
def deletelanguage(): 
    language_id = ParameterCheck().secure_parameter(request.form['language_id'])
    return jsonify(cLanguages().deletelanguage(language_id))
   
@app.route("/listlanguages", methods=['GET'])
#@login_required
def listlanguages(): 
    return jsonify(cLanguages().listlanguages())
    
@app.route("/getlanguage", methods=['GET'])
#@login_required
def getlanguage():
    language_id = ParameterCheck().secure_parameter(request.form['language_id'])
    return jsonify(cLanguages().getlanguage(language_id))

@app.route("/searchlanguage", methods=['GET'])
#@login_required
def searchlanguage():
    search_text = ParameterCheck().secure_parameter(request.form['search_text'])
    return jsonify(cLanguages().searchlanguage(search_text))

###---------------------------------------------------------------------------------------

@app.route("/createservice", methods=['GET'])
#@login_required
def createservice():
    kwargs = {
        "group_id":ParameterCheck().secure_parameter(request.form['group_id']),
        "contact_id":ParameterCheck().secure_parameter(request.form['contact_id']),
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "service_url":ParameterCheck().secure_parameter(request.form['service_url']),
        "tag_name_1":ParameterCheck().secure_parameter(request.form['tag_name_1']),
        "tag_name_2":ParameterCheck().secure_parameter(request.form['tag_name_2']),
        "tag_name_3":ParameterCheck().secure_parameter(request.form['tag_name_3']),
        "description":ParameterCheck().secure_parameter(request.form['description']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cServices().createservice(kwargs))

@app.route("/updateservice", methods=['GET'])
#@login_required
def updateservice():
    kwargs = {
        "id":ParameterCheck().secure_parameter(request.form['id']),
        "group_id":ParameterCheck().secure_parameter(request.form['group_id']),
        "contact_id":ParameterCheck().secure_parameter(request.form['contact_id']),
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "service_url":ParameterCheck().secure_parameter(request.form['service_url']),
        "tag_name_1":ParameterCheck().secure_parameter(request.form['tag_name_1']),
        "tag_name_2":ParameterCheck().secure_parameter(request.form['tag_name_2']),
        "tag_name_3":ParameterCheck().secure_parameter(request.form['tag_name_3']),
        "description":ParameterCheck().secure_parameter(request.form['description']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cServices().updateservice(kwargs))
    
@app.route("/deleteservice", methods=['GET'])
#@login_required
def deleteservice(): 
    service_id = ParameterCheck().secure_parameter(request.form['service_id'])
    return jsonify(cServices().deleteservice(service_id))
   
@app.route("/listservices", methods=['GET'])
#@login_required
def listservices():
    group_id = ParameterCheck().secure_parameter(request.form['group_id'])
    return jsonify(cServices().listservices(group_id))
    
@app.route("/getservice", methods=['GET'])
#@login_required
def getservice():
    service_id = ParameterCheck().secure_parameter(request.form['service_id'])
    return jsonify(cServices().getservice(service_id))

@app.route("/searchservice", methods=['GET'])
#@login_required
def searchservice():
    search_text = ParameterCheck().secure_parameter(request.form['search_text'])
    group_id = ParameterCheck().secure_parameter(request.form['group_id'])
    return jsonify(cServices().searchservice(search_text,group_id))

###---------------------------------------------------------------------------------------

@app.route("/createterm", methods=['GET'])
#@login_required
def createerm():
    kwargs = {
        "language_id":ParameterCheck().secure_parameter(request.form['language_id']),
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "value":ParameterCheck().secure_parameter(request.form['value']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cTerms().createterm(kwargs))

@app.route("/updateterm", methods=['GET'])
#@login_required
def updateterm():
    kwargs = {
        "id":ParameterCheck().secure_parameter(request.form['id']),
        "language_id":ParameterCheck().secure_parameter(request.form['language_id']),
        "name":ParameterCheck().secure_parameter(request.form['name']),
        "value":ParameterCheck().secure_parameter(request.form['value']),
        "insert_time":str(datetime.datetime.now()),
        "is_deleted":"0"
    }
    return jsonify(cTerms().updateterm(kwargs))
    
@app.route("/deleteterm", methods=['GET'])
#@login_required
def deleteterm(): 
    term_id = ParameterCheck().secure_parameter(request.form['term_id'])
    return jsonify(cTerms().deleteterm(term_id))
   
@app.route("/listterms", methods=['GET'])
#@login_required
def listterms(): 
    return jsonify(cTerms().listterms())
    
@app.route("/getterm", methods=['GET'])
#@login_required
def getterm():
    term_id = ParameterCheck().secure_parameter(request.form['term_id'])
    return jsonify(cTerms().getterm(term_id))

@app.route("/searchterm", methods=['GET'])
#@login_required
def searchterm():
    search_text = ParameterCheck().secure_parameter(request.form['search_text'])
    return jsonify(cTerms().searchterm(search_text))

###---------------------------------------------------------------------------------------

@app.route("/getservicelistSLA",methods=['GET','POST'])
#@login_required
def getservicelistSLA():
    begin_time = ParameterCheck().secure_parameter(request.form['begin_time'])
    end_time = ParameterCheck().secure_parameter(request.form['end_time'])
    return jsonify(cSLA().get_service_list_SLA(begin_time,end_time)) 

@app.route("/getgrouplistSLA",methods=['GET'])
#@login_required
def getgrouplistSLA():
    begin_time = ParameterCheck().secure_parameter(request.form['begin_time'])
    end_time = ParameterCheck().secure_parameter(request.form['end_time'])
    return jsonify(cSLA().get_group_list_SLA(begin_time,end_time))  

@app.route("/getserviceSLA",methods=['GET'])
#@login_required
def getserviceSLA():
    service_id = ParameterCheck().secure_parameter(request.form['service_id'])
    begin_time = ParameterCheck().secure_parameter(request.form['begin_time'])
    end_time = ParameterCheck().secure_parameter(request.form['end_time'])
    return jsonify(cSLA().get_service_SLA(service_id,begin_time,end_time))  

@app.route("/getgroupSLA",methods=['GET'])
#@login_required
def getgroupSLA():
    group_id = ParameterCheck().secure_parameter(request.form['group_id'])
    begin_time = ParameterCheck().secure_parameter(request.form['begin_time'])
    end_time = ParameterCheck().secure_parameter(request.form['end_time'])
    return jsonify(cSLA().get_group_SLA(group_id,begin_time,end_time))  

@app.route("/getservicebulletins",methods=['GET'])
#@login_required
def getservicebulletins():
    service_id = ParameterCheck().secure_parameter(request.form['service_id'])
    begin_time = ParameterCheck().secure_parameter(request.form['begin_time'])
    end_time = ParameterCheck().secure_parameter(request.form['end_time'])
    return jsonify(cSLA().get_service_bulletins(service_id,begin_time,end_time))  

@app.route("/getgroupbulletins",methods=['GET'])
#@login_required
def getgroupbulletins():
    group_id = ParameterCheck().secure_parameter(request.form['group_id'])
    begin_time = ParameterCheck().secure_parameter(request.form['begin_time'])
    end_time = ParameterCheck().secure_parameter(request.form['end_time'])
    return jsonify(cSLA().get_group_bulletins(group_id,begin_time,end_time))

#@app.route("/setSLAallbulletins",methods=['GET'])
#@login_required
#def setSLAallbulletins():
    #return jsonify(cSLA().set_SLA_all_bulletins())  

###---------------------------------------------------------------------------------------

@app.route("/login",methods=['GET'])
def login():
    authentication_service_url = ParameterCheck().secure_parameter(request.form['authentication_service_url'])
    organization_id = ParameterCheck().secure_parameter(request.form['organization_id'])
    username = ParameterCheck().secure_parameter(request.form['username'])
    password = ParameterCheck().secure_parameter(request.form['password'])
    
    result = cUsers().userlogin(authentication_service_url,organization_id,username,password)
    if result["userid"]:
        user=SessionUser(authentication_service_url,result)
        login_user(user)

    return jsonify(result)

@app.route("/logout",methods=['GET'])
@login_required
def logout():
    authentication_service_url = g.user.url
    sessionusername = g.user.username
    sessionuserid = g.user.userid

    logout_user()
    return jsonify(cUsers().userlogout(authentication_service_url,sessionusername,sessionuserid))

###---------------------------------------------------------------------------------------

@app.route("/listuserlogs", methods=['GET'])
#@login_required
def listuserlogs():
    authentication_service_url = ParameterCheck().secure_parameter(request.form['authentication_service_url'])
    user_id = ParameterCheck().secure_parameter(request.form['user_id'])
    begin_time = ParameterCheck().secure_parameter(request.form['begin_time'])
    return jsonify(cUserLogs().listuserlogs(authentication_service_url,user_id,begin_time))

@app.route("/deletealluserlog", methods=['GET'])
#@login_required
def deletealluserlog(): 
    return jsonify(cUserLogs().deletealluserlog())

###---------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
    
