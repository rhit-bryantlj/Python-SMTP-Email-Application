#!/usr/bin/python

import smtplib

sender = 'Eggsy@rose-hulman.edu'
receivers = ['bryantlj@rose-hulman.edu']

message = """From: Eggsy <eggsy@rose-hulman.edu>
To: Logan Bryant <bryantlj@rose-hulman.edu>
MIME-Version: 1.0
Content-type: alternative
Subject: CSSE432 Homework 2 Logan Bryant

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
   smtpObj = smtplib.SMTP('rosehulman-edu01b.mail.protection.outlook.com', 25)
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")