# -*- coding: utf-8 -*-
import uuid

class MailText():
    def generate_token(self):
        return str(uuid.uuid4())

    def get_text_user_register(self,username,password,name,surname):
        text = "<p>Dear "+name +" "+ surname +",</p><br/><br/>" + \
            "<p>Your registeration is completed and account information is below.</p><br/><br/>"+ \
            "<p>Username: " +username +"<br/>"+ \
            "<p>Password: " +password +"<br/>"+ \
            "<br/><p>Best Regards,<br/>"
            
        return text
    
    def get_text_user_reset_password(self,username,password,name,surname):
        text = "<p>Dear "+name +" "+ surname +",</p><br/><br/>" + \
            "<p>Your password is changed and it is below.</p><br/><br/>"+ \
            "<p>Username: " +username +"</p><br/>"+ \
            "<p>Password: " +password +"</p><br/>"+ \
            "<br/><p>Best Regards,</p><br/>"
            
        return text
