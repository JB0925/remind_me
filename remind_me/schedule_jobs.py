from apscheduler.schedulers.background import BackgroundScheduler
from dateutil.parser import parse

from remind_me.sms import send
from remind_me.check_email import ReadEmail

sched = BackgroundScheduler({'apscheduler.timezone': 'EST'})


def scheduled_job(msg, number, carrier):
    send(msg, number, carrier)


def shutdown():
    sched.shutdown(wait=False)


def run_jobs(jobs=None):
    for job in jobs:
        if len(job) == 2:
            job, run_date = job
            run_date = parse(run_date)
            sched.add_job(shutdown, trigger='date', run_date=run_date)
        else:
            msg, number, carrier, run_date = job
            run_date = parse(run_date)
            sched.add_job(scheduled_job, args=(msg,number,carrier), trigger='date', run_date=run_date)


def main(jobs=None):
    run_jobs(jobs)
    print(sched.get_jobs())
    try:
        sched.start()
    except:
        pass


if __name__ == '__main__':
    main()


