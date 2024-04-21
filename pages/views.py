from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def company(request):
    return render(request, 'pages/company_info.html')

def login(request):
    return render(request, 'pages/login.html')
# Create your views here.
