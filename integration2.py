import requests,json

class Integration():
    
    def send_mail(self,kwargs):        
        session = requests.Session()
        
        headers = {
            "content-type": "application/json"
        }
        print(kwargs)
        
        values = {
            "smtp" : str(kwargs["media_service_smtp"]),
            "port" : str(kwargs["media_service_port"]),
            "user_mail" : str(kwargs["media_service_user"]),
            "password" : str(kwargs["media_service_password"]),
            "tolist" : str(kwargs["tolist"]),
            "cclist" : str(kwargs["cclist"]),
            "bcclist" : str(kwargs["bcclist"]),
            "subject" : str(kwargs["subject"]),
            "body" : str(kwargs["body"])
        }

        url = str(kwargs["media_service_url"]) + "/sendmail"

        response = session.post(
            url=url,
            data =values
        )
        
        session.close()
        return response.content  

    def user_login(self,authentication_service_url,organization_id,username,password):
        session = requests.Session()
        
        headers = {
            "content-type": "application/json"
        }
        
        values = {
            "organization_id" : str(organization_id),
            "username" : username,
            "password" : str(password)
        }
    
        response = session.post(
            url=str(authentication_service_url) + "/userlogin",
            data =values
        )
        
        session.close()
        return json.loads(response.content)

    def user_logout(self,authentication_service_url):
        
        session = requests.Session()
    
        url=authentication_service_url+"/userlogout"
        
        response = session.get(
            url=url
        )
        
        session.close()
        
        return json.loads(response.content)