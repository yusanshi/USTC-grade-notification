import smtplib
from email.mime.text import MIMEText
from email.header import Header
from config import *


def send_mail(text):
    message = MIMEText('<h1>'+text+'</h1>', 'html', 'utf-8')
    message['From'] = SENDER
    message['To'] = RECEIVER
    message['Subject'] = Header(text, 'utf-8')

    a = 'Sender <%s>' % SENDER
    print(a)
    smtpObj = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT)
    smtpObj.login(SMTP_USERNAME, SMTP_PASSWORD)
    smtpObj.sendmail(SENDER,
                     [RECEIVER], message.as_string())
    smtpObj.quit()


if __name__ == "__main__":
    # Test
    send_mail("出分啦！")