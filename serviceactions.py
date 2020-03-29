# -*- coding: utf-8 -*-
import threading
import time

class BulletinThread (threading.Thread):
    def __init__(self, threadID, name, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay
      self.stoprequest = threading.Event()
      
    def start(self):
        threading.Thread.start(self)
        
    def stop(self):
        self.stoprequest.set()
        
    def restart(self):
        threading.Thread.__init__(self)
        threading.Thread.start(self)
    
    def run(self):
        #print("Starting " + self.name)
        while not self.stoprequest.isSet():
            send_bulletin_notifications()
            time.sleep(self.delay)
            #print("Bulletin Exiting " + str(datetime.datetime.now()))
            
class AssetThread (threading.Thread):
    def __init__(self, threadID, name, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay
      self.stoprequest = threading.Event()

    def start(self):
        threading.Thread.start(self)
        
    def stop(self):
        self.stoprequest.set()

    def restart(self):
        threading.Thread.__init__(self)
        threading.Thread.start(self)

    def run(self):
        #print("Starting " + self.name)
        while not self.stoprequest.isSet():
            send_asset_notifications()
            time.sleep(self.delay)
            #print("Asset Exiting " + str(datetime.datetime.now()))
            
class ContractThread (threading.Thread):
    def __init__(self, threadID, name, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.delay = delay
      self.stoprequest = threading.Event()

    def start(self):
        threading.Thread.start(self)
        
    def stop(self):
        self.stoprequest.set()

    def restart(self):
        threading.Thread.__init__(self)
        threading.Thread.start(self)

    def run(self):
        #print("Starting " + self.name)
        while not self.stoprequest.isSet():
            send_contract_notifications()
            time.sleep(self.delay)
            #print("Contract Exiting " + str(datetime.datetime.now()))
        
def send_bulletin_notifications():
    text=""
    return text

def send_asset_notifications():
    text=""
    return text

def send_contract_notifications():
    text=""
    return text