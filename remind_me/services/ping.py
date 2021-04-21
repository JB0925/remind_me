import requests
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval', minutes=30)
def ping_site() -> None:
    response = requests.get('https://desolate-garden-98632.herokuapp.com/')
    print(response.status_code)


def make_pings():
    scheduler.start()
    print(scheduler.get_jobs())