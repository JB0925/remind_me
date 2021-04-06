import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from decouple import config

MY_NUMBER = config('MOBILE_NUMBER')
EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')


carriers = {
    'att': 'mms.att.net',
    'tmobile': 'tmomail.net',
    'verizon': 'vtext.com',
    'sprint': 'page.nextel.com'
}

jobs = [
    ('Hi from Python', MY_NUMBER, 'Verizon'),
    ('dentist appointment', MY_NUMBER, 'verizon'),
    ('dah dah dah', 2813308004, 'squigglydodah')
]


class InvalidCarries(Exception):
    pass


def send(message, number, carrier):
    carrier = carrier.lower()

    if carrier not in carriers:
        raise InvalidCarries(f"'{carrier}' not a valid carrier")

    to_number = f'{number}@{carriers[carrier]}'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL, PASSWORD)

    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to_number
    #msg['Subject'] = 'Hello\n'
    msg.attach(MIMEText(message, 'plain'))
    sms = msg.as_string()


    server.sendmail(EMAIL, to_number, sms)
    server.quit()


def send_multiple_messages(jobs):           #not sure if I'll need this, now that I figured out how to use a for loop
    for job in jobs:                        #with apscheduler
        msg, number, carrier = job
        send(msg, number, carrier)
