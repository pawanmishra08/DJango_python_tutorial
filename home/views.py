from django.shortcuts import render , redirect
from django.http import HttpResponse
from vege.seed import  *
from .utils import send_email_to_client

# Create your views here.


def send_email(request):
    send_email_to_client()
    return redirect('/')


def home(request):
    # seed_db(10)

    peoples = [
        {'name': 'Abhay Mandal', 'age': 24},
        {'name': 'Yubraj Yadav', 'age': 27},
        {'name': 'Bharamdev Thakur', 'age': 22},
        {'name': 'Niraj Yadav', 'age': 25},
        {'name': 'Ramesh sah', 'age': 23},
    ]

    for people in peoples:
        if people['age'] :
            print("yes")

    vegetables = ['Tomato', 'potato', 'pumpkin']

    # for people in peoples:
    #     print(people)


    return render(request, "index.html", context= {'page': 'Django Tutorial 2025', 'peoples': peoples, 'vegetables': vegetables})

def about(request):
    context = {'page': 'About'}
    return render(request, "about.html", context)

def contact(request):
    context = {'page': 'contact'}
    return render(request, "contact.html", context)

def success_page(request):
    print("*" * 10)
    context = {'page': 'contact'}
    return HttpResponse("<h1>This is success page</h1>")