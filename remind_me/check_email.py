import imaplib
import email
from decouple import config
from remind_me.sms import PASSWORD

EMAIL = config('EMAIL')
PASSWORD = config('PASSWORD')


class ReadEmail:
    def __init__(self, email: str = EMAIL, password: str = PASSWORD):
        self.email = email
        self.password = password
        self.imap = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        self.messages = []


    def login(self):
        self.imap.login(self.email, self.password)
        self.imap.select('"[Gmail]/All Mail"')


    def get_messages(self):
        result, data = self.imap.uid('search', None, 'All')
        if result == 'OK':
            for num in data[0].split():
                temp = []
                result, data = self.imap.uid('fetch', num, '(RFC822)')
                if result == 'OK':
                    email_message = email.message_from_bytes(data[0][1])
                    temp.append(email_message['From'])
                    if email_message.is_multipart():
                        for part in email_message.get_payload():
                            temp.append(part.get_payload())
                    else:
                        temp.append(email_message.get_payload())
                self.messages.append(temp)
                    
        self.imap.close()
        self.imap.logout()
        return self.messages[-1]


def main():
    reader = ReadEmail()
    reader.login()
    print(reader.get_messages())


if __name__ == '__main__':
    main()
