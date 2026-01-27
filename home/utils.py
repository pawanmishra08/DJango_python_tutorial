from home.models import Student
import time
from django.core.mail import send_mail , EmailMessage
from django.conf import settings

def run_this_function():
    print("Function Started !!!")
    print("Function Started !!!")

    time.sleep(2) # Simulating a delay of 2 seconds
    print("Function Excuted Successfully !!!")

def send_email_to_client():
    subject = "Test Email from Django Application"
    message = "This is a test message from Django Application."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [""]  # whom you want to send the email
    send_mail(subject , message, from_email, recipient_list)

def send_email_with_attachment(subject, message , recipient_list, file_path):
    mail = EmailMessage(subject= subject, body = message, from_email= settings.EMAIL_HOST_USER,
                        to= [recipient_list]
                         )
    mail.attach_file(file_path)
    mail.send()