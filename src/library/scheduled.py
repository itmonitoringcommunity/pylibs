# -*- coding: utf-8 -*-
import threading
import time

from .mail import *

mail = CustomMail()


class CustomScheduled():
    def __init__(self):
        self.thread_b = CustomThread(1, "Thread-1", 6)  # for each 6 seconds
        self.thread_a = CustomThread(2, "Thread-2", 6)  # for each 6 seconds
        self.thread_c = CustomThread(3, "Thread-3", 6)  # for each 6 seconds
        self.msg = ''

    def send_notifications(self, title, content):
        kwargs = {
            'smtp': 'smtp.gmail.com',
            'port': '587',
            'username': 'itmonitoringcommunity@gmail.com',
            'password': 'MonitoringCommunity18',
            'tolist': 'oguzkaragoz@gmail.com',
            'cclist': 'itmonitoringcommunity@gmail.com',
            'bcclist': '',
            'subject': title,
            'body': content
        }

        mail.send_mail(kwargs)
        print(mail.msg)

    def start(self):
        try:
            self.thread_b.start()
            self.thread_a.start()
            self.thread_c.start()
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is started"

    def stop(self):
        try:
            self.thread_b.stop()
            self.thread_a.stop()
            self.thread_c.stop()
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is stopped"

    def restart(self):
        try:
            self.thread_b.restart()
            self.thread_a.restart()
            self.thread_c.restart()
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is restarted"


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
        # print("Starting " + self.name)
        while not self.stoprequest.isSet():
            # print("Notification " + str(datetime.datetime.now()))
            # send_notifications('test title', 'test content')
            time.sleep(self.delay)
