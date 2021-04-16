from uuid import uuid4
from datetime import timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from dateutil.parser import parse
from decouple import config

from remind_me.sms import send
from remind_me.check_email import ReadEmail

jobstore = {'default': SQLAlchemyJobStore(url=config('DATABASE_URL'))}
sched = BackgroundScheduler(jobstores=jobstore)

timezones = {
    'EST': 5, 'EDT': 4,
    'CDT': 5, 'CST': 6,
    'MDT': 6, 'MST': 7,
    'PDT': 7, 'PST': 8,
    'AKDT': 8, 'AKST': 9,
    'Hawaii': 10
}



def scheduled_job(msg, number, carrier):
    send(msg, number, carrier)


def shutdown():
    sched.shutdown(wait=False)


def run_jobs(jobs, timezone):
    for job in jobs:
        if len(job) == 2:
            job, run_date = job
            run_date = parse(run_date) + timedelta(hours=timezones[timezone])
            sched.add_job(shutdown, trigger='date', run_date=run_date)
        else:
            msg, number, carrier, run_date = job
            run_date = parse(run_date) + + timedelta(hours=timezones[timezone])
            sched.add_job(scheduled_job, args=(msg,number,carrier), trigger='date', run_date=run_date,
                            id=str(uuid4()))


def main(jobs, timezone):
    run_jobs(jobs, timezone)
    print(sched.get_jobs())
    try:
        sched.start()
    except:
        pass


if __name__ == '__main__':
    main()


