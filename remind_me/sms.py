import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from decouple import config

EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')

carriers = {
    'at&t': 'mms.att.net',
    'tmobile': 'tmomail.net',
    'verizon': 'vtext.com',
    'sprint': 'pm.sprint.com'
}


class InvalidCarrier(Exception):
    pass


def send(message, number, carrier):
    if carrier.lower().strip() not in carriers:
        raise InvalidCarrier(f"'{carrier}' is not a valid carrier.")
    to_number = str(number)+'@{}'.format(carriers[carrier.lower().strip()])

    server = smtplib.SMTP('smtp.mail.yahoo.com', 465)
    server.ehlo()
    server.starttls()
    server.login(EMAIL, PASSWORD)

    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = to_number
    msg.attach(MIMEText(message, 'plain'))
    sms = msg.as_string()


    server.sendmail(EMAIL, to_number, sms)
    msg = ''
    server.quit()
