import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import MY_NUMBER, PASSWORD

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


def send(message, number, carrier):
    if carrier.lower() not in carriers:
        return
    to_number = str(number)+'@{}'.format(carriers[carrier.lower()])
    email, password = 'testagain180@gmail.com', PASSWORD

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = to_number
    #msg['Subject'] = 'Hello\n'
    msg.attach(MIMEText(message, 'plain'))
    sms = msg.as_string()


    server.sendmail(email, to_number, sms)
    server.quit()


def send_multiple_messages(jobs):           #not sure if I'll need this, now that I figured out how to use a for loop
    for job in jobs:                        #with apscheduler
        msg, number, carrier = job
        send(msg, number, carrier)