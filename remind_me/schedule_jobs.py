from remind_me.sms import send
from remind_me.check_email import ReadEmail

from apscheduler.schedulers.background import BlockingScheduler
from dateutil.parser import parse

sched = BlockingScheduler()


def add():
    print(2+2)


def subtract():
    print(7-3)


def multiply():
    print(4*4)


def scheduled_job(msg, number, carrier):
    send(msg, number, carrier)


def shutdown():
    sched.shutdown(wait=False)

jobs = [
    ('kids dentist appt @ 12:30', 5409035731, 'Verizon', '04-02-2021 20:55'),
    ('go to sleep @ 11:30', 5409035731, 'verizon', '04-02-2021 20:56'),
    ('xyz', 2813308004, 'att', '04-02-2021 20:57'),
    (shutdown, '04-02-2021 20:58')
]


for job in jobs:
    if len(job) == 2:
        job, run_date = job
        run_date = parse(run_date)
        sched.add_job(shutdown, trigger='date', run_date=run_date)
    else:
        msg, number, carrier, run_date = job
        run_date = parse(run_date)
        sched.add_job(scheduled_job, args=(msg,number,carrier), trigger='date', run_date=run_date)
    
print(sched.get_jobs())
sched.start()


