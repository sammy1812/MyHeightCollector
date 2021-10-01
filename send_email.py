from email.mime.text import MIMEText
import smtplib as mail_send
def send_email(email, height,avg_height,cou):
    from_email = "height.collector123@gmail.com"
    from_password = "fast_and_furious"
    to_email = email

    subject = "Height data"
    message = f"hey {to_email}, your height is <strong>{height}cm</strong>. Out of <strong>{cou}</strong> entries,the average height of the all is <strong>{avg_height}cm</strong>"
    msg = MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    gmail = mail_send.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
