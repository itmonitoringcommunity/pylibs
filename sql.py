# -*- coding: utf-8 -*-

import sqlite3,threading
from sqlite3 import Error
from pathlib import Path

# Our thread class
class sqlthread (threading.Thread):
 
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run (self):
        dbfile="models/bulletinservice.db"
        sqlfile="models/bulletinservice.sql"
        DBCreation(dbfile,sqlfile)
        
class DBCreation:

    def __init__(self,dbfile,sqlfile):        
        my_file = Path(dbfile)
        if my_file.is_file()==False:
            # file not exists
            self.create_connection(dbfile)
            self.executeScriptsFromFile(sqlfile)
            self.conn.close()
    
    def executeScriptsFromFile(self,filename):
        # Open and read the file as a single buffer
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()
    
        # all SQL commands (split on ';'       
        sqlCommands = sqlFile.replace('\n','').replace('\t','').replace('    ',' ').split(';')
        
        
        # Execute every command from the input file
        for command in sqlCommands[0:-1]:
            print(command + ' \n\n')
            # This will skip and report errors
            # For example, if the tables do not yet exist, this will skip over
            # the DROP TABLE commands
            try:
                c = self.conn.cursor()
                c.execute(command)
                self.conn.commit()
            except sqlite3.OperationalError:
                print("Command skipped: ", sqlite3.OperationalError)
    
    
    def create_connection(self,db_file):
        """ create a database connection to a SQLite database """
        try:
            self.conn = sqlite3.connect(db_file)            
            print(sqlite3.version)
        except Error as e:
            print(e)
 
def start():
    sqlthread().start()
        