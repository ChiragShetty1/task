from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def clients(request):
    return render(request,"clients.html")
def register(request):
    return render(request,"register.html")
def training(request):
    return render(request,"training.html")
def exam(request):
    return render(request,"exam.html")