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

    def SendMail(self):
        if(self.mailBody == ""):
            return "[ERROR] |: Mail Body cannot be left empty"
        if(self.mailSubject == ""):
            return "[ERROR] |: Please Insert a mail Subject"
        if(self.receiverMail == ""):
            return "[ERROR] |: There is No receiver Specified"
        #Create SMTP session for sending the mail
        #use gmail with port | yahoo with its port
        if("gmail" in self.senderMail):
            self.session = smtplib.SMTP('smtp.gmail.com', 587)
        elif("yahoo" in self.senderMail):
            #self.session = smtplib.SMTP('smtp.mail.yahoo.com', 465)
            print("sorry Yahoo mailing is currently Down")
            return "[FAILED] |: System Dosnt Support Mailing using a Yahoo STMP"
        
        #enable security
        self.session.starttls() 

        #login with mail_id and password
        self.session.login(self.senderMail, self.senderPassword) 
        self.text = self.message.as_string()
        self.session.sendmail(self.senderMail, self.receiverMail, self.text)

        #end session
        self.session.quit()

        #return success status
        return "[SUCCESS] |: Mail Was Sent Successfully"

