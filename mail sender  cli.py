from MailHandler import MailHandler

#The mail addresses and password
sender_address =input("enter sender email :")
#default sender 
if(sender_address ==""):
    sender_address = 'debuggerconcept@gmail.com'
sender_pass =input("enter sender password : ")

#default password
if(sender_pass ==""):
    sender_pass= 'c_951753'
mail_subject = input("enter subject :")

mail_content = input("enter mail content :")

receiver_address = input("enter receiver mail :")
if(receiver_address == ""):
    receiver_address = "os9104236@gmail.com" 
    
mail = MailHandler(sender_address,sender_pass,receiver_address)
mail.constructMail(mail_subject,mail_content)
print(mail.SendMail())






















