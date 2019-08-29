import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import getpass

from databases.db_actions import subs_view_subs
from databases.db_conn_decr import dbconnect
from scraper.hrs_scraper import get_rabbit_link
from templates.templates import email_tmpl

sender_email = "therabbitdaily@gmail.com"
password = 'Ih8uih8u'

message = MIMEMultipart("alternative")
message["Subject"] = "The Rabbit Daily"
message["From"] = 'The Hasty Rabbit Courier'

# Create the plain-text and HTML version of your message
text = """\
Whatup there should be a rabbit here"""
email_html = email_tmpl(get_rabbit_link())

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(email_html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    
    with dbconnect('databases/subscribers.db') as conn:
        subs = subs_view_subs(conn, test=True)
        for sub in subs:
            server.sendmail(
                sender_email, sub[1], message.as_string()
            )