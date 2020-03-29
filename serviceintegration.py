import requests


def send_mail(media_service_url,media_service_smtp,media_service_port,media_service_user,media_service_password,user_mail,subject,body,tolist,cclist,bcclist):
    #get_text_reset_user_password(user[4],password,user[16],user[17]),
    
    session = requests.Session()
    
    headers = {
        "content-type": "application/json"
    }
    
    values = {
        "smtp" : str(media_service_smtp),
        "port" : media_service_port,
        "user" : str(media_service_user),
        "password" : str(media_service_password),
        "tolist" : str(tolist),
        "cclist" : str(cclist),
        "bcclist" : str(bcclist),
        "subject" : str(subject),
        "body" : str(body)
    }

    response = session.post(
        url=str(media_service_url) + "/sendmail",
        data =values
    )
    
    session.close()
    return response.content

def get_active_bulletins():
    text=""
    return text

def get_waiting_assets():
    text=""
    return text

def get_waiting_contracts():
    text=""
    return text