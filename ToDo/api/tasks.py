from celery import shared_task
from time import sleep
from ToDo.celery import app
from django.core.mail import send_mail

@app.task
def send_email_task():
    sleep(5)
    send_mail('Тема Задание', 'Executed/Not Exectued', 'beket_test@mail.ru', ['beket_test2@mail.ru'])