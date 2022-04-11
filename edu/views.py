
# Create your views here.
from distutils.command.config import config
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

import pyrebase

from django.http import HttpResponse

from .models import Destination1

config={
    'apiKey': 'AIzaSyDEcARcl_W_J_0izDC5XGyRFo1xHIB97Jg',
    'authDomain': 'esp32demo-a6cd3.firebaseapp.com',
    'databaseURL': 'https://esp32demo-a6cd3-default-rtdb.asia-southeast1.firebasedatabase.app',
    'databaseURL': 'https://esp32demo-a6cd3-default-rtdb.asia-southeast1.firebasedatabase.app',
    'projectId': 'esp32demo-a6cd3',
    'storageBucket': 'esp32demo-a6cd3.appspot.com',
    'messagingSenderId': '724212216976',
    'appId': '1:724212216976:web:ad1e28c37eea0ced8c9415'
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

# Create your views here.

def index1(request):
    flag=0
    ref = int(request.POST["ref"])
    pas = int(request.POST["pass"])
    dets=Destination1.objects.all()
    for val in dets:
        if (val.id==ref):
            flag=1
            name=val.name
    if (flag):        
        return render(request,'index1.html',{'name':name,'flag':flag})
    else:
        return render(request,'index.html')
    
def index(request):
    return render(request,'index.html')

def About(request): 
    # send_mail(
    #             'Welcome Email',
    #             'You have been successfully login.',
    #             'okbye260@gmail.com',
    #             ['okbye260@gmail.com'],
    #             fail_silently=False,
    # )
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')


def result(request):
    dets=Destination1.objects.all()
    for val in dets:
            SSN = database.child('test').child('float').get().val()
            Voltage = database.child('test').child('Voltage').get().val()
            Current = database.child('test').child('int').get().val()
            if (val.Password==SSN):
                return render(request,'result.html',{'dets':dets, 'Voltage':Voltage, 'Current':Current, 'Pow':Voltage*Current,'val':val})
        
    