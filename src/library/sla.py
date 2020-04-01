# -*- coding: utf-8 -*-
import datetime,sqlite3,re

class CustomSLA:
    def __init__(self):
        self.data_services={}
        self.descrption =""
        self.pattern = "(tag1 | tag2 |tag3 |tag 4)" 

    def find_bulletins(self):
        value_text = self.descrption
        pattern = self.pattern               
        
        m = re.search(pattern, value_text,re.IGNORECASE)        
        
        if m:
            # This is reached.
            print("search:", m.group(1))
           
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
    
    
    
    