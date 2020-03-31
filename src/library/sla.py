# -*- coding: utf-8 -*-
import datetime,sqlite3,re

class SLA:
    
    def __init__(self):
        self.conn = sqlite3.connect('models/bulletinservice.db')
        
    def __del__(self):
        self.conn.close()

    
    def set_streaming_SLA(self,bulletin_id):
        try:
            command_deleteoldviewdatas=("delete from groupped_bulletin_view where bulletin_id={0} and is_deleted=0").format(bulletin_id)
            self.c = self.conn.cursor()
            self.c.execute(command_deleteoldviewdatas)
            self.conn.commit()
            
            command_getbulletin = ("select * from bulletins where id={0} and is_deleted=0").format(bulletin_id)
            self.c = self.conn.cursor()
            self.c.execute(command_getbulletin)
            self.conn.commit()
            data_bulletin = self.c.fetchall()
            
            
            command_getservices = ("select * from services where is_deleted=0")
            self.c = self.conn.cursor()
            self.c.execute(command_getservices)
            self.conn.commit()
            data_services = self.c.fetchall()
            
            for service in data_services:
                service_id = service[0]
                group_id = service[1]
                                
                # Input.
                value_text = data_bulletin[0][19]
                pattern = "("+ service[3] +"|"+ service[5] +"|"+ service[6] +"|"+ service[7] +")"                
                
                m = re.search(pattern, value_text,re.IGNORECASE)        
                
                if m:
                    # This is reached.
                    #print("search:", m.group(1))
                                
                    command_insertview = ("INSERT INTO groupped_bulletin_view(bulletin_id,bulletin_type_id,bulletin_state_id,code,duration,group_id,service_id,begin_time,end_time,insert_time,is_deleted)"+ \
                              "VALUES ({0},{1},{2},'{3}',{4},{5},{6},'{7}','{8}','{9}',{10})"). \
                              format(bulletin_id,data_bulletin[0][3],data_bulletin[0][5],data_bulletin[0][16],data_bulletin[0][22],group_id,service_id,data_bulletin[0][20],data_bulletin[0][21],data_bulletin[0][25],0)
                    self.c = self.conn.cursor()
                    self.c.execute(command_insertview)
                    self.conn.commit()
                
            return {"status":"true"}
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}
    
    def set_SLA_all_bulletins(self):
        command_deleteview = ("delete from groupped_bulletin_view")
        self.c = self.conn.cursor()
        self.c.execute(command_deleteview)
        self.conn.commit()

        command_getallbulletins = ("select * from bulletins where is_deleted=0")
        self.c = self.conn.cursor()
        self.c.execute(command_getallbulletins)
        self.conn.commit()
        data_bulletins = self.c.fetchall()

        for bulletin in data_bulletins:
            self.set_streaming_SLA(bulletin[0][0])
        return {"status":"true"}

    def calculate_SLA(self,outage_minutes,begin_time,end_time):
        d1 = datetime.datetime.strptime(begin_time,'%Y-%m-%d %H:%M:%S')
        if not end_time:
            d2 = datetime.datetime.now()
        else:
            d2 = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        
        diff = (d2-d1)
        
        total_minutes = diff.total_seconds() / 60
        sla = 100.00

        if outage_minutes:
            sla = 100 - (int(outage_minutes)/int(round(total_minutes)) * 100)
        
        return ("{0:.2f}").format(sla)
    
    def get_service_SLA(self,service_id,begin_time,end_time):        
        try:
            bulletin_type_id = 3
            bulletin_state_id = 4
            command = ("select sum(duration) from groupped_bulletin_view where bulletin_type_id={0} and bulletin_state_id={1} and service_id={2} and begin_time >='{3}' and end_time <='{4}' and is_deleted=0").format(bulletin_type_id,bulletin_state_id,service_id,begin_time,end_time)
            self.c = self.conn.cursor()
            self.c.execute(command)
            self.conn.commit()
            data = self.c.fetchone()[0]
            #print(data)
            sla = self.calculate_SLA(data,begin_time,end_time) 
            return(sla)
            
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}
        
    def get_group_SLA(self,group_id,begin_time,end_time):
        try:
            bulletin_type_id = 3
            bulletin_state_id = 4
            command = ("select sum(duration) from groupped_bulletin_view where bulletin_type_id={0} and bulletin_state_id={1} and group_id={2} and begin_time >='{3}' and end_time <='{4}' and is_deleted=0").format(bulletin_type_id,bulletin_state_id,group_id,begin_time,end_time)
            self.c = self.conn.cursor()
            self.c.execute(command)
            self.conn.commit()
            data = self.c.fetchone()[0]
            sla = self.calculate_SLA(data,begin_time,end_time) 
            return(sla)
            
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}
    
    def get_service_list_SLA(self,begin_time,end_time):
        command_getservices = ("select * from services where is_deleted=0")
        self.c = self.conn.cursor()
        self.c.execute(command_getservices)
        self.conn.commit()
        data_services = self.c.fetchall()
        sla_list=[]
        
        for service in data_services:
            service_id = service[0]
            name = service[3]
            sla = self.get_service_SLA(service_id,begin_time,end_time)
            sla_list.append({"id":service_id,"name":name,"sla":sla})
        
        return sla_list
        
    def get_group_list_SLA(self,begin_time,end_time):
        command_getgroups = ("select * from groups where is_deleted=0")
        self.c = self.conn.cursor()
        self.c.execute(command_getgroups)
        self.conn.commit()
        data_groups = self.c.fetchall()
        sla_list=[]
        
        for group in data_groups:
            group_id = group[0]
            name = group[1]
            sla = self.get_group_SLA(group_id,begin_time,end_time)
            sla_list.append({"id":group_id,"name":name,"sla":sla})
        
        return sla_list
    
    def get_service_bulletins(self,service_id,begin_time,end_time):        
        try:
            command = ("select distinct g.bulletin_id,b.* from groupped_bulletin_view as g JOIN bulletins as b ON(g.bulletin_id=b.id) where g.service_id={0} and g.begin_time >='{1}' and g.end_time <='{2}' and g.is_deleted=0 ORDER BY datetime(b.begin_time) DESC").format(service_id,begin_time,end_time)
            self.c = self.conn.cursor()
            self.c.execute(command)
            self.conn.commit()
            data = self.c.fetchall()
            #print(data)
            return(data)
            
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}
            
    def get_group_bulletins(self,group_id,begin_time,end_time):
        try:
            command = ("select distinct g.bulletin_id,b.* from groupped_bulletin_view as g JOIN bulletins as b ON(g.bulletin_id=b.id) where g.group_id={0} and g.begin_time >='{1}' and g.end_time <='{2}' and g.is_deleted=0 ORDER BY datetime(b.begin_time) DESC").format(group_id,begin_time,end_time)
            self.c = self.conn.cursor()
            self.c.execute(command)
            self.conn.commit()
            data = self.c.fetchall()
            #print(data)
            return(data)
            
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}
    