import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

smtpserveraddress = "<To be replaced>"
smtpaccount = "<To be replaced>"
smtpport = 587
smtppassword = "<To be replaced>"
fromaddress = "<To be replaced>"
toaddress ="<To be replaced>"
subject = "test message"
body = "This is test"

smtpobj = smtplib.SMTP(smtpserveraddress,smtpport)
smtpobj.set_debuglevel(True)
smtpobj.login(smtpaccount, smtppassword)

msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = fromaddress
msg['To'] = toaddress
msg['Date'] = formatdate()
print(msg)

smtpobj.sendmail(fromaddress, toaddress, msg.as_string())
smtpobj.close()
