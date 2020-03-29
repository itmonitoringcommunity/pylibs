import requests,json,os

class Integration():
    def check_session(self,authentication_service_url,organization_key,session_token):
        session = requests.Session()
        
        values = {
            "organization_key": organization_key,
            "session_token": session_token              
        }
        response = session.get(
            url=authentication_service_url+"/checksession",
            data=values
        )
        
        session.close()
        return json.loads(response.content)["organization"]