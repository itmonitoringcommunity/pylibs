# -*- coding: utf-8 -*-
import datetime,requests,json
from models import SessionInformations

class ParameterCheck():

    def secure_parameter(self,parameter):     
        result =str(parameter) \
            .replace("'",'') \
            .replace('"','') \
            .replace('{','') \
            .replace('}','') \
            .replace('--','') \
            .replace('|','') 
        return result

    def isInt_try(self,v):
        try:
            i = int(v)
        except:
            return False
        return True
    
    def check_length(self,length):
        if length:
            if length !="0":
                if self.isInt_try(length) == True:         
                    return True
                return False
            return False
        return False

    def check_int(self,value):
        if value:
            if self.isInt_try(value) == True:
                return value
            return 0
        return 0
    
    def check_salt_and_password(self,salt,password):
        if salt and password:
            return True
        return False
    
    def check_password(self,password):
        if password:
            return True
        return False
    
    def check_parameters_hashed(self,salt,password,hashed):
        if salt and password and hashed:
            return True
        return False

    def check_null_string(self,text):
        if text:
            return True
        return False

    def is_datetime(self,dt):
        dt = dt.split('.')[0]
        try:
            print(dt)
            dt_obj = datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M:%S') 
        except ValueError:
            return False
            
        return True

    def check_user_mail(self, user_mail):
        if user_mail:
            return True
        return False

    def check_url_response(self,url):
        if url:
            response = requests.get(
                url=url
            )
            if response.status_code == 200:
                return True
                
        return False

    def check_attachments(self,attachments):
        if attachments:
            for file in attachments:
                if file.filename:
                    return True
        return False
    
    def check_session_organization_value(self,id=None,name=None,organization_key=None,session_token=None):
        result = SessionInformations().checksession(organization_key,session_token)

        if id and json.loads(result)["status"]=="true":
            if json.loads(result)["organization_id"]==id:
                return True
        if name and json.loads(result)["status"]=="true":
            if json.loads(result)["organization"]==name:
                return True
        if id==None and name==None and json.loads(result)["status"]=="true":
            return True
        
        return False

    def check_sessioninformation_parameter(self,kwargs,idcheck=False):
        if idcheck == True:
            if self.check_length(kwargs["id"]) == False:
                return False
        if self.check_length(kwargs["user_id"]) == False:
            return False
        if self.check_null_string(kwargs["session_token"]) == False:
            return False
        if self.check_int(kwargs["is_login_success"]) == False:
            return False
        if self.check_int(kwargs["is_logout_success"]) == False:
            return False
        if self.is_datetime(kwargs["insert_time"]) == False:
            return False
        if self.check_int(kwargs["is_deleted"]) == False:
            return False

        return True

    def check_organization_parameter(self,kwargs,idcheck=False):
        if idcheck == True:
            if self.check_length(kwargs["id"]) == False:
                return False
        if self.check_null_string(kwargs["name"]) == False:
            return False
        if self.check_null_string(kwargs["key"]) == False:
            return False
        if self.is_datetime(kwargs["insert_time"]) == False:
            return False
        if self.check_int(kwargs["is_deleted"]) == False:
            return False

        return True
    
    def check_department_parameter(self,kwargs,idcheck=False):
        if idcheck == True:
            if self.check_length(kwargs["id"]) == False:
                return False
        if self.check_length(kwargs["organization_id"]) == False:
            return False
        if self.check_null_string(kwargs["name"]) == False:
            return False
        if self.is_datetime(kwargs["insert_time"]) == False:
            return False
        if self.check_int(kwargs["is_deleted"]) == False:
            return False

        return True

    def check_application_parameter(self,kwargs,idcheck=False):
        if idcheck == True:
            if self.check_length(kwargs["id"]) == False:
                return False
        if self.check_length(kwargs["organization_id"]) == False:
            return False
        if self.check_null_string(kwargs["name"]) == False:
            return False
        if self.is_datetime(kwargs["insert_time"]) == False:
            return False
        if self.check_int(kwargs["is_deleted"]) == False:
            return False

        return True

    def check_role_parameter(self,kwargs,idcheck=False):
        if idcheck == True:
            if self.check_length(kwargs["id"]) == False:
                return False
        if self.check_length(kwargs["application_id"]) == False:
            return False
        if self.check_null_string(kwargs["name"]) == False:
            return False
        if self.is_datetime(kwargs["insert_time"]) == False:
            return False
        if self.check_int(kwargs["is_deleted"]) == False:
            return False

        return True
    
    def check_usernotification_parameter(self,kwargs,idcheck=False):
        if idcheck == True:
            if self.check_length(kwargs["id"]) == False:
                return False
        if self.check_length(kwargs["user_id"]) == False:
            return False
        if self.check_null_string(kwargs["type"]) == False:
            return False
        if self.check_null_string(kwargs["name"]) == False:
            return False
        if self.check_null_string(kwargs["icon"]) == False:
            return False
        if self.check_null_string(kwargs["url"]) == False:
            return False
        if self.check_null_string(kwargs["description"]) == False:
            return False
        if self.is_datetime(kwargs["insert_time"]) == False:
            return False
        if self.check_int(kwargs["is_deleted"]) == False:
            return False

        return True

    def check_menu_parameter(self,kwargs,idcheck=False):
        if idcheck == True:
            if self.check_length(kwargs["id"]) == False:
                return False
        if self.check_length(kwargs["role_id"]) == False:
            return False
        if self.check_null_string(kwargs["name"]) == False:
            return False
        if self.check_null_string(kwargs["link_text"]) == False:
            return False
        if self.is_datetime(kwargs["insert_time"]) == False:
            return False
        if self.check_int(kwargs["is_deleted"]) == False:
            return False
        
        return True

    def check_title_parameter(self,kwargs,idcheck=False):
        if idcheck == True:
            if self.check_length(kwargs["id"]) == False:
                return False
        if self.check_null_string(kwargs["name"]) == False:
            return False
        if self.is_datetime(kwargs["insert_time"]) == False:
            return False
        if self.check_int(kwargs["is_deleted"]) == False:
            return False

        return True

    def check_contact_parameter(self,kwargs,idcheck=False):
        if idcheck == True:
            if self.check_length(kwargs["id"]) == False:
                return False
        if self.check_null_string(kwargs["name"]) == False:
            return False
        if self.is_datetime(kwargs["insert_time"]) == False:
            return False
        if self.check_int(kwargs["is_deleted"]) == False:
            return False

        return True

    def check_user_parameter(self,kwargs,idcheck=False):
        if idcheck ==True:
            if self.check_length(kwargs["id"]) == False:
                return False
        if self.check_length(kwargs["title_id"]) == False:
            return False
        if self.check_length(kwargs["role_id"]) == False:
            return False
        if self.check_length(kwargs["department_id"]) == False:
            return False
        if self.check_null_string(kwargs["username"]) == False:
            return False
        if self.check_null_string(kwargs["user_mail"]) == False:
            return False
        if self.check_url_response(kwargs["media_service_url"]) == False:
            return False
        if self.check_null_string(kwargs["media_service_smtp"]) == False:
            return False
        if self.check_null_string(kwargs["media_service_port"]) == False:
            return False
        if self.check_null_string(kwargs["media_service_user"]) == False:
            return False
        if self.check_null_string(kwargs["media_service_password"]) == False:
            return False
        if self.check_url_response(kwargs["security_service_url"]) == False:
            return False
        if self.check_url_response(kwargs["exportimport_service_url"]) == False:
            return False
        if self.check_null_string(kwargs["name"]) == False:
            return False
        if self.check_null_string(kwargs["surname"]) == False:
            return False
        if self.check_null_string(kwargs["gender"]) == False:
            return False
        if self.is_datetime(kwargs["insert_time"]) == False:
            return False
        if self.check_int(kwargs["is_deleted"]) == False:
            return False

        return True
    
    
    