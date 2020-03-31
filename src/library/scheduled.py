# -*- coding: utf-8 -*-
import threading
import time

def send_notifications():
    text=""
    return text

    
class CustomScheduled():
    def __init__(self):
        self.thread_b = CustomThread(1, "Thread-1", 6)  # for each 6 seconds
        self.thread_a = CustomThread(2, "Thread-2", 6)  # for each 6 seconds
        self.thread_c = CustomThread(3, "Thread-3", 6)  # for each 6 seconds

    def start(self):   
        try:
            self.thread_b.start()
            self.thread_a.start()
            self.thread_c.start()
        except Exception as e:
            return print({"status":"false","message":e})
        
        return print({"status":"true","value":"Scheduler Service is started"})

    def stop(self):
        try:
            self.thread_b.stop()
            self.thread_a.stop()
            self.thread_c.stop()
        except Exception as e:
            return print({"status":"false","message":e})
        
        return print({"status":"true","value":"Scheduler Service is stopped"})

    def restart(self):
        try:
            self.thread_b.restart()
            self.thread_a.restart()
            self.thread_c.restart()
        except Exception as e:
            return print({"status":"false","message":e})
        
        return print({"status":"true","value":"Scheduler Service is restarted"})



class CustomThread (threading.Thread):
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
            send_notifications()
            time.sleep(self.delay)
            #print("Notification " + str(datetime.datetime.now()))
  
