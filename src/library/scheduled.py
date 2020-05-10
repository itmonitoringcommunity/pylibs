# -*- coding: utf-8 -*-
import threading
import datetime
import time


class CustomScheduled():
    def __init__(self, API):
        self.API = API
        self.thread_a = CustomThread(1, "Thread-1", API)
        self.msg = ''

    def start(self):
        try:
            self.thread_a.start()
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is started"

    def stop(self):
        try:
            self.thread_a.stop()
            self.thread_a = CustomThread(1, "Thread-1", self.API)
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is stopped"

    def restart(self):
        try:
            self.thread_a.restart()
        except Exception as e:
            self.msg = "" + str(e)

        self.msg = "Scheduler Service is restarted"


class CustomThread (threading.Thread):
    def __init__(self, threadID, name, API):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = 20
        self.api = API

        self.stoprequest = threading.Event()

    def __check_scheduled_bulletins(self):
        self.api.get_scheduled_bulletins()

        for bulletin in self.api.scheduledBulletins:
            if (bulletin["is_automated"] == "1") and (bulletin["state"] == "Scheduled"):
                dt = datetime.datetime.strptime(bulletin["begin_time"].split('+')[0],
                                                "%Y-%m-%dT%H:%M:%S")

                if datetime.datetime.now() >= dt:
                    bulletin["color"] = "#e55353"
                    bulletin["state"] = "Started"
                    self.api.bulletin = bulletin
                    self.api.id = str(bulletin["id"])
                    self.api.set_bulletin()
                    self.api.send_bulletin()
                    print(dt, ' ', self.api.id, ' ', bulletin["code"],
                          ' Started state was processed.', '\n')

    def __check_started_bulletins(self):
        self.api.get_started_bulletins()

        for bulletin in self.api.startedBulletins:

            if (bulletin["is_automated"] == "1") and (bulletin["state"] == "Started"):
                if (bulletin["end_time"] is not None) or (bulletin["end_time"] is not ""):
                    dt = datetime.datetime.strptime(bulletin["end_time"].split('+')[0],
                                                    "%Y-%m-%dT%H:%M:%S")

                    if datetime.datetime.now() >= dt:
                        bulletin["is_automated"] = "0"
                        bulletin["color"] = "#2eb85c"
                        bulletin["state"] = "Done"
                        self.api.bulletin = bulletin
                        self.api.id = str(bulletin["id"])
                        self.api.set_bulletin()
                        self.api.send_bulletin()
                        print(dt, ' ', self.api.id, ' ', bulletin["code"],
                              ' Done state was processed.', '\n')

    def run_check_bulletins(self):
        self.__check_scheduled_bulletins()
        self.__check_started_bulletins()

    def start(self):
        threading.Thread.start(self)

    def stop(self):
        self.stoprequest.set()

    def restart(self):
        threading.Thread.__init__(self)
        threading.Thread.start(self)

    def run(self):
        while not self.stoprequest.isSet():
            self.run_check_bulletins()
            time.sleep(self.delay)
