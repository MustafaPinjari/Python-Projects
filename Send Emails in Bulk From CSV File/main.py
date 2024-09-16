import csv 
from email.message import EmailMessage
import smtplib

def get_credentials(filepath):
    with open("crerdentials.txt", "r") as f:
        email_address = f.readline()
        emial_pass = f.readline()
    return (email_address, emial_pass)
def login(email_address, emial_pass, s):
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(email_address, emial_pass)
    print("login")

def send_mail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    email_address, emial_pass = get_credentials("crerdentials.txt")
    login(email_address, emial_pass, s)
    subject = "Welcome to Mustafa's Python project Repo"
    body = '''
        Follow us on socials
        '''
    message =EmailMessage()
    message.set_content(body)
    message['Subject'] = subject

    with open("Your Csv file containing emails", newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for email in spamreader:
            s.send_message(email_address, email[0], message)
            print("Send to "+ email[0])

    s.quit()
    print("Sent")

if __name__ == "__main__":
    send_mail()