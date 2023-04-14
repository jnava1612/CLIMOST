import smtplib

from email.mime.text import MIMEText


def sendnotification(sender_email, sender_password, receivers, subject, message, to_html = False):
    text_type = "plain"
    if to_html:
        text_type = "html"
    email_message = MIMEText(message, text_type)
    email_message['Subject'] = subject
    email_message['From'] = sender_email
    email_message['To'] = ', '.join(receivers)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, sender_password)
    for receiver in receivers:
        server.sendmail(sender_email, receivers, email_message.as_string())
    server.quit()    
    
sender = "pmvc.umss@gmail.com"
senderpwd = "ngznomqnkfhzgued"
receptores = ["navajorgeeduardo@gmail.com", "nava.sejas.jorge@gmail.com"]
print("mandando correo")

sendnotification(sender, senderpwd, receptores, "Prueba Funcion", "Mensaje de Prueba")

print("correo enviado")
