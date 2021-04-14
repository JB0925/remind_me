from apscheduler.schedulers.background import BackgroundScheduler
from dateutil.parser import parse
from datetime import timedelta

from remind_me.sms import send
from remind_me.check_email import ReadEmail

sched = BackgroundScheduler()

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
            sched.add_job(scheduled_job, args=(msg,number,carrier), trigger='date', run_date=run_date)


def main(jobs, timezone):
    run_jobs(jobs, timezone)
    print(sched.get_jobs())
    try:
        sched.start()
    except:
        pass


if __name__ == '__main__':
    main()


