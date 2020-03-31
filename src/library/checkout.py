# -*- coding: utf-8 -*-
import datetime,requests,json

class CustomCheckout():

    def secure(self,parameter):     
        result =str(parameter) \
            .replace("'",'') \
            .replace('"','') \
            .replace('{','') \
            .replace('}','') \
            .replace('--','') \
            .replace('|','') 
        return result

    def is_int_try(self,value):
        try:
            i = int(value)
        except:
            return False
        return True
    
    def check_length(self,length):
        if length:
            if length !="0":
                if self.is_int_try(length) == True:         
                    return True
                return False
            return False
        return False

    def is_null_string(self,text):
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
