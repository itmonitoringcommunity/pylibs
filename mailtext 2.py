# -*- coding: utf-8 -*-
import datetime
from models import BulletinProcedures,BulletinStates,BulletinTypes,Bulletins,Groups,Languages,Services,SLA,Terms

class MailText():
    
    def calculate_duration(self,begin_time,end_time):
        d1 = datetime.datetime.strptime(begin_time,'%Y-%m-%d %H:%M:%S')
        if not end_time:
            d2 = datetime.datetime.now()
        else:
            d2 = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        
        diff = (d2-d1)
        
        mins = diff.total_seconds() / 60
        return str(int(round(mins)))
    
    def generate_bulletin_code(self):
        text="BLT" + Bulletins().getallbulletincount().zfill(6)        
        return text
    
    def get_title_bulletin(self,kwargs):
        text = (kwargs[21]+ " - " + 
            Terms().gettermwithlanguage("Bulletin.Type." + str(BulletinTypes().getbulletintype(kwargs[3])[1]).replace(" ",""), kwargs[1]) + " - " + 
            str(kwargs[6]).replace(" ","") + " - " + #bulletin_priority
            Terms().gettermwithlanguage("Bulletin.State." + str(BulletinStates().getbulletinstate(kwargs[4])[1]).replace(" ",""), kwargs[1])
            )
        return text
    
    def get_text_bulletin(self,kwargs):
        text=""
        text += "<center><table border='1' style='width:500px;'>"
        text += "<tr>"
        text += "<td colspan='2' style='background-color: #808080;vertical-align:central;padding:10px;'>"
        text += "<table border='0'><tr><td style='width:260px;font-weight: bold;color: white;font-size: 35px; '>"
        text += kwargs[21] #code
        text += "</td><td style='text-align:right;font-weight: bold;color: white; '> <span style=''>Service Monitoring Center</span><br /><span style=''>"
        text += kwargs[2] #modify_time
        text += "</td></tr></table></td>"
        text += "</tr>"
        
        text += "<tr>"
        text += "<td colspan='2' style='font-size: 28px;padding:10px;'>"
        text += "<span style='font-weight: bold; color: " + BulletinStates().getbulletinstate(kwargs[4])[3] + "'>"
        text += kwargs[22] #title
        text += "</span></td>"
        text += "</tr>"      
        
        text += "<tr style='background-color: #D3D3D3;'>"
        text += "<td style='width: 200px; font-weight: bold; padding: 10px;'>"
        text += Terms().gettermwithlanguage("Bulletin.Type", kwargs[1])
        text += "</td>"
        text += "<td style='width: 300px; padding: 10px;'>"
        text += Terms().gettermwithlanguage("Bulletin.Type." + str(BulletinTypes().getbulletintype(kwargs[3])[1]).replace(" ",""), kwargs[1])
        
        
        text += "</td>"
        text += "</tr>"
        
        text += "<tr>"
        text += "<td style='width: 200px; font-weight: bold; padding: 10px;'>"
        text += Terms().gettermwithlanguage("Bulletin.Detail", kwargs[1])
        text += "</td>"
        text += "<td style='padding: 10px;'>"
        text += kwargs[23] #detail
        text += "</td>"
        text += "</tr>"
        text += "<tr style='background-color: #D3D3D3;'>"
        text += "<td style='width: 200px; font-weight: bold; padding: 10px;'>"
        text += Terms().gettermwithlanguage("Bulletin.Effect", kwargs[1])
        text += "</td>"
        text += "<td style='padding: 10px;'>"
        text += kwargs[24] #effect
        text += "</td>"
        text += "</tr>"
        
        text += "<tr>"
        text += "<td style='width: 200px; font-weight: bold; padding: 10px;'>"
        text += Terms().gettermwithlanguage("Bulletin.Responsible", kwargs[1])
        text += "</td>"
        text += "<td style='padding: 10px;'>"
        text += kwargs[7] #contact
        text += "</td>"
        text += "</tr>"
        text += "<tr style='background-color: #D3D3D3;'>"
        text += "<td style='width: 200px; font-weight: bold; padding: 10px;'>"
        text += Terms().gettermwithlanguage("Bulletin.BeginTime", kwargs[1])
        text += "</td>"
        text += "<td style='padding: 10px;'>"
        text += kwargs[25] #begin_time
        text += " (TR)</td>"
        text += "</tr>"
        
        text += "<tr>"
        text += "<td style='width: 200px; font-weight: bold; padding: 10px;'>"
        text += Terms().gettermwithlanguage("Bulletin.EndTime", kwargs[1])
        text += "</td>"
        text += "<td style='padding: 10px;'>"
        
        if not kwargs[26]:    
            text += Terms().gettermwithlanguage("Bulletin.Undefined", kwargs[1])
        else:
            text += kwargs[26] + " (TR)" #end_time
        
        text += "</td>"
        text += "</tr>"
        
        if kwargs[14]: #case_id
            text += "<tr style='background-color: #D3D3D3;'>"
            text += "<td style='width: 200px; font-weight: bold; padding: 10px;'>"
            text += Terms().gettermwithlanguage("Bulletin.CaseId", kwargs[1])
            text += "</td>"
            text += "<td style='padding: 10px;'><a href='"+ kwargs[13] +"'>" #ticket_case_url
            text += kwargs[14] #ticket_case_id
            text += "</a></td>"
            text += "</tr>"
            
        if kwargs[26]: #end_time
            text += "<tr style='background-color: #D3D3D3;'>"
            text += "<td style='width: 200px; font-weight: bold; padding: 10px;'>"
            text += Terms().gettermwithlanguage("Bulletin.Duration", kwargs[1])
            text += "</td>"
            text += "<td style='padding: 10px;'>" 
            text += kwargs[27] #duration
            text += " (" + Terms().gettermwithlanguage("Bulletin.Minute", kwargs[1]) + ") </td>"
            text += "</tr>"
        
        text += "<tr>"
        text += "<td style='width: 200px; font-weight: bold; padding: 10px;'>"
        text += Terms().gettermwithlanguage("Bulletin.Priority", kwargs[1])
        text += "</td>"
        text += "<td style='padding: 10px;'>" 
        text += kwargs[6] #bulletin_priority
        text += "</td>"
        text += "</tr>"
        
        text += "<tr style='background-color: #D3D3D3;'>"
        text += "<td style='width: 200px; font-weight: bold; padding: 10px;'>"
        text += Terms().gettermwithlanguage("Bulletin.State", kwargs[1])
        text += "</td>"
        text += "<td style='padding: 10px;color:white;"
        text += "background-color: " + BulletinStates().getbulletinstate(kwargs[4])[3] + ";'>"
        text += Terms().gettermwithlanguage("Bulletin.State." + str(BulletinStates().getbulletinstate(kwargs[4])[1]).replace(" ",""), kwargs[1])
        text += "</td>"
        text += "</tr>"
        
        text += "<tr>"
        text += "<td style='width: 200px; font-weight: bold; padding: 10px;'>"
        text += Terms().gettermwithlanguage("Bulletin.CreatedBy", kwargs[1])
        text += "</td>"
        text += "<td style='padding: 10px;'>"
        text += kwargs[20] #created_by
        text += "</td>"
        text += "</tr>"
        text += "</table>"
        text += "</center>"
        
        return text
