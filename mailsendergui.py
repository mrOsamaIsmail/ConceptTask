from MailHandler import MailHandler

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class gui():

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GMAIL MAIL SENDING APP")
        self.window.geometry("600x350")
        Seperator = tk.Label(text="-----------------")
        self.greeting = tk.Label(text="Gmail Mail Sender")
        self.greeting.pack()
        Seperator.pack()

        sendermlabel = tk.Label(text="Sender Gmail Accunt")
        sendermlabel.pack()

        self.senderMailE = tk.Entry(width=50)
        self.senderMailE.pack()

        senderPasswrd = tk.Label(text= "Sender password :")
        senderPasswrd.pack()

        self.senderPass = tk.Entry(width=50)
        self.senderPass.pack()

        note = tk.Label(text="*note :mail account must have the allow unknown apps login enabled*")
        note.pack()
        notice = tk.Label(text="in case of empty sender credintials the DebuggerConcept@gmail would be used as a  sender")
        notice.pack()

        receiverMailLabel = tk.Label(text="To")
        receiverMailLabel.pack()

        self.receiverMail = tk.Entry(width=50)
        self.receiverMail.pack()

        MailSubjectLabel = tk.Label(text="Subject")
        MailSubjectLabel.pack()

        self.MailSubject = tk.Entry(width=50)
        self.MailSubject.pack()

        MailContentLabel = tk.Label(text="Mail")
        MailContentLabel.pack()

        self.MailContent = tk.Entry(width=50)
        self.MailContent.pack()

        
        Seperator.pack()

        Enter = tk.Button(text="Send Mail",width=30,command=self.SendMail)
        Enter.pack()

        self.resultLABEl = tk.Label(text="")
        self.resultLABEl.pack()
        
    def MainLoop(self):
        self.window.mainloop()

    def SendMail(self):
        
        #The mail addresses and password
        sender_address = self.senderMailE.get()
        #default sender 
        if(sender_address ==""):
            sender_address = 'debuggerconcept@gmail.com'
        
        sender_pass =  self.senderPass.get()
        #default password
        if(sender_pass ==""):
            sender_pass= 'c_951753'
        
        self.error = ""

        mail_subject = self.MailSubject.get()
        mail_content = self.MailContent.get()
        receiver_address = self.receiverMail.get()

        mail = MailHandler(sender_address,sender_pass,receiver_address)
        mail.constructMail(mail_subject,mail_content)

        self.error = mail.SendMail()
        
        self.resultLABEl.config(text = self.error)
        if(("ERROR" in self.error)):
            return
        else:
            self.ClearInputs()
        
        
    def ClearInputs(self):
        self.senderMailE.delete(0, 'end')
        self.MailContent.delete(0, 'end')
        self.MailSubject.delete(0, 'end')
        self.receiverMail.delete(0, 'end')
        self.senderPass.delete(0, 'end')

Gui = gui()
Gui.MainLoop()




















