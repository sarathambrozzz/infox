from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def profiledash(request):
    return render(request,'profiledash.html')

def Training(request):
    return render(request,'Training.html')

def trainingteam1(request):
    return render(request,'trainingteam1.html')
def trainerstable(request):
    return render(request,'trainerstable.html')
def topictable(request):
    return render(request,'topictable.html')
def completedtasktable(request):
    return render(request,'completedtasktable.html')
def trainingprofile(request):
    return render(request,'trainingprofile.html')
def traineestable(request):
    return render(request,'traineestable.html')     
                   

