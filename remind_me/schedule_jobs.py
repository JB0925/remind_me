from sms import send
from check_email import ReadEmail

from apscheduler.schedulers.background import BlockingScheduler

sched = BlockingScheduler()


def add():
    print(2+2)


def subtract():
    print(7-3)


def multiply():
    print(4*4)


def scheduled_job(func, msg, number, carrier):
    func(msg, number, carrier)


def shutdown():
    sched.shutdown(wait=False)

jobs = [
    (send, 'kids dentist appt @ 12:30', 5409035731, 'Verizon', '04-01-2021 10:10'),
    (send, 'go to sleep @ 11:30', 5409035731, 'verizon', '04-01-2021 10:11'),
    (send, 'xyz', 2813308004, 'att', '04-01-10:12'),
    (shutdown, '04-01-2021 10:13')
]


for job in jobs:
    if 'shutdown' in job[0]:
        job, run_date = job
        sched.add_job(shutdown, trigger='date', run_date=run_date)
    job, msg, number, carrier, run_date = job     
    sched.add_job(scheduled_job, args=(job,msg,number,carrier), trigger='date', run_date=run_date)
    
print(sched.get_jobs())
sched.start()


