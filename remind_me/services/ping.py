from datetime import datetime, timedelta

import requests
from apscheduler.schedulers.background import BackgroundScheduler
from dateutil.parser import parse

from remind_me.data import db_session
from remind_me.data.events import Events
from remind_me.schedule_jobs import timezones
from remind_me.sms import send

scheduler = BackgroundScheduler()


@scheduler.scheduled_job('interval', minutes=20)
def ping_site() -> None:
    session = db_session.create_session()
    all_events = session.query(Events).filter(Events.sent == False).all()
    print(all_events)
    for ev in all_events:
        event_time = parse(ev.date_and_time) + timedelta(hours=timezones[ev.timezone])
        current_time = datetime.now()
        if current_time > event_time:
            ev.sent = True
            session.commit()
            send(ev.event, ev.phone_number, ev.carrier)
    response = requests.get('https://desolate-garden-98632.herokuapp.com/')
    print(response.status_code)


def make_pings():
    scheduler.start()
    print(scheduler.get_jobs())