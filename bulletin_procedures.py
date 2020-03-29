# -*- coding: utf-8 -*-

import sqlite3

class BulletinProcedures():
    
    def __init__(self):
        self.conn = sqlite3.connect("models/bulletinservice.db")

    def __del__(self):
        self.conn.close()   
    
    def createbulletinprocedure(self,kwargs):
        try:
            if self.bulletinprocedurenotexist(kwargs["name"]) == True:           
                command =("INSERT INTO bulletin_procedures(name,description,tolist,cclist,bcclist,insert_time,is_deleted) " +  
                          "VALUES ('{0}','{1}','{2}','{3}','{4}','{5}',{6})").format(kwargs["name"],kwargs["description"],kwargs["tolist"],kwargs["cclist"],kwargs["bcclist"],kwargs["insert_time"],kwargs["is_deleted"])
                self.c = self.conn.cursor()
                self.c.execute(command)
                self.conn.commit()
                return {"status":"true", "id":str(self.c.lastrowid)}
            else:
                return {"status":"false", "message":"this username was inserted"}
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}

    def updatebulletinprocedure(self,kwargs):
        try:            
            command =("update bulletin_procedures set name='{1}',description='{2}',tolist='{3}',cclist='{4}',bcclist='{5}',insert_time='{6}',is_deleted={7} "+ 
                      "where id={0}").format(kwargs["id"],kwargs["name"],kwargs["description"],kwargs["tolist"],kwargs["cclist"],kwargs["bcclist"],kwargs["insert_time"],kwargs["is_deleted"])
            self.c = self.conn.cursor()
            self.c.execute(command)
            self.conn.commit()
            return {"status":"true", "value":kwargs["id"]}
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}
    
    def deletebulletinprocedure(self,id):
        try:
            command =("update bulletin_procedures set is_deleted=1 where id={0} and is_deleted=0").format(id)
            self.c = self.conn.cursor()
            self.c.execute(command)
            self.conn.commit()
            return {"status":"true"}
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}
    
    def listbulletinprocedures(self):
        try:
            command =("select * from bulletin_procedures where is_deleted=0 ORDER BY name ASC")
            self.c = self.conn.cursor()
            self.c.execute(command)
            self.conn.commit()
            data = self.c.fetchall()
            return data
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}
    
    def getbulletinprocedure(self,id):
        try:
            command =("select * from bulletin_procedures where id={0} and is_deleted=0").format(id)
            self.c = self.conn.cursor()
            self.c.execute(command)
            self.conn.commit()
            data =self.c.fetchall()
            
            if len(data) != 0:
                return data[0]
            else:
                return False
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}
    
    def searchbulletinprocedure(self,text):
        try:
            command =("select * from bulletin_procedures where name like '%{0}%' and is_deleted=0 ORDER BY name ASC").format(text)
            self.c = self.conn.cursor()
            self.c.execute(command)
            self.conn.commit()
            data = self.c.fetchall()
            return data
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}
    
    def bulletinprocedurenotexist(self,name):
        try:           
            command =("select * from bulletin_procedures where name='{0}' is_deleted=0").format(name)
            self.c = self.conn.cursor()
            self.c.execute(command)
            self.conn.commit()
            
            data = self.c.fetchall()
            if len(data) == 0:
                return True
            else:
                return False
        except sqlite3.Error as er:
            return {"status":"false", "message":str(er.args[0])}
        