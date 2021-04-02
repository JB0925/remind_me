from .sms import send
from .check_email import ReadEmail

from apscheduler.schedulers.background import BlockingScheduler

sched = BlockingScheduler()


def add():
    print(2+2)


def subtract():
    print(7-3)


def multiply():
    print(4*4)


def scheduled_job(job):
    print(job())


def shutdown():
    sched.shutdown(wait=False)

jobs = [(add, 23, 10), (subtract, 23, 11), (multiply, 23,12), (shutdown, 23, 13)]


for job in jobs:                #if I wrap this in a function to make it callable, it won't work. This is the only way I could get it to work. If I put it in a function, it only ran one job.
    job, hour, minute = job     #it works with the decorator in the link I showed you, but that will only run one job.
    id_ = str(job) + str(minute) #as in, I may need to run three jobs in a row, or a job now, 36 minutes from now, etc.
    sched.add_job(scheduled_job, args=(job,), trigger='cron', day_of_week='wed', hour=hour, minute=minute, id=id_)
    
print(sched.get_jobs())
sched.start()


