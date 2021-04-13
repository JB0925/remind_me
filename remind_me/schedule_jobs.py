from apscheduler.schedulers.background import BlockingScheduler
from dateutil.parser import parse

from remind_me.sms import send
from remind_me.check_email import ReadEmail

sched = BlockingScheduler()


def scheduled_job(msg, number, carrier):
    send(msg, number, carrier)


def shutdown():
    sched.shutdown(wait=False)


def add_job(job):
    if len(job) == 2:
        job, run_date = job
        run_date = parse(run_date)
        sched.add_job(shutdown, trigger='date', run_date=run_date)
    else:
        msg, number, carrier, run_date = job
        run_date = parse(run_date)
        sched.add_job(scheduled_job, args=(msg,number,carrier), trigger='date', run_date=run_date)
