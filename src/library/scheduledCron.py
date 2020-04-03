from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
import datetime


def job_function():
    print("Cron Scheduler " + str(datetime.datetime.now()))


trigger = OrTrigger([
    CronTrigger(hour='7', minute='30-59'),
    CronTrigger(hour='8-22', minute='*'),
    CronTrigger(hour='23', minute='0-30')
])


class CustomScheduledCron():
    def __init__(self):
        self.msg = ''
        self.sched = BackgroundScheduler()

    def add_jobs(self):
        self.sched.add_job(job_function, 'interval', seconds=6)
        self.sched.add_job(job_function, trigger)

    def start(self):
        try:
            self.sched = BackgroundScheduler()
            self.add_jobs()
            self.sched.start()
        except Exception as e:
            self.msg = "" + str(e)
        self.msg = "Corn Scheduler Service is started"

    def stop(self):
        try:
            self.sched.shutdown()
        except Exception as e:
            self.msg = "" + str(e)
        self.msg = "Cron Scheduler Service is stopped"

    def restart(self):
        try:
            self.sched.shutdown()
            self.sched = BackgroundScheduler()
            self.add_jobs()
            self.sched.start()
        except Exception as e:
            self.msg = "" + str(e)
        self.msg = "Cron Scheduler Service is restarted"
