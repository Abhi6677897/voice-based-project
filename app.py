import os
import smtplib
import speech_recognition as sr
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyttsx3

listener = sr.Recognizer()
tts = pyttsx3.init()

def talking_tom(text):
    tts.say(text)
    tts.runAndWait()

def mic():
    with sr.Microphone() as source:
        print ("program is listening....")
        voice = listener.listen(source)
        listener.adjust_for_ambient_noise(source)
        data = listener.recognize_google(voice)
        print(data)
        return data.lower()

dict = {"abhi":"kadamabhishek613@gmail.com",
        "madhuri":"kadammadhuri314@gmail.com"}

def send_mail(receiver,subject,body, attachment_path=None):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("your@gmaill.com","password")
    email = MIMEMultipart()
    email["From"] = "your@gmail.com"
    email["To"] = receiver
    email["Subject"] = subject
    email.attach(MIMEText(body))

    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            email.attach(part)

    server.send_message(email)

def main():
    talking_tom("To whom do you want to send this email?")
    name = mic()
    receiver = dict[name]
    talking_tom("Speak the subject of the email")
    subject = mic()
    talking_tom("Speak the message of the email")
    body = mic()
    talking_tom("Do you want to attach a file? If yes, speak 'yes', else speak 'no'")
    response = mic()
    if response == 'yes':
        talking_tom("Please specify the file path of the attachment")
        attachment_path = mic()
        send_mail(receiver, subject, body, attachment_path)
    else:
        send_mail(receiver, subject, body)
    talking_tom("your email has been sent")
    print("your email has been sent")

main()
