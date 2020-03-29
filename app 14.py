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
    #print(str(uuid.uuid4()))
    return "Hello World! (ZabbixService)"

###---------------------------------------------------------------------------------------

@app.route('/gethosts', methods=['GET'])
def gethosts():
    zabbix_server = request.args.get('zabbix_server',None)
    api_username = request.args.get('api_username',None)
    api_password = request.args.get('api_password',None)
    
    return jsonify(get_hosts(zabbix_server,api_username,api_password))

@app.route('/gethostgroups', methods=['GET'])
def gethostgroups():
    zabbix_server = request.args.get('zabbix_server',None)
    api_username = request.args.get('api_username',None)
    api_password = request.args.get('api_password',None)
    
    return jsonify(get_host_groups(zabbix_server,api_username,api_password))

@app.route("/gettriggers",methods=['GET'])
def gettriggers():
    zabbix_server = request.args.get('zabbix_server',None)
    api_username = request.args.get('api_username',None)
    api_password = request.args.get('api_password',None)
    
    return jsonify(get_triggers(zabbix_server,api_username,api_password))


@app.route("/getitems",methods=['GET'])
def getitems():
    zabbix_server = request.args.get('zabbix_server',None)
    api_username = request.args.get('api_username',None)
    api_password = request.args.get('api_password',None)
    host = request.args.get('host',None)
    key = request.args.get('key',None)
    
    return jsonify(get_items(zabbix_server,api_username,api_password,host,key))

    
@app.route("/getitemaverage",methods=['GET'])
def getitemaverage():
    zabbix_server = request.args.get('zabbix_server',None)
    api_username = request.args.get('api_username',None)
    api_password = request.args.get('api_password',None)
    itemid = request.args.get('itemid',None)
    minutes = request.args.get('minutes',None)
    
    return jsonify(get_item_average(zabbix_server,api_username,api_password,itemid,minutes))

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
    app.run(host='0.0.0.0', port=5006)
    
