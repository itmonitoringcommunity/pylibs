import requests,os,json

class Integration():
    def upload_attachments(self,exportimport_service_url,user_mail,attachments):
        attachment_ids = ""
        if attachments:
            for file in attachments:
                #file.save("Attachments/"+file.filename)   
                #f = open("Attachments/"+file.filename, 'rb')
                files = {'file_data':(file.filename, file)}
                values = {
                    "user_mail": user_mail,
                    "description": "description"                
                }
                
                response = requests.post(
                    url=exportimport_service_url+"/importfile",  
                    files=files,
                    data=values            
                    )
                
                attachment_ids = attachment_ids + str(json.loads(response.content)["id"]) + ','
                #f.close()
                #os.remove("Attachments/"+file.filename)

        attachment_ids = attachment_ids.strip(',')
        return attachment_ids
    
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