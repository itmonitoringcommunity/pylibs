# -*- coding: utf-8 -*-
# You need to set the Allow less secure apps: ON,
# login to google using the account desired,
# and go to the security page
# and set the Allow less secure apps to be ON.
# https://www.google.com/settings/security/lesssecureapps

import smtplib

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gaierror


class CustomMail():
    def __init__(self):
        self.msg = ''

    def send_mail_with_files(self, kwargs, attachments=None):
        msg = MIMEMultipart()
        msg['From'] = kwargs["username"]
        msg['To'] = kwargs["tolist"]
        msg['Cc'] = kwargs["cclist"]
        msg['Bcc'] = kwargs["bcclist"]
        msg['Subject'] = kwargs["subject"]
        msg.attach(MIMEText(kwargs["body"], 'html'))

        if attachments is not None:
            for file in attachments:
                # print(file.filename)
                part = MIMEApplication(
                    file.stream.read(),
                    Name=file.filename
                )
                # After the file is closed
                part['Content-Disposition'] = (
                    'attachment; filename="{0}"').format(file.filename)
                msg.attach(part)

        try:
            server = smtplib.SMTP(kwargs["smtp"], kwargs["port"])
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(kwargs["username"], kwargs["password"])

            # maili gönderiyoruz. Aldığı parametreler gonderenin mail adresi, alıcının mail adresi, ve mail içeriği
            recipients = kwargs["cclist"].split(
                ",") + kwargs["bcclist"].split(",") + [kwargs["tolist"]]
            # print(recipients)
            server.sendmail(kwargs["username"], recipients, msg.as_string())
            server.quit()
            self.msg = "Notification mail is sent successfuly."
        except smtplib.SMTPException as e:
            self.msg = "Some smtp parameters are invalid " + str(e)
        except gaierror as e:
            self.msg = "No internet access " + str(e)

    def send_mail(self, kwargs, attachments=None):
        msg = MIMEMultipart()
        msg['From'] = kwargs["username"]
        msg['To'] = kwargs["tolist"]
        msg['Cc'] = kwargs["cclist"]
        msg['Bcc'] = kwargs["bcclist"]
        msg['Subject'] = kwargs["subject"]
        msg.attach(MIMEText(kwargs["body"], 'html'))

        if attachments is not None:
            for file in attachments:
                # print(file.filename)
                part = MIMEApplication(
                    file.stream.read(),
                    Name=file.filename
                )
                # After the file is closed
                part['Content-Disposition'] = (
                    'attachment; filename="{0}"').format(file.filename)
                msg.attach(part)
        try:
            server = smtplib.SMTP(kwargs["smtp"], kwargs["port"])
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(kwargs["username"], kwargs["password"])

            # maili gönderiyoruz. Aldığı parametreler gonderenin mail adresi, alıcının mail adresi, ve mail içeriği
            recipients = kwargs["cclist"].split(
                ",") + kwargs["bcclist"].split(",") + [kwargs["tolist"]]
            # print(recipients)
            server.sendmail(kwargs["username"], recipients, msg.as_string())
            server.quit()

            self.msg = "Notification mail is sent successfuly."
        except smtplib.SMTPException as e:
            self.msg = "Some smtp parameters are invalid " + str(e)
        except gaierror as e:
            self.msg = "No internet access " + str(e)
