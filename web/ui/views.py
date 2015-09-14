from django.shortcuts import render

def register_view(request):
    return render(request, 'ui/register.html')

def login_view(request):
    return render(request, 'ui/login.html')
