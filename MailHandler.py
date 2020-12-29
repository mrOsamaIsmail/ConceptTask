import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MailHandler:
    def __init__(self,sender,senderPasswrd,receiver):
        #Sender Credentials
        self.senderMail = sender
        self.senderPassword = senderPasswrd
        #Receiver Mail
        self.receiverMail = receiver
        

    def constructMail(self,mailsubject,mailbody):
        #The Actual Mail
        self.mailSubject = mailsubject
        self.mailBody = mailbody
        #The SMTP service
        self.smtpService = ""
        self.smtpPort = ""
        #Setup the MIME
        self.message = MIMEMultipart()
        self.message['From'] = self.senderMail
        self.message['To'] = self.receiverMail
        #the subject
        self.message['Subject'] = self.mailSubject 
        #The body and the attachments for the mail
        self.message.attach(MIMEText(self.mailBody, 'plain'))

